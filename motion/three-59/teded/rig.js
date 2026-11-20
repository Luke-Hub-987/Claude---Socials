// Shared drawing kit for the 3:59 TED-Ed cutaways (P229): the runner rig, tokens, clock, lettering.

const W=1080,H=1920,D=Math.PI/180;
const C={paper:'#f3ead8',paper2:'#ebdfc8',ink:'#2a2420',blue:'#1f7ae0',blueD:'#1559a8',gold:'#f5b52e',red:'#d9473f',
  mute:'#9fb0c6',sand:'#c9bfae',road:'#ddd0b8',roadD:'#cbbd a2'.replace(' ',''),grass:'#a9c48a',grassD:'#8fb071',tree:'#6f9b5a',treeD:'#5a8449'};
const SK=['#f1c7a3','#d8a07a','#a86f4c','#7a4a2e','#e9b892','#c98b62'];
const HR=['#2a1d15','#6b4528','#c99a5b','#1a1a1a','#8a3b1f','#3b2a20'];
function shade(hex,k){const n=parseInt(hex.slice(1),16),f=v=>Math.max(0,Math.min(255,Math.round(v*(1-k))));
  return '#'+[n>>16&255,n>>8&255,n&255].map(v=>f(v).toString(16).padStart(2,'0')).join('')}
const P=(x,y)=>({x,y}), add=(a,b)=>P(a.x+b.x,a.y+b.y), dir=(deg,l)=>P(l*Math.sin(deg*D),l*Math.cos(deg*D));
const f1=v=>v.toFixed(1);

/* a tapered limb: a polygon between two joints with round ends */
function limb(a,b,w1,w2,col){const dx=b.x-a.x,dy=b.y-a.y,L=Math.hypot(dx,dy)||1,nx=-dy/L,ny=dx/L;
  return `<path d="M${f1(a.x+nx*w1/2)} ${f1(a.y+ny*w1/2)}L${f1(b.x+nx*w2/2)} ${f1(b.y+ny*w2/2)}L${f1(b.x-nx*w2/2)} ${f1(b.y-ny*w2/2)}L${f1(a.x-nx*w1/2)} ${f1(a.y-ny*w1/2)}Z" fill="${col}"/>`+
    `<circle cx="${f1(a.x)}" cy="${f1(a.y)}" r="${w1/2}" fill="${col}"/><circle cx="${f1(b.x)}" cy="${f1(b.y)}" r="${w2/2}" fill="${col}"/>`}

/* a shorts leg: round at the hip, a straight hem at the thigh */
function sleeve(a,b,w1,w2,col){const dx=b.x-a.x,dy=b.y-a.y,L=Math.hypot(dx,dy)||1,nx=-dy/L,ny=dx/L;
  return `<path d="M${f1(a.x+nx*w1/2)} ${f1(a.y+ny*w1/2)}L${f1(b.x+nx*w2/2)} ${f1(b.y+ny*w2/2)}L${f1(b.x-nx*w2/2)} ${f1(b.y-ny*w2/2)}L${f1(a.x-nx*w1/2)} ${f1(a.y-ny*w1/2)}Z" fill="${col}"/><circle cx="${f1(a.x)}" cy="${f1(a.y)}" r="${w1/2}" fill="${col}"/>`}
