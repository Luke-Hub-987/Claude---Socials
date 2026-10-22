/* ERN pace plan engine (21 Oct 2026).
   The method from the pacing videos, as code:
   - Watch pace for 0-10K: the 5-second band that contains goal pace.
     A GPS watch reads about 1% long in a race, so this runs a few seconds a K
     behind goal on real distance: behind at 10K on purpose.
   - 10-40K: the band that brings you home about 2 minutes under goal
     (with room for a watch reading 1.5% long), as small a pick-up as that allows. Last 2K: 10 s/K quicker again.
   - Goals of 4:30 and slower walk every drink station (about 15 s each,
     2 per 10K); the walks are inside the times.
   - Sign times = band centre x 10.1 km (the watch's 1%), plus walks.
   - Gels: 30g at 20 minutes, then every 30, none in the last 20 minutes,
     carry one spare.
   The 4 goals already published in videos return the published numbers. */
(function (root) {
  var PUBLISHED = {
    12600: { signs: ['50:00', '1:39', '2:29', '3:18'], bands: [[295, 300], [290, 295], [280, 285]], finish: '3:28', carry: 7 },
    13500: { signs: ['54:00', '1:46', '2:39', '3:32'], bands: [[320, 320], [313, 313], [303, 303]], finish: '3:43', carry: 8 },
    14399: { signs: ['57:30', '1:54', '2:50', '3:47'], bands: [[342, 342], [335, 335], [325, 325]], finish: '3:59', carry: 8 },
    16200: { signs: ['1:05', '2:08', '3:11', '4:14'], bands: [[380, 385], [370, 375], [360, 365]], finish: '4:28', carry: 9, walk: true }
  };
  var MILE = 1.609344;

  function mmss(s) { s = Math.round(s); return Math.floor(s / 60) + ':' + ('0' + s % 60).slice(-2); }
  function hmm(s) { s = Math.round(s / 60); return Math.floor(s / 60) + ':' + ('0' + s % 60).slice(-2); }
  function signTime(s) { return s < 3600 ? mmss(Math.round(s / 30) * 30) : hmm(s); }
  function r5(x) { return Math.round(x / 5) * 5; }
  function band(b, unit) {
    var lo = unit === 'mi' ? r5(b[0] * MILE) : b[0], hi = unit === 'mi' ? r5(b[1] * MILE) : b[1];
    return lo === hi ? mmss(lo) : mmss(lo) + ' to ' + mmss(hi);
  }
  function gelTimes(finishSec) {
    var out = [];
    for (var t = 20 * 60; t <= finishSec - 20 * 60; t += 30 * 60) out.push(hmm(t));
    return out;
  }

  // goal: seconds, e.g. 3:40 -> 13200
  function build(goal) {
    var pub = PUBLISHED[goal === 14400 ? 14399 : goal], walk = goal >= 16200, b, signs, finishSec;
    if (pub) {
      b = pub.bands; signs = pub.signs;
      var p = pub.finish.split(':'); finishSec = (+p[0] * 60 + +p[1]) * 60;
    } else {
      // Pick the bands so the plan finishes about 2 minutes under goal
      // (never less than the 1.5%-watch margin), like the published plans.
      var G = goal / 42.195, lo = 5 * Math.floor(G / 5), w = walk ? 30 : 0, best = null;
      var min = goal * 0.005 + 15; // covers a watch reading 1.5% long
      [lo + 2.5, lo + 7.5].forEach(function (c1) {
        for (var c2 = c1 - 5; c2 >= c1 - 20; c2 -= 5) {
          var F = c1 * 10.1 + c2 * 30.3 + (c2 - 10) * 2.195 * 1.01 + w * 4, slack = goal - F;
          var cand = { c1: c1, c2: c2, F: F, slack: slack, ok: slack >= min };
          // safe first; then the smallest pick-up after 10K; then closest to 2 minutes
          var jump = c1 - c2, bj = best && best.c1 - best.c2;
          if (!best || (cand.ok && !best.ok) ||
              (cand.ok && best.ok && (jump < bj || (jump === bj && Math.abs(slack - 120) < Math.abs(best.slack - 120)))) ||
              (!cand.ok && !best.ok && slack > best.slack)) best = cand;
        }
      });
      var c = [best.c1, best.c2, best.c2 - 10];
      b = c.map(function (x) { return [x - 2.5, x + 2.5]; });
      var t = 0, raw = [];
      t += c[0] * 10.1 + w; raw.push(t);
      for (var i = 0; i < 3; i++) { t += c[1] * 10.1 + w; raw.push(t); }
      finishSec = t + c[2] * 2.195 * 1.01;
      signs = raw.map(signTime);
    }
    var gels = gelTimes(finishSec);
    return {
      goal: goal, walk: walk, signs: signs,
      finish: hmm(finishSec), finishSec: finishSec,
      stages: [
        { name: '0 to 10K', km: band(b[0], 'km'), mi: band(b[0], 'mi'), talk: 'All 10 words in one breath, normal voice' },
        { name: '10 to 40K', km: band(b[1], 'km'), mi: band(b[1], 'mi'), talk: '10 words a bit breathy by 20K, about 5 by 30K, 2 or 3 by 40K' },
        { name: 'Last 2K', km: band(b[2], 'km'), mi: band(b[2], 'mi'), talk: 'Elbows back. Whatever you have left' }
      ],
      gels: gels, carry: pub ? pub.carry : gels.length + 1
    };
  }

  function parseGoal(str) {
    var m = /^(\d):(\d\d)/.exec(str || ''); if (!m) return null;
    if (/sub-?4/i.test(str)) return 14399; // "3:59 (sub-4)" -> the published sub-4 plan
    return (+m[1] * 60 + +m[2]) * 60;
  }

    // how a goal reads on screen: 14399 and 14400 are both the sub-4 plan
  function label(goal) { return goal >= 14399 && goal <= 14400 ? 'Sub-4' : hmm(goal); }

  root.ERNPlan = { build: build, parseGoal: parseGoal, hmm: hmm, label: label };
  if (typeof module !== 'undefined') module.exports = root.ERNPlan;
})(this);
