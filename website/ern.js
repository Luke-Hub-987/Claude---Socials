/* ERN site: shared behaviour for both pages. */
window.ERN = (function(){
  // Klaviyo: the company ID is the public site ID already on the live site.
  // One list for everyone (Luke, 23 Oct): Email List. The waitlist and the
  // results form use it too; what someone signed up for is saved on their
  // profile (bar_waitlist, result_time) and the sign-up source, so a segment
  // can pick them out later. While the list ID is empty, forms run in
  // preview mode and send nothing.
  var KLAVIYO = { company: 'RhFsS3', planList: '', waitlistList: '', resultsList: '' };
  // On Shopify the list IDs come from the section settings (theme editor),
  // written into window.ERN_CONFIG, so nobody has to edit this file.
  if (window.ERN_CONFIG) for (var k in window.ERN_CONFIG) if (window.ERN_CONFIG[k]) KLAVIYO[k] = window.ERN_CONFIG[k];
  KLAVIYO.waitlistList = KLAVIYO.waitlistList || KLAVIYO.planList;
  KLAVIYO.resultsList = KLAVIYO.resultsList || KLAVIYO.planList;

  function klaviyo(path, data){
    return fetch('https://a.klaviyo.com/client/' + path + '/?company_id=' + KLAVIYO.company, {
      method: 'POST', keepalive: true,
      headers: { 'Content-Type': 'application/vnd.api+json', 'revision': '2024-10-15' },
      body: JSON.stringify({ data: data })
    }).then(function(r){ if (!r.ok) throw new Error('Klaviyo ' + path + ' ' + r.status); });
  }

  // One call: the subscription carries the plan details on the profile, so
  // the person joins the list with their plan already saved and the welcome
  // email can show it. (Two calls at once for a brand-new email raced each
  // other in Klaviyo and the sign-up was lost, 23 Oct.) If Klaviyo ever
  // refuses a property, subscribe without them first, then save the details,
  // so a bad property can never cost the sign-up.
  function subscribe(which, profile, source){
    var listId = KLAVIYO[which];
    if (!listId) {
      if (window.console) console.warn('ERN: no Klaviyo list ID for ' + which + ', nothing was saved (preview mode).');
      return new Promise(function(r){ setTimeout(r, 500); });
    }
    var who = { email: profile.email }; if (profile.first_name) who.first_name = profile.first_name;
    var body = function(attrs){ return { type: 'subscription', attributes: {
      custom_source: source,
      profile: { data: { type: 'profile', attributes: attrs } }
    }, relationships: { list: { data: { type: 'list', id: listId } } } }; };
    var full = who;
    if (profile.properties) { full = { properties: profile.properties }; for (var k in who) full[k] = who[k]; }
    var wait = function(ms){ return new Promise(function(r){ setTimeout(r, ms); }); };
    // one retry after a short pause covers a dropped connection
    var once = function(attrs){ return klaviyo('subscriptions', body(attrs)).catch(function(e){
      if (window.console) console.warn(e); return wait(1500).then(function(){ return klaviyo('subscriptions', body(attrs)); }); }); };
    if (!profile.properties) return once(who);
    return once(full).catch(function(e){
      if (window.console) console.warn(e);
      return klaviyo('subscriptions', body(who)).then(function(){
        return klaviyo('profiles', { type: 'profile', attributes: { email: profile.email, properties: profile.properties } })
          .catch(function(e2){ if (window.console) console.warn(e2); });
      });
    });
  }

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
  return { subscribe: subscribe, validEmail: validEmail, sticky: sticky, track: track };
})();
