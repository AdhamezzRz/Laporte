const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.setContent(require('fs').readFileSync(process.argv[2],'utf8'));
console.log(JSON.stringify(await p.evaluate(()=>[...document.querySelectorAll('path')].map(e=>{const b=e.getBBox();return [e.id,+b.x.toFixed(1),+b.y.toFixed(1),+b.width.toFixed(1),+b.height.toFixed(1)]}))));await b.close()})();