/* poses: hip/knee per leg, shoulder/elbow per arm (degrees; + is forward), lean of the torso, head tilt */
const POSE={
  run:   {nH:30,nK:22,fH:-26,fK:92,nS:-38,nE:128,fS:32,fE:88,lean:9,tilt:0},
  sprint:{nH:42,nK:30,fH:-34,fK:110,nS:-55,nE:135,fS:48,fE:80,lean:16,tilt:-4},
  trudge:{nH:16,nK:14,fH:-14,fK:40,nS:-14,nE:70,fS:12,fE:60,lean:15,tilt:14},
  watch: {nH:26,nK:20,fH:-22,fK:80,nS:58,nE:100,fS:-30,fE:110,lean:8,tilt:10},
  stand: {nH:4,nK:2,fH:-4,fK:2,nS:8,nE:14,fS:-6,fE:12,lean:1,tilt:0},
};
/* o: x, y (ground), s (scale), f (1 right, -1 left), pose, look {skin,hair,style,top,shorts,shoe,brow,eye,mouth,bib} */
function runner(o){
  const p=Object.assign({},typeof o.pose==='object'?o.pose:POSE[o.pose||'run'],o.adj||{});
  const L=Object.assign({skin:'#f6d6bf',hair:'#5a3a24',style:'short',top:C.blue,shorts:C.ink,shoe:C.gold,brow:'calm',eye:[0,0],mouth:'line',bib:true},o.look||{});
  const skD=shade(L.skin,.16), topD=shade(L.top,.18), shD=shade(L.shorts,.25);
  const hip=P(0,-196), sh=add(hip,dir(180-p.lean,128)); // torso goes up
  const legPts=(a,k)=>{const kn=add(hip,dir(a,98)),an=add(kn,dir(a-k,96));return{kn,an,toe:add(an,dir(a-k+90,40))}};
  const armPts=(s,e)=>{const el=add(sh,dir(s,70)),hd=add(el,dir(s+e,60));return{el,hd}};
  const nl=legPts(p.nH,p.nK), fl=legPts(p.fH,p.fK), na=armPts(p.nS,p.nE), fa=armPts(p.fS,p.fE);
  const shoe=(lg,col)=>{const a=Math.atan2(lg.toe.y-lg.an.y,lg.toe.x-lg.an.x)/D;
    const sole=col==='#ffffff'||col===shade('#ffffff',.18)?'#b9b2a6':'#fbf6ee';
    return `<g transform="translate(${f1(lg.an.x)} ${f1(lg.an.y)}) rotate(${f1(a)})"><path d="M-16 6 C-18 -12 2 -17 13 -13 C26 -9 40 -5 50 1 C56 5 54 12 47 12 L-16 12 Z" fill="${col}"/><rect x="-18" y="8" width="72" height="10" rx="5" fill="${sole}"/><path d="M8 -6 L22 2" stroke="${shade(col,.25)}" stroke-width="4" stroke-linecap="round"/></g>`};
  const thigh=(lg,skin,sh_)=>limb(hip,lg.kn,46,31,skin)+sleeve(hip,add(hip,P((lg.kn.x-hip.x)*.46,(lg.kn.y-hip.y)*.46)),50,48,sh_);
  const calf=(lg,skin)=>{const dx=lg.an.x-lg.kn.x,dy=lg.an.y-lg.kn.y,l=Math.hypot(dx,dy),nx=-dy/l,ny=dx/l,m=P(lg.kn.x+dx*.33+nx*5,lg.kn.y+dy*.33+ny*5);return limb(lg.kn,m,31,34,skin)+limb(m,lg.an,34,17,skin)};
  let g='';
  // shadow
  g+=`<ellipse cx="10" cy="4" rx="${90}" ry="12" fill="${C.ink}" opacity=".10"/>`;
  // far arm, far leg
  g+=limb(sh,fa.el,25,19,skD)+limb(fa.el,fa.hd,19,15,skD)+`<circle cx="${f1(fa.hd.x)}" cy="${f1(fa.hd.y)}" r="13" fill="${skD}"/>`;
  g+=calf(fl,skD)+thigh(fl,skD,shD)+shoe(fl,shade(L.shoe,.18));
  // torso (singlet) and shorts
  const tr=`translate(${f1(hip.x)} ${f1(hip.y)}) rotate(${f1(p.lean)})`;
  g+=`<g transform="${tr}"><path d="M-25 8 C-31 -40 -35 -92 -27 -122 C-21 -138 14 -140 25 -125 C36 -109 35 -80 28 -62 C23 -42 27 -14 25 8 Z" fill="${L.top}"/>
    <path d="M-25 8 C-31 -40 -35 -92 -27 -122 C-22 -131 -14 -134 -8 -134 C-16 -100 -16 -40 -10 8 Z" fill="${topD}"/>
    ${L.bib?`<g transform="translate(4 -72) rotate(-4)"><rect x="-4" y="-18" width="34" height="32" rx="4" fill="#fff"/><rect x="2" y="-10" width="22" height="5" rx="2" fill="${C.sand}"/><rect x="2" y="0" width="14" height="5" rx="2" fill="${C.sand}"/></g>`:''}
    <rect x="-31" y="-6" width="60" height="30" rx="12" fill="${L.shorts}"/><rect x="-31" y="-6" width="60" height="7" rx="3" fill="${shade(L.shorts,.3)}"/></g>`;
  // near leg
  g+=calf(nl,L.skin)+thigh(nl,L.skin,L.shorts)+shoe(nl,L.shoe);
  // neck and head
  const hc=add(sh,dir(180-p.lean+p.tilt*.3,52)), ang=p.lean*.5+p.tilt;
  g+=limb(sh,add(sh,dir(180-p.lean,26)),20,18,skD);
  let hd='';
  if(L.style==='pony')hd+=`<path d="M-30 -14 C-62 -10 -70 18 -58 40 C-50 24 -44 10 -26 6Z" fill="${L.hair}"/>`;
  if(L.style==='bun')hd+=`<circle cx="-30" cy="-30" r="15" fill="${L.hair}"/>`;
  hd+=`<ellipse cx="0" cy="0" rx="35" ry="39" fill="${L.skin}"/>`;
  hd+=`<path d="M33 4 L42 12 L32 16Z" fill="${L.skin}"/>`; // nose
  if(L.style==='cap')hd+=`<path d="M-36 -6 C-36 -44 30 -50 36 -14 L64 -10 C60 -4 40 -4 34 -6 Z" fill="${L.top===C.blue?C.ink:C.blue}"/>`;
  else if(L.style==='bald'){} else hd+=`<path d="M-37 6 C-42 -34 -6 -50 22 -38 C34 -32 38 -20 36 -12 C20 -22 6 -18 -6 -14 C-14 -4 -22 4 -37 6Z" fill="${L.hair}"/>`;
  hd+=`<ellipse cx="-6" cy="4" rx="8" ry="11" fill="${skD}"/><circle cx="16" cy="12" r="8" fill="#e5826f" opacity=".28"/>`; // ear, cheek
  const [ex,ey]=L.eye; hd+=`<ellipse cx="${18+ex}" cy="${-3+ey}" rx="4.6" ry="5.6" fill="${C.ink}"/>`;
  const brows={calm:'M10 -16 L28 -17',up:'M10 -22 L28 -26',tired:'M10 -14 L28 -20',set:'M10 -20 L28 -14'};
  hd+=`<path d="${brows[L.brow]}" stroke="${shade(L.hair,0)}" stroke-width="5" stroke-linecap="round" fill="none"/>`;
  const mouths={line:'M22 20 L32 20',open:'M22 18 Q28 28 34 18',puff:'M24 20 Q30 15 34 20',grit:'M20 19 L34 19'};
  hd+=`<path d="${mouths[L.mouth]}" stroke="${shade(L.skin,.5)}" stroke-width="4" stroke-linecap="round" fill="${L.mouth==='open'?shade(L.skin,.5):'none'}"/>`;
  if(L.mouth==='puff')hd+=`<circle cx="30" cy="10" r="0" />`;
  if(L.sweat)hd+=`<path d="M-2 -40 q-7 12 0 16 q7 -4 0 -16Z" fill="#8cc4ee"/><path d="M44 -26 q-6 10 0 13 q6 -3 0 -13Z" fill="#8cc4ee"/>`;
  g+=`<g transform="translate(${f1(hc.x)} ${f1(hc.y)}) rotate(${f1(ang)})">${hd}</g>`;
  // near arm (with a watch when looking at it)
  g+=limb(sh,na.el,25,19,L.skin)+limb(na.el,na.hd,19,15,L.skin)+`<circle cx="${f1(na.hd.x)}" cy="${f1(na.hd.y)}" r="13" fill="${L.skin}"/>`;
  if(o.watch){const w=add(na.el,P((na.hd.x-na.el.x)*.72,(na.hd.y-na.el.y)*.72));g+=`<circle cx="${f1(w.x)}" cy="${f1(w.y)}" r="11" fill="${C.ink}"/><circle cx="${f1(w.x)}" cy="${f1(w.y)}" r="6" fill="${C.gold}"/>`}
  const out={g:`<g transform="translate(${o.x} ${o.y}) scale(${(o.f||1)*o.s} ${o.s})">${g}</g>`,
    hand:P(o.x+(o.f||1)*o.s*na.hd.x,o.y+o.s*na.hd.y), head:P(o.x+(o.f||1)*o.s*hc.x,o.y+o.s*hc.y)};
  return out;
}

