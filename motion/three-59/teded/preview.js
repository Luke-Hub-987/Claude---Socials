// node preview.js out.png "1:2.0,1:5.5,..."  -> contact sheet of frames (scene:time)
const path=require('path');const {chromium}=require('/opt/node-tools/node_modules/playwright');
const [out,list]=process.argv.slice(2);const items=list.split(',').map(x=>x.split(':').map(Number));
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
 const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+path.resolve(__dirname,'cutaways.html'));await p.evaluate(()=>document.fonts.ready);
 const files=[];for(const [s,t] of items){await p.evaluate(([s,t])=>{load(s-1);frame(t)},[s,t]);await p.waitForTimeout(30);
  const f=`/tmp/claude-0/-home-user-Claude---Socials/ac16d627-e5be-5689-9e8d-aa102c79fb45/scratchpad/pv-${s}-${t}.png`;await p.screenshot({path:f});files.push(f)}
 await b.close();if(errs.length)console.log('ERR',errs.slice(0,3));console.log(files.join('\n'))})();
