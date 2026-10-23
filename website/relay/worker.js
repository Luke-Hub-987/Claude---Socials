// ERN sign-up relay (Cloudflare Worker), 23 Oct 2026.
//
// Why it exists: iPhone Safari refused to let the site talk to klaviyo.com
// at all ("Load failed", normal and private tabs), because klaviyo.com is on
// tracker lists. So the site posts here instead, and this Worker talks to
// Klaviyo server-to-server with a private API key. The visitor's phone never
// contacts klaviyo.com, and Klaviyo's bot filter doesn't apply to a server.
//
// Settings (Worker > Settings > Variables and Secrets):
//   KLAVIYO_PRIVATE_KEY  secret, pk_... with Profiles, Lists, Subscriptions: full access
//   KLAVIYO_LIST_ID      Vw9wxY (Email List)
//   ALLOWED_ORIGIN       https://engineroomnutrition.com
//
// The site sends a plain form post (no CORS pre-check):
//   email, source, props (JSON of profile properties), company (honeypot, must be empty)
// Two calls to Klaviyo, in order, so nothing races:
//   1. profile-import: create or update the profile with the plan details
//   2. subscription job: email marketing consent + add to the list, which
//      starts the "Added to list" welcome flow (single opt-in list)
// Every sign-up and every failure is logged (Worker > Logs) to count them.

const KLAVIYO = 'https://a.klaviyo.com/api/';
const REVISION = '2024-10-15';
const EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

export default {
  async fetch(request, env) {
    const origin = request.headers.get('Origin') || '';
    const allowed = (env.ALLOWED_ORIGIN || '').split(',').map(s => s.trim()).filter(Boolean);
    const ok = allowed.includes(origin);
    const cors = {
      'Access-Control-Allow-Origin': ok ? origin : allowed[0] || '',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Vary': 'Origin'
    };
    const reply = (status, body) => new Response(JSON.stringify(body), { status, headers: { ...cors, 'Content-Type': 'application/json' } });

    if (request.method === 'OPTIONS') return new Response(null, { status: 204, headers: cors });
    const path = new URL(request.url).pathname;
    if (request.method !== 'POST') return reply(405, { ok: false, error: 'POST only' });
    if (!ok) return reply(403, { ok: false, error: 'origin not allowed' });

    let form;
    try { form = await request.formData(); } catch (e) { return reply(400, { ok: false, error: 'bad form' }); }

    // the site reports a failed save here so failures can be counted
    if (path.endsWith('/log')) {
      console.log(JSON.stringify({ kind: 'site-failure', reason: String(form.get('reason') || '').slice(0, 200), app: String(form.get('app') || '').slice(0, 40), source: String(form.get('source') || '').slice(0, 60) }));
      return reply(200, { ok: true });
    }

    if (form.get('company')) { console.log(JSON.stringify({ kind: 'honeypot' })); return reply(200, { ok: true }); } // a bot: pretend it worked
    const email = String(form.get('email') || '').trim().toLowerCase();
    if (!EMAIL.test(email) || email.length > 200) return reply(400, { ok: false, error: 'invalid email' });
    const source = String(form.get('source') || 'Website').slice(0, 60);
    let props = {};
    try { props = JSON.parse(String(form.get('props') || '{}')); } catch (e) { props = {}; }
    if (typeof props !== 'object' || Array.isArray(props) || props === null) props = {};
    const clean = {};
    for (const [k, v] of Object.entries(props).slice(0, 40)) {
      if (!/^[a-z0-9_]{1,40}$/i.test(k) || v === '' || v == null) continue;
      clean[k] = typeof v === 'boolean' || typeof v === 'number' ? v : String(v).slice(0, 200);
    }
    clean.signup_source = source;

    if (!env.KLAVIYO_PRIVATE_KEY || !env.KLAVIYO_LIST_ID) return reply(500, { ok: false, error: 'relay not configured' });
    const headers = {
      'Authorization': 'Klaviyo-API-Key ' + env.KLAVIYO_PRIVATE_KEY,
      'revision': REVISION, 'accept': 'application/vnd.api+json', 'content-type': 'application/vnd.api+json'
    };
    const call = async (path, data) => {
      const r = await fetch(KLAVIYO + path, { method: 'POST', headers, body: JSON.stringify({ data }) });
      if (!r.ok) throw new Error(path + ' ' + r.status + ' ' + (await r.text()).slice(0, 300));
      return r;
    };

    try {
      await call('profile-import/', { type: 'profile', attributes: { email, properties: clean } });
      await call('profile-subscription-bulk-create-jobs/', {
        type: 'profile-subscription-bulk-create-job',
        attributes: {
          custom_source: source,
          profiles: { data: [{ type: 'profile', attributes: { email, subscriptions: { email: { marketing: { consent: 'SUBSCRIBED' } } } } }] }
        },
        relationships: { list: { data: { type: 'list', id: env.KLAVIYO_LIST_ID } } }
      });
      console.log(JSON.stringify({ kind: 'signup', source, domain: email.split('@')[1] }));
      return reply(200, { ok: true });
    } catch (e) {
      console.log(JSON.stringify({ kind: 'klaviyo-error', source, error: String(e.message).slice(0, 300) }));
      return reply(502, { ok: false, error: 'klaviyo' });
    }
  }
};
