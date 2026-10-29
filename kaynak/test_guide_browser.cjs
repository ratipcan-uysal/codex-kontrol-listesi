/* Optional integration checks for guide and legacy-checklist navigation. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const fs=require('node:fs/promises');
const path=require('node:path');
const assert=require('node:assert/strict');
const base=process.env.BASE_URL || 'http://127.0.0.1:8769/';
const out=path.resolve(process.env.EVIDENCE_DIR || 'work/guide-browser');
(async()=>{
 await fs.mkdir(out,{recursive:true});
 const results=[],errors=[];
 const browser=await chromium.launch({headless:true,...(process.env.CHROME_PATH?{executablePath:process.env.CHROME_PATH}:{})});
 const context=await browser.newContext({viewport:{width:1440,height:1000},colorScheme:'light',reducedMotion:'reduce'});
 const page=await context.newPage();page.on('pageerror',e=>errors.push(e.message));
 const check=async(name,fn)=>{try{await fn();results.push({name,status:'PASS'});}catch(e){results.push({name,status:'FAIL',error:e.message});throw e;}};
 try{
  await page.goto(base);
  await check('checklist entry opens guide',async()=>{await page.getByRole('link',{name:'Ana rehberi aç →'}).click();await page.waitForURL('**/rehber/index.html');assert.equal(await page.locator('h1').textContent(),'Codex’i Derinlemesine Kullanma Rehberi');});
  await page.screenshot({path:path.join(out,'guide-desktop-light.png')});
  await check('complete index has 18 ordered chapters',async()=>{assert.equal(await page.locator('.prose > ol > li').count(),18);assert.equal(await page.locator('.prose > ul > li').count(),9);});
  await check('sequential reading and current navigation',async()=>{await page.locator('a[rel="next"]').click();await page.waitForURL('**/01-olanaklar.html');assert.equal(await page.locator('[aria-current="page"]').count(),1);await page.locator('a[rel="next"]').click();await page.waitForURL('**/02-uygulama.html');assert.ok((await page.locator('h1').textContent()).startsWith('2.'));await page.locator('a[rel="prev"]').click();await page.waitForURL('**/01-olanaklar.html');});
  await check('chapter contents jump reaches heading',async()=>{await page.locator('.page-toc summary').click();const link=page.locator('.page-toc a').first();const hash=await link.getAttribute('href');await link.click();assert.ok(page.url().endsWith(hash));assert.equal(await page.locator(hash).count(),1);});
  await check('all 107 checklist rows link to their mapped chapter',async()=>{await page.goto(base);assert.equal(await page.locator('.guide-link a').count(),107);await page.locator('#m-1-1 summary').click();await page.locator('#m-1-1 .guide-link a').click();await page.waitForURL('**/11-talimatlar.html');});
  await check('chapter returns to original checklist anchor',async()=>{await page.locator('.prose a[href="../index.html#m-1-1"]').click();await page.waitForFunction(()=>document.querySelector('#m-1-1 details')?.open);assert.equal(await page.evaluate(()=>document.activeElement.closest('article')?.id),'m-1-1');});
  await check('guide navigation preserves saved checkmarks',async()=>{await page.locator('#check-m-1-1').check();await page.locator('#m-1-1 .guide-link a').click();await page.getByRole('link',{name:'107 madde ↗'}).click();await page.waitForSelector('#check-m-1-1');assert.equal(await page.locator('#check-m-1-1').isChecked(),true);});
  await check('all guide pages return successful response with one heading',async()=>{await page.goto(base+'rehber/index.html');const paths=await page.locator('.sidebar nav a').evaluateAll(a=>a.map(x=>x.getAttribute('href')));for(const p of paths){const response=await page.goto(base+'rehber/'+p);assert.equal(response.status(),200,p);assert.equal(await page.locator('h1').count(),1,p);assert.ok((await page.locator('.prose').textContent()).length>1000,p);}});
  await page.goto(base+'rehber/komutlar.html');
  await page.screenshot({path:path.join(out,'guide-commands-desktop.png')});
  await check('28 desktop commands and goal surface distinction',async()=>{assert.equal(await page.locator('table').first().locator('tbody tr').count(),28);assert.ok((await page.locator('.prose').textContent()).includes('düğmeleri tarif ediyor'));});
  for(const width of [390,320]){
   await check('mobile '+width+' has readable scrolling tables without page overflow',async()=>{await page.setViewportSize({width,height:844});await page.goto(base+'rehber/komutlar.html');assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);assert.equal(await page.locator('.sidebar').isVisible(),false);assert.equal(await page.locator('.table-scroll').first().getAttribute('tabindex'),'0');assert.equal(await page.locator('.table-hint').first().isVisible(),true);assert.equal(await page.locator('table code').first().evaluate(e=>getComputedStyle(e).whiteSpace),'nowrap');await page.locator('.table-scroll').first().focus();await page.keyboard.press('ArrowRight');assert.ok(await page.locator('.table-scroll').first().evaluate(e=>e.scrollWidth>e.clientWidth));});
   await page.screenshot({path:path.join(out,'guide-commands-mobile-'+width+'.png')});
   await page.evaluate(()=>window.scrollTo(0,0));await page.screenshot({path:path.join(out,'guide-commands-mobile-top-'+width+'.png')});
  }
  await page.setViewportSize({width:1440,height:1000});await page.emulateMedia({colorScheme:'dark'});await page.goto(base+'rehber/05-yonetmek.html');
  await check('dark chapter layout has no horizontal overflow',async()=>{assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);});
  await page.screenshot({path:path.join(out,'guide-chapter-dark.png')});
  const nojs=await browser.newContext({javaScriptEnabled:false});const p2=await nojs.newPage();
  await check('guide content and navigation work without JavaScript',async()=>{await p2.goto(base+'rehber/index.html');await p2.locator('.prose ol a').first().click();assert.equal(await p2.locator('h1').count(),1);assert.ok((await p2.locator('.prose').textContent()).includes('Kurgu'));});await nojs.close();
  await check('no browser JavaScript errors',async()=>{assert.deepEqual(errors,[]);});
 }finally{
  await fs.writeFile(path.join(out,'results.json'),JSON.stringify({results,errors},null,2));
  await context.close();await browser.close();
 }
 console.log(JSON.stringify({passed:results.filter(x=>x.status==='PASS').length,failed:results.filter(x=>x.status==='FAIL').length}));
})().catch(e=>{console.error(e);process.exitCode=1;});
