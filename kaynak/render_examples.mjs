import fs from 'node:fs/promises';
import path from 'node:path';
import {createRequire} from 'node:module';
import {pathToFileURL} from 'node:url';
const require=createRequire(path.join(process.env.RUNTIME_NODE_MODULES,'package.json'));
const {Presentation,PresentationFile,FileBlob}=require('@oai/artifact-tool');
const sk=path.resolve(process.env.PRESENTATIONS_SKILL_DIR);
const {finalizePresentation,applyPresentationChartFont}=await import(pathToFileURL(path.join(sk,'container_tools/artifact_tool_utils.mjs')));
const dir=path.resolve(process.argv[2]), build=path.join(dir,'build');
await fs.mkdir(build,{recursive:true});
const d=JSON.parse(await fs.readFile(path.join(dir,'deck.json'),'utf8'));
await fs.mkdir(path.join(dir,'output'),{recursive:true});
const p=Presentation.create({slideSize:{width:1280,height:720}});
function text(s,value,x,y,w,h,size=28,color='#25282B',bold=false){const sh=s.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});sh.text=value;sh.text.style={typeface:'Arial',fontSize:size,color,bold};return sh;}
function base(p,n,title,tag){const s=p.slides.add();s.background.fill='#FFFFFF';text(s,tag,72,48,1100,35,18,'#62666C',true);text(s,title,72,112,1136,115,48,'#202426',true);text(s,'ATÖLYE • KURGU ÖĞRETİM ÖRNEĞİ',72,656,950,26,15,'#62666C');text(s,String(n).padStart(2,'0'),1140,652,70,30,20);s.speakerNotes.text=d.source+' Gerçek ürün fiyatları değildir.';return s;}
let s=base(p,1,'İki zorunlu koşulu karşılayan seçenek: B','ARAŞTIRMA → KARAR');
text(s,d.conditions.join('  +  '),72,266,1100,55,32);
text(s,'2.500 TL',72,366,550,100,78,'#202426',true);
text(s,'3.000 TL bütçe içinde\n500 TL pay kalıyor.',730,376,470,120,34);
text(s,d.unknown,72,545,1120,60,26,'#62666C');
s.speakerNotes.text+=' İki koşulu önce açıklayın. 500 TL farkı güvenlik payı diye kesinleştirmeyin: ek ücret henüz bilinmiyor.';
s=base(p,2,'Aynı ölçütlerle üç seçeneği karşılaştır','KARARIN DAYANAĞI');
const table=s.tables.add({rows:4,columns:3,left:72,top:260,width:1136,height:280,columnWidths:[235,220,681],values:[['Seçenek','Bedel','Kararı etkileyen fark'],...d.rows]});
table.borders.assign({style:'solid',fill:'#DFE1E3',width:1});
for(let r=0;r<4;r++){table.rows[r].height=70;for(let c=0;c<3;c++){const cell=table.getCell(r,c);cell.fill=r===0?'#25282B':r===2?'#E9EBED':'#FFFFFF';cell.text.style={typeface:'Arial',fontSize:26,color:r===0?'#FFFFFF':'#25282B',bold:r===0||r===2};}}
text(s,'Bütçe: 3.000 TL  ·  B’den sonra kalan: 500 TL',72,566,1136,40,25);
text(s,d.unknown,72,610,1136,35,22,'#62666C');
s.speakerNotes.text+=' B satırını gösterin: A ücretsiz olsa da CSV yok; C ucuz olsa da hesap gerekiyor. Slayt önce/sonra örneğinde bilgi aynı, karşılaştırma biçimi farklıdır.';
s=base(p,3,'Hangi yeni bilgi kararı değiştirir?','BİLİNMEYEN → SONRAKİ ADIM');
text(s,'01',72,270,100,55,36,'#62666C');text(s,'Ek ücret 500 TL’yi aşarsa bütçe aşılır.',190,270,1000,90,34,'#25282B',true);
text(s,'Vergi ve ödeme komisyonunu doğrula; toplam maliyeti güncelle.',190,355,990,65,26,'#62666C');
text(s,'02',72,460,100,55,36,'#62666C');text(s,d.change,190,460,970,110,34);
s.speakerNotes.text+=' Logo rengi araştırması bu kararı değiştirmez. Önce ek ücret ve hesap koşulunu çözün.';
await(await PresentationFile.exportPptx(p)).save(path.join(build,'candidate.pptx'));
const finalized=await finalizePresentation({workspaceDir:dir,candidatePath:path.join(build,'candidate.pptx'),finalPath:path.join(dir,'output/atolye-karar.pptx'),pythonExecutable:process.env.RUNTIME_PYTHON,integrityValidatorPath:path.join(sk,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(sk,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit','--require-native-table-slide','2'],explicitTotalSlideCount:3,requiredNativeTableOwnerSlides:[2],fontPolicy:{basis:'design',families:['Arial']},verifyArtifactToolImport:true,receiptPath:path.join(dir,'validation.json')});
console.log('Finalized presentation');
const final=await PresentationFile.importPptx(await FileBlob.load(path.join(dir,'output/atolye-karar.pptx')));
async function png(p,s,name){const b=await p.export({slide:s,format:'png',scale:1});await fs.writeFile(path.join(dir,'output',name),new Uint8Array(await b.arrayBuffer()));}
for(const [i,slide] of final.slides.items.entries())await png(final,slide,`atolye-slayt-${i+1}.png`);
const before=Presentation.create({slideSize:{width:1280,height:720}});
s=base(before,2,'Aynı ölçütlerle üç seçeneği karşılaştır','KARARIN DAYANAĞI');text(s,d.dense,72,270,1136,330,32);await png(before,s,'atolye-slayt-once.png');
const chartdata=JSON.parse(await fs.readFile(path.join(dir,'chart.json'),'utf8'));
const cp=Presentation.create({slideSize:{width:1280,height:720}});s=base(cp,1,'Altı kayıt, üç ayrı durum','CSV → KAYIT SAYISI');
const chart=s.charts.add('bar',{position:{left:100,top:245,width:1050,height:330},categories:chartdata.map(x=>x[0]),series:[{name:'Kayıt sayısı',values:chartdata.map(x=>x[1]),fill:'#454A50'}],hasLegend:false,barOptions:{direction:'column',gapWidth:150},dataLabels:{showValue:true,position:'outEnd',textStyle:{typeface:'Arial',fontSize:26}},yAxis:{minimumScale:0,maximumScale:4,majorUnit:1,majorGridlines:{fill:'#DFE1E3',width:1}},xAxis:{textStyle:{typeface:'Arial',fontSize:24}}});
applyPresentationChartFont(chart,{fontFamily:'Arial',fontSize:24});
text(s,'Bu grafik geliri veya kişi sayısını değil, kayit_id ile ayrılan kayıtları gösterir.',72,590,1136,60,24,'#62666C');await png(cp,s,'katilim-grafik.png');
