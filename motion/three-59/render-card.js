const path=require('path');const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
await p.goto('file://'+path.resolve('motion/three-59/card.html'));await p.waitForFunction(()=>document.title==='ready');await p.waitForTimeout(300);
await p.screenshot({path:'motion/three-59/three-59-clock-card-16x9.png'});await b.close()})();
