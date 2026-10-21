/* ERN site v3: shared behaviour for both pages. */
window.ERN = (function(){
  // Klaviyo: the company ID is the public site ID already on the live site.
  // Paste the two list IDs (Lists & segments > list > Settings > List ID).
  // While a list ID is empty, forms run in preview mode and send nothing.
  var KLAVIYO = { company: 'RhFsS3', planList: '', waitlistList: '' };

  function subscribe(which, profile, source){
    var listId = KLAVIYO[which];
    if (!listId) return new Promise(function(r){ setTimeout(r, 500); });
    return fetch('https://a.klaviyo.com/client/subscriptions/?company_id=' + KLAVIYO.company, {
      method: 'POST',
      headers: { 'Content-Type': 'application/vnd.api+json', 'revision': '2024-10-15' },
      body: JSON.stringify({ data: { type: 'subscription', attributes: {
        custom_source: source,
        profile: { data: { type: 'profile', attributes: profile } }
      }, relationships: { list: { data: { type: 'list', id: listId } } } } })
    }).then(function(r){ if (!r.ok) throw new Error('Klaviyo ' + r.status); });
  }

  function validEmail(e){ return /^\S+@\S+\.\S+$/.test(e); }

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
  return { subscribe: subscribe, validEmail: validEmail, sticky: sticky };
})();
