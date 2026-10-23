/* ERN site: shared behaviour for both pages. */
window.ERN = (function(){
  // Klaviyo: the company ID is the public site ID already on the live site.
  // One list for everyone (Luke, 23 Oct): Email List. The waitlist and the
  // results form use it too; what someone signed up for is saved on their
  // profile (bar_waitlist, result_time) and the sign-up source, so a segment
  // can pick them out later. While the list ID is empty, forms run in
  // preview mode and send nothing.
  var KLAVIYO = { company: 'RhFsS3', planList: '', waitlistList: '', resultsList: '', relay: '' };
  // On Shopify the list IDs come from the section settings (theme editor),
  // written into window.ERN_CONFIG, so nobody has to edit this file.
  if (window.ERN_CONFIG) for (var k in window.ERN_CONFIG) if (window.ERN_CONFIG[k]) KLAVIYO[k] = window.ERN_CONFIG[k];
  KLAVIYO.waitlistList = KLAVIYO.waitlistList || KLAVIYO.planList;
  KLAVIYO.resultsList = KLAVIYO.resultsList || KLAVIYO.planList;

  // How a sign-up reaches Klaviyo (23 Oct, after iPhone Safari blocked
  // klaviyo.com outright: "Load failed" in normal and private tabs):
  //   1. our relay (a Cloudflare Worker, URL in the theme settings): the
  //      phone never contacts klaviyo.com; the Worker calls Klaviyo's server
  //      API with a private key, saves the plan, then subscribes to the list
  //   2. if the relay can't be reached: Klaviyo's form endpoint directly
  //      (a plain form post; works on desktop)
  //   3. if both fail: keep the sign-up on the phone and send it on their
  //      next visit, and report the failure to the relay so we can count it
  // Single opt-in list, so joining it starts the welcome flow.
  function wait(ms){ return new Promise(function(r){ setTimeout(r, ms); }); }
  function honeypot(){ var h = document.querySelector('.ern input[name="ern_hp_field"]'); return h ? h.value : ''; }
  function viaRelay(profile, source){
    var body = new URLSearchParams();
    body.append('email', profile.email); body.append('source', source); body.append('company', honeypot());
    var props = {}; for (var k in (profile.properties || {})) props[k] = profile.properties[k];
    if (profile.first_name) props.first_name = profile.first_name;
    body.append('props', JSON.stringify(props));
    return fetch(KLAVIYO.relay, { method: 'POST', body: body })
      .then(function(r){ return r.json().catch(function(){ return {}; }).then(function(j){ if (!r.ok || !j.ok) throw new Error('Relay ' + r.status + ' ' + (j.error || '')); return j; }); });
  }
  function viaKlaviyo(listId, profile, source){
    var body = new URLSearchParams();
    body.append('g', listId); body.append('email', profile.email); body.append('$source', source);
    var props = profile.properties || {}, keys = [];
    if (profile.first_name) { body.append('$first_name', profile.first_name); keys.push('$first_name'); }
    for (var k in props) { if (props[k] === '' || props[k] == null) continue; body.append(k, String(props[k])); keys.push(k); }
    body.append('signup_source', source); keys.push('signup_source');
    body.append('$fields', keys.join(','));
    return fetch('https://a.klaviyo.com/ajax/subscriptions/subscribe', { method: 'POST', body: body })
      .then(function(r){ return r.json(); })
      .then(function(j){ if (!j || !j.success) throw new Error('Klaviyo: ' + ((j && j.errors) || []).join(' ')); return j; });
  }
  function send(listId, profile, source){
    var first = KLAVIYO.relay ? viaRelay(profile, source) : Promise.reject(new Error('no relay set'));
    return first.catch(function(e1){
      if (window.console) console.warn(e1);
      return viaKlaviyo(listId, profile, source).catch(function(e2){
        if (window.console) console.warn(e2);
        return wait(1500).then(function(){ return KLAVIYO.relay ? viaRelay(profile, source) : viaKlaviyo(listId, profile, source); })
          .catch(function(e3){ throw new Error((KLAVIYO.relay ? e1.message + ' / ' : '') + e2.message); });
      });
    });
  }
  // sign-ups that couldn't be sent wait on the phone for the next visit
  var QKEY = 'ern_pending_signups';
  function queue(){ try { return JSON.parse(localStorage.getItem(QKEY) || '[]'); } catch (e) { return []; } }
  function saveQueue(q){ try { if (q.length) localStorage.setItem(QKEY, JSON.stringify(q.slice(-5))); else localStorage.removeItem(QKEY); } catch (e) {} }
  function report(reason, source){
    if (!KLAVIYO.relay || !navigator.sendBeacon) return;
    var ua = navigator.userAgent, app = /Instagram/.test(ua) ? 'Instagram app' : /musical_ly|TikTok|BytedanceWebview/i.test(ua) ? 'TikTok app' : /FBAN|FBAV/.test(ua) ? 'Facebook app' : /CriOS/.test(ua) ? 'Chrome iPhone' : /iPhone|iPad/.test(ua) ? 'Safari iPhone' : /Android/.test(ua) ? 'Android' : 'Desktop';
    var b = new URLSearchParams(); b.append('reason', reason); b.append('app', app); b.append('source', source);
    try { navigator.sendBeacon(KLAVIYO.relay.replace(/\/?$/, '/log'), b); } catch (e) {}
  }
  function subscribe(which, profile, source){
    var listId = KLAVIYO[which];
    if (!listId) {
      if (window.console) console.warn('ERN: no Klaviyo list ID for ' + which + ', nothing was saved (preview mode).');
      return wait(500);
    }
    return send(listId, profile, source).catch(function(e){
      var q = queue(); q.push({ which: which, profile: profile, source: source, at: Date.now() }); saveQueue(q);
      report(String(e.message || e), source);
      throw e;
    });
  }
  function flushQueue(){
    var q = queue(); if (!q.length) return;
    saveQueue([]);
    q.forEach(function(item){
      if (Date.now() - item.at > 14 * 864e5) return; // older than two weeks: drop
      var listId = KLAVIYO[item.which]; if (!listId) return;
      send(listId, item.profile, item.source + ' (sent on return visit)').catch(function(){ var r = queue(); r.push(item); saveQueue(r); });
    });
  }
  // someone who has just signed up: same call, they're already on the list
  // so no second welcome email goes out
  function update(email, properties, source){ return subscribe('planList', { email: email, properties: properties }, source || 'Site update'); }

  function validEmail(e){ return /^\S+@\S+\.\S+$/.test(e); }

  // one event per funnel step, to Microsoft Clarity and Google Tag Manager /
  // GA4 (dataLayer). Never to Klaviyo's site script: identifying a brand-new
  // email there at the same moment as the subscription made the two collide
  // and Klaviyo dropped the sign-up (23 Oct). The subscription is the only
  // call that tells Klaviyo who someone is. The email never goes to analytics.
  function track(name, props){
    props = props || {};
    var safe = {}; for (var k in props) if (k !== 'email') safe[k] = props[k];
    try { if (window.clarity) window.clarity('event', name); } catch (e) {}
    try { (window.dataLayer = window.dataLayer || []).push(Object.assign({ event: name }, safe)); } catch (e) {}
  }

  // fade sections in as they scroll into view
  function reveal(){
    var els = document.querySelectorAll('.ern .rv');
    if (!('IntersectionObserver' in window)) { els.forEach(function(e){ e.classList.add('in'); }); return; }
    var io = new IntersectionObserver(function(es){
      es.forEach(function(e){ if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach(function(e){ io.observe(e); });
  }

  // sticky mobile button once the main form is off screen, hidden after sign-up
  function sticky(formId, doneId){
    var stick = document.querySelector('.ern .stick'), form = document.getElementById(formId);
    if (!stick || !form || !('IntersectionObserver' in window)) return;
    new IntersectionObserver(function(es){
      var done = !document.getElementById(doneId).hidden;
      stick.classList.toggle('on', !es[0].isIntersecting && !done && window.scrollY > 200);
    }).observe(form);
  }

  document.addEventListener('DOMContentLoaded', reveal);
  document.addEventListener('DOMContentLoaded', function(){ setTimeout(flushQueue, 2000); });
  return { subscribe: subscribe, update: update, validEmail: validEmail, sticky: sticky, track: track };
})();
