// Renders each scene of a motion file to its own 1920x1080 MP4 (30 fps).
// Usage: node motion/render.js motion/goal-gone.html <out dir> [scene numbers...]
const path=require('path'),{spawn}=require('child_process');
const {chromium}=require('/opt/node-tools/node_modules/playwright');
const [file,out,...only]=process.argv.slice(2);const FPS=30;
(async()=>{
  const browser=await chromium.launch();
  const page=await browser.newPage({viewport:{width:1920,height:1080}});
  await page.goto('file://'+path.resolve(file)+'?render=1');
  await page.evaluate(()=>document.fonts.ready);
  const scenes=await page.evaluate(()=>SCENES.map(s=>({id:s.id,dur:s.dur})));
  for(const [i,s] of scenes.entries()){
    if(only.length&&!only.includes(String(i+1)))continue;
    await page.evaluate(i=>load(i),i);
    const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate',String(FPS),'-c:v','mjpeg','-i','-',
      '-c:v','libx264','-pix_fmt','yuv420p','-crf','16','-preset','medium','-movflags','+faststart',path.join(out,s.id+'.mp4')],{stdio:['pipe','inherit','inherit']});
    const n=Math.round(s.dur*FPS);
    for(let f=0;f<n;f++){await page.evaluate(t=>frame(t),f/FPS);ff.stdin.write(await page.screenshot({type:'jpeg',quality:95}))}
    ff.stdin.end();await new Promise(r=>ff.on('close',r));console.log('done',s.id);
  }
  await browser.close();
})();
