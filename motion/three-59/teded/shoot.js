// node motion/three-59/teded/shoot.js [ids...]  -> PNG stills at 1080x1920
const path=require('path');const {chromium}=require('/opt/node-tools/node_modules/playwright');
const ids=process.argv.slice(2).length?process.argv.slice(2):['sheet','1','2','3'];
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
 for(const id of ids){await p.goto('file://'+path.resolve(__dirname,'scenes.html')+'?s='+id);await p.evaluate(()=>document.fonts.ready);
  await p.waitForTimeout(150);await p.screenshot({path:path.resolve(__dirname,'still-'+id+'.png')});console.log('ok',id)}
 await b.close()})();
