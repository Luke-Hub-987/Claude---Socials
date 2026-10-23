/* ERN site: shared behaviour for both pages. */
window.ERN = (function(){
  // Sign-ups use Klaviyo's own embedded forms (Luke, 23 Oct: "keep it super
  // simple", the way the old site collected emails). Klaviyo's form saves the
  // email to the Email List, which starts the welcome flow. Our own code never
  // calls Klaviyo: on iPhones, custom calls to klaviyo.com were refused
  // ("Load failed", in Safari and in Instagram's browser), while Klaviyo's
  // forms carry the check Klaviyo's bot filter needs.
  // The form IDs come from the theme editor (window.ERN_CONFIG).
  var CONFIG = { klPlanForm: '', klBarForm: '' };
  if (window.ERN_CONFIG) for (var k in window.ERN_CONFIG) if (window.ERN_CONFIG[k]) CONFIG[k] = window.ERN_CONFIG[k];

  // Klaviyo fires a "klaviyoForms" event on the page when a form is
  // submitted; run cb(email) when it's the form we're waiting for
  function onKlaviyoSubmit(formId, cb){
    window.addEventListener('klaviyoForms', function(e){
      var d = e.detail || {};
      if (d.type !== 'submit') return;
      if (formId && d.formId && String(d.formId) !== String(formId)) return;
      cb(((d.metaData || {}).$email) || '');
    });
  }

  // Our own email box shows instantly; Klaviyo's form loads hidden behind it
  // (it took ~6s to appear on a phone's first visit, 23 Oct). On tap we put
  // the email into Klaviyo's form and press its button, so Klaviyo's own form
  // still does the saving. Resolves when Klaviyo says it's submitted.
  function sendViaKlaviyo(holder, email, waitMs){
    return new Promise(function(resolve, reject){
      var start = Date.now(), done = false;
      function onEvent(e){ var d = e.detail || {}; if (d.type === 'submit' && !done) { done = true; window.removeEventListener('klaviyoForms', onEvent); resolve(); } }
      window.addEventListener('klaviyoForms', onEvent);
      (function tryFill(){
        if (done) return;
        var input = holder && holder.querySelector('input[type="email"], input[name="email"]');
        var button = holder && holder.querySelector('button[type="submit"], button');
        if (input && button) {
          var setter = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
          setter.call(input, email);
          input.dispatchEvent(new Event('input', { bubbles: true }));
          input.dispatchEvent(new Event('change', { bubbles: true }));
          setTimeout(function(){ if (!done) button.click(); }, 50);
          setTimeout(function(){ if (!done) { done = true; window.removeEventListener('klaviyoForms', onEvent); reject(new Error('Klaviyo did not confirm')); } }, 8000);
          return;
        }
        if (Date.now() - start > (waitMs || 15000)) { done = true; window.removeEventListener('klaviyoForms', onEvent); reject(new Error('Klaviyo form never loaded')); return; }
        setTimeout(tryFill, 200);
      })();
    });
  }

  // if Klaviyo's form hasn't appeared after a few seconds (blocked, or no
  // form ID set yet), run cb so nobody is left with nothing
  function ifFormMissing(holder, cb, ms){
    setTimeout(function(){ if (holder && !holder.querySelector('form, input, button')) cb(); }, ms || 6000);
  }

  // one event per funnel step, to Microsoft Clarity and Google Tag Manager /
  // GA4 (dataLayer). The email never goes to analytics.
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
  return { config: CONFIG, onKlaviyoSubmit: onKlaviyoSubmit, ifFormMissing: ifFormMissing, sendViaKlaviyo: sendViaKlaviyo, sticky: sticky, track: track };
})();
