/* ERN site: shared behaviour for both pages. */
window.ERN = (function(){
  // Klaviyo: the company ID is the public site ID already on the live site.
  // The three list IDs (Lists & segments > list > Settings > List ID).
  // While a list ID is empty, forms run in preview mode and send nothing.
  var KLAVIYO = { company: 'RhFsS3', planList: '', waitlistList: '', resultsList: '' };
  // On Shopify the list IDs come from the section settings (theme editor),
  // written into window.ERN_CONFIG, so nobody has to edit this file.
  if (window.ERN_CONFIG) for (var k in window.ERN_CONFIG) if (window.ERN_CONFIG[k]) KLAVIYO[k] = window.ERN_CONFIG[k];

  function klaviyo(path, data){
    return fetch('https://a.klaviyo.com/client/' + path + '/?company_id=' + KLAVIYO.company, {
      method: 'POST',
      headers: { 'Content-Type': 'application/vnd.api+json', 'revision': '2024-10-15' },
      body: JSON.stringify({ data: data })
    }).then(function(r){ if (!r.ok) throw new Error('Klaviyo ' + path + ' ' + r.status); });
  }

  // Two calls: the subscription puts the email on the list (this starts the
  // flow), the profile call saves the plan details. Kept apart so a rejected
  // property can never stop the sign-up itself.
  function subscribe(which, profile, source){
    var listId = KLAVIYO[which];
    if (!listId) {
      if (window.console) console.warn('ERN: no Klaviyo list ID for ' + which + ', nothing was saved (preview mode).');
      return new Promise(function(r){ setTimeout(r, 500); });
    }
    var who = { email: profile.email }; if (profile.first_name) who.first_name = profile.first_name;
    var sub = klaviyo('subscriptions', { type: 'subscription', attributes: {
      custom_source: source,
      profile: { data: { type: 'profile', attributes: who } }
    }, relationships: { list: { data: { type: 'list', id: listId } } } });
    var props = profile.properties ? klaviyo('profiles', { type: 'profile', attributes: { email: profile.email, properties: profile.properties } })
      .catch(function(e){ if (window.console) console.warn(e); }) : null;
    return Promise.all([sub, props]);
  }

  function validEmail(e){ return /^\S+@\S+\.\S+$/.test(e); }

  // one event per funnel step, to whatever is installed: Microsoft Clarity,
  // Google Tag Manager / GA4 (dataLayer) and Klaviyo (once we know the email)
  function track(name, props){
    props = props || {};
    try { if (window.clarity) window.clarity('event', name); } catch (e) {}
    try { (window.dataLayer = window.dataLayer || []).push(Object.assign({ event: name }, props)); } catch (e) {}
    try { if (window.klaviyo && props.email) { window.klaviyo.push(['identify', { email: props.email }]); window.klaviyo.push(['track', name, props]); } } catch (e) {}
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
