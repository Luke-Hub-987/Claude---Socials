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

  // Sign-ups go to Klaviyo's form endpoint (the one its older embedded forms
  // post to): a plain form post, so the browser sends it straight away with
  // no CORS pre-check. Klaviyo's newer client API (/client/subscriptions,
  // /client/events) needs a pre-check that Klaviyo's bot filter refused in
  // real browsers once the Klaviyo pop-ups were off (23 Oct), so nothing
  // saved. This one worked every time from the same browsers. It adds the
  // email to the list (single opt-in, so the welcome flow fires) and saves
  // the plan details on the profile in the same request.
  function wait(ms){ return new Promise(function(r){ setTimeout(r, ms); }); }
  function post(listId, profile, source){
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
  function subscribe(which, profile, source){
    var listId = KLAVIYO[which];
    if (!listId) {
      if (window.console) console.warn('ERN: no Klaviyo list ID for ' + which + ', nothing was saved (preview mode).');
      return wait(500);
    }
    return post(listId, profile, source).catch(function(e){
      if (window.console) console.warn(e);
      return wait(1500).then(function(){ return post(listId, profile, source); });
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
  return { subscribe: subscribe, update: update, validEmail: validEmail, sticky: sticky, track: track };
})();