/* a finisher token for the bunching chart: head and shoulders */
function token(x,y,s,top,skin,hair){return `<g transform="translate(${x} ${y}) scale(${s})">
  <path d="M-40 44 C-40 8 -24 -4 0 -4 C24 -4 40 8 40 44 Z" fill="${top}"/><path d="M-12 -2 L0 14 L12 -2Z" fill="${shade(top,.2)}"/>
  <circle cx="0" cy="-30" r="22" fill="${skin}"/><path d="M-23 -30 C-24 -54 18 -62 23 -36 C12 -44 -6 -44 -23 -30Z" fill="${hair}"/></g>`}

/* paper, grain, lettering */
const defs=`<defs><filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="7"/><feColorMatrix values="0 0 0 0 .16  0 0 0 0 .13  0 0 0 0 .1  0 0 0 .07 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
<radialGradient id="vig" cx="50%" cy="45%" r="75%"><stop offset="60%" stop-color="#000" stop-opacity="0"/><stop offset="100%" stop-color="#5a4630" stop-opacity=".16"/></radialGradient></defs>`;
const paper=()=>`<rect width="${W}" height="${H}" fill="${C.paper}"/>`;
const finish=()=>`<rect width="${W}" height="${H}" fill="#fff" filter="url(#grain)"/><rect width="${W}" height="${H}" fill="url(#vig)"/>`;
const hand=(x,y,t,size,col,anchor='middle',rot=0)=>`<text x="${x}" y="${y}" font-family="Hand" font-weight="700" font-size="${size}" fill="${col||C.ink}" text-anchor="${anchor}" transform="rotate(${rot} ${x} ${y})">${t}</text>`;
const num=(x,y,t,size,col,anchor='middle')=>`<text x="${x}" y="${y}" font-family="BC" font-weight="800" font-size="${size}" fill="${col||C.ink}" text-anchor="${anchor}" letter-spacing="1">${t}</text>`;
function clock(cx,cy,w,t,col){const h=w*.36;return `<g><rect x="${cx-w/2+8}" y="${cy-h/2+10}" width="${w}" height="${h}" rx="${h*.18}" fill="${C.ink}" opacity=".18"/>
  <rect x="${cx-w/2}" y="${cy-h/2}" width="${w}" height="${h}" rx="${h*.18}" fill="${C.ink}"/>
  <rect x="${cx-w/2+14}" y="${cy-h/2+14}" width="${w-28}" height="${h-28}" rx="${h*.12}" fill="#15110e"/>
  ${num(cx,cy+h*.27,t,h*.74,col||'#f6efe2')}</g>`}
const speed=(x,y,n,len,col)=>Array.from({length:n},(_,i)=>`<path d="M${x} ${y+i*34} l${-len+(i%2)*60} 0" stroke="${col||C.ink}" stroke-width="7" stroke-linecap="round" opacity=".35"/>`).join('');
const arrow=(d,col)=>`<path d="${d}" stroke="${col}" stroke-width="9" fill="none" stroke-linecap="round"/>`;
function tree(x,y,s,c1,c2){return `<g transform="translate(${x} ${y}) scale(${s})"><rect x="-9" y="-90" width="18" height="90" rx="6" fill="#7a5b40"/>
  <circle cx="0" cy="-150" r="78" fill="${c1}"/><circle cx="-38" cy="-120" r="48" fill="${c1}"/><circle cx="26" cy="-176" r="40" fill="${c2}" opacity=".5"/></g>`}

