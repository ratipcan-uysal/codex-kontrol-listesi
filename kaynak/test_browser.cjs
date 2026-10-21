/* Optional browser checks: Playwright + Chrome/Chromium. See DOGRULAMA.md. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const fs=require('node:fs/promises');
const path=require('node:path');
const assert=require('node:assert/strict');
const base=process.env.BASE_URL || 'http://127.0.0.1:8769/';
const out=path.resolve(process.env.EVIDENCE_DIR || 'work/browser-evidence');
const results=[];
(async()=>{
 await fs.mkdir(out,{recursive:true});
 const browser=await chromium.launch({headless:true,...(process.env.CHROME_PATH?{executablePath:process.env.CHROME_PATH}:{})});
 const context=await browser.newContext({viewport:{width:1440,height:1000},colorScheme:'light',reducedMotion:'reduce',acceptDownloads:true});
 const page=await context.newPage();
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 const check=async(name,fn)=>{try{await fn();results.push({name,status:'PASS'});}catch(e){results.push({name,status:'FAIL',error:e.message});throw e;}};
 const visible=()=>page.locator('.item:not([hidden])').count();
 const marked=()=>page.locator('.item-check:checked').count();
 const upload=async(obj)=>page.locator('#import-state').setInputFiles({name:'test.json',mimeType:'application/json',buffer:Buffer.from(JSON.stringify(obj))});
 const oldBackup={version:1,checklist:'codex-20261016',checked:['1.1','2.1']};
 try {
  await page.goto(base);await page.locator('.item').last().waitFor();
  await check('107 items and 19 sections',async()=>{assert.equal(await visible(),107);assert.equal(await page.locator('.check-section').count(),19);assert.equal(await page.locator('h1').count(),1);});
  await page.screenshot({path:path.join(out,'desktop-light.png')});
  await check('basic and advanced filters',async()=>{await page.locator('[data-level="basic"]').click();assert.equal(await visible(),25);await page.locator('[data-level="advanced"]').click();assert.equal(await visible(),82);await page.locator('#clear-filters').click();});
  await check('Turkish uppercase search',async()=>{await page.locator('#search').fill('İZİN');const upper=await page.locator('.item:not([hidden])').evaluateAll(rows=>rows.map(r=>r.dataset.item));await page.locator('#search').fill('izin');assert.deepEqual(await page.locator('.item:not([hidden])').evaluateAll(rows=>rows.map(r=>r.dataset.item)),upper);assert.ok(upper.length>0);});
  await check('section title search',async()=>{await page.locator('#search').fill('Mobil ve simülatör');assert.equal(await visible(),5);});
  await check('empty result and recovery',async()=>{await page.locator('#search').fill('xyzz-not-a-word-92834');assert.equal(await visible(),0);assert.equal(await page.locator('#empty').isVisible(),true);await page.locator('#empty-reset').click();assert.equal(await visible(),107);});
  await check('collapse search-opened details regression',async()=>{await page.locator('#search').fill('hook');assert.ok(await page.locator('.item:not([hidden]) details[open]').count()>0);assert.equal(await page.locator('#expand-all').textContent(),'Detayları kapat');await page.locator('#expand-all').click();assert.equal(await page.locator('.item:not([hidden]) details[open]').count(),0);await page.locator('#expand-all').click();assert.equal(await page.locator('.item:not([hidden]) details[open]').count(),await visible());await page.locator('#clear-filters').click();});
  await check('checkmark persists after reload',async()=>{await page.locator('#check-m-1-1').check();await page.reload();assert.equal(await page.locator('#check-m-1-1').isChecked(),true);assert.equal(await page.locator('#side-done').textContent(),'1');});
  await check('unfinished excludes checked item',async()=>{await page.locator('#unfinished').check();assert.equal(await visible(),106);assert.equal(await page.locator('#m-1-1').isVisible(),false);await page.locator('#clear-filters').click();});
  await check('quick start clears filters and focuses target',async()=>{await page.locator('#search').fill('no-results-xyzz');await page.locator('[data-jump="3.1"]').click();assert.equal(await visible(),107);assert.equal(await page.locator('#m-3-1 details').getAttribute('open'),'');assert.equal(await page.evaluate(()=>document.activeElement.closest('article')?.id),'m-3-1');});
  await check('clipboard content matches example',async()=>{await context.grantPermissions(['clipboard-read','clipboard-write'],{origin:new URL(base).origin});await page.locator('[data-copy="3.1"]').click();assert.equal(await page.evaluate(()=>navigator.clipboard.readText()),await page.locator('#m-3-1 code').textContent());});
  let backup;
  await check('JSON export contains selected stable ID',async()=>{const wait=page.waitForEvent('download');await page.locator('#export-state').click();const download=await wait;const savePath=path.join(out,'export.json');await download.saveAs(savePath);backup=JSON.parse(await fs.readFile(savePath,'utf8'));assert.deepEqual(backup.checked,['1.1']);assert.equal(backup.checklist,'codex-20261016');});
  await check('reset cancellation keeps data',async()=>{page.once('dialog',d=>d.dismiss());await page.locator('#reset-state').click();assert.equal(await marked(),1);});
  await check('confirmed reset clears data',async()=>{page.once('dialog',d=>d.accept());await page.locator('#reset-state').click();assert.equal(await marked(),0);});
  await check('export-import round trip',async()=>{await upload(backup);await page.waitForFunction(()=>document.querySelectorAll('.item-check:checked').length===1);assert.equal(await page.locator('#check-m-1-1').isChecked(),true);});
  await check('import cancellation preserves previous marks',async()=>{page.once('dialog',d=>d.dismiss());await upload(oldBackup);await page.waitForFunction(()=>document.getElementById('import-status').textContent.includes('iptal'));assert.equal(await marked(),1);});
  await check('legacy backup imports after confirmation',async()=>{page.once('dialog',d=>d.accept());await upload(oldBackup);await page.waitForFunction(()=>document.querySelectorAll('.item-check:checked').length===2);assert.equal(await page.locator('#check-m-2-1').isChecked(),true);});
  await check('unknown ID rejected atomically',async()=>{await upload({...oldBackup,checked:['1.2','999.1']});await page.waitForFunction(()=>document.getElementById('import-status').textContent.startsWith('Yüklenemedi'));assert.equal(await marked(),2);assert.equal(await page.locator('#check-m-1-1').isChecked(),true);});
  await check('null import rejected safely',async()=>{await upload(null);await page.waitForFunction(()=>document.getElementById('import-status').textContent.startsWith('Yüklenemedi'));assert.equal(await marked(),2);});
  await check('oversize backup rejected safely',async()=>{await page.locator('#import-state').setInputFiles({name:'large.json',mimeType:'application/json',buffer:Buffer.from(' '.repeat(100001))});await page.waitForFunction(()=>document.getElementById('import-status').textContent.includes('büyük'));assert.equal(await marked(),2);});
  await check('item deep link opens requested detail',async()=>{await page.goto(base+'#m-8-6');await page.waitForFunction(()=>document.querySelector('#m-8-6 details').open);assert.equal(await page.locator('#m-8-6 details').getAttribute('open'),'');assert.equal(await page.evaluate(()=>document.activeElement.closest('article')?.id),'m-8-6');});
  await check('desktop dark layout',async()=>{await page.emulateMedia({colorScheme:'dark'});await page.goto(base);assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);await page.screenshot({path:path.join(out,'desktop-dark.png')});});
  for(const width of [390,320]){
   await check('mobile '+width+' layout and navigation',async()=>{await page.setViewportSize({width,height:844});await page.emulateMedia({colorScheme:'light'});await page.goto(base);assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);assert.equal(await page.locator('#mobile-nav').isVisible(),true);if(width===390)await page.screenshot({path:path.join(out,'mobile-light.png')});await page.locator('#mobile-nav').selectOption('8');assert.equal(await page.locator('#section-8').isVisible(),true);await page.locator('#m-8-6 summary').click();assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);if(width===390){await page.locator('#m-8-6').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,'mobile-hook.png')});}});
  }
  await check('all rendered external source links use HTTPS',async()=>{const hrefs=await page.locator('.item-ref a').evaluateAll(as=>as.map(a=>a.href));assert.equal(hrefs.length,107);assert.ok(hrefs.every(h=>h.startsWith('https://')));});
  await check('Markdown download is available',async()=>{const response=await context.request.get(new URL('codex-kontrol-listesi.md',base).href);assert.equal(response.status(),200);assert.ok((await response.text()).includes('107 madde'));});
  await check('no JavaScript runtime errors',async()=>assert.deepEqual(errors,[]));
  await check('storage failure leaves usable checklist',async()=>{const c=await browser.newContext();await c.addInitScript(()=>{Object.defineProperty(Storage.prototype,'getItem',{value(){throw new Error('blocked');}});Object.defineProperty(Storage.prototype,'setItem',{value(){throw new Error('blocked');}});});const p=await c.newPage();await p.goto(base);await p.locator('#check-m-1-1').check();assert.equal(await p.locator('#side-done').textContent(),'1');assert.ok((await p.locator('#storage-note').textContent()).includes('kapalı'));await c.close();});
  await check('JavaScript disabled offers full Markdown fallback',async()=>{const c=await browser.newContext({javaScriptEnabled:false});const p=await c.newPage();await p.goto(base);assert.equal(await p.locator('noscript a').isVisible(),true);await c.close();});
 } finally {
  await fs.writeFile(path.join(out,'browser-results.json'),JSON.stringify({base,browser:await browser.version(),results},null,2));
  await browser.close();
  console.log(JSON.stringify(results,null,2));
 }
})().catch(e=>{console.error(e);process.exitCode=1;});
