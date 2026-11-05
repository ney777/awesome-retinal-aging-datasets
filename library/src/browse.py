"""Generate a self-contained offline reader from the same tables used for CSV and SQLite."""
import json
from collections import defaultdict
from pathlib import Path


def render(root, tables, stats):
    topics = defaultdict(list)
    clinical = defaultdict(list)
    evidence = defaultdict(list)
    for entry in tables["topics"]:
        if entry["tier"] != "Unknown":
            topics[entry["id"]].append([entry[k] for k in ("topic", "tier", "reason", "evidence_id")])
    for entry in tables["phenotypes"]:
        if entry["evidence_id"] != "Unknown" or entry["status"] != "Uncertain":
            clinical[entry["id"]].append([entry[k] for k in ("field", "status", "scope", "evidence_id")])
    for entry in tables["evidence"]:
        evidence[entry["id"]].append([entry[k] for k in ("evidence_id", "url", "locator", "checked")])

    items = []
    for row in tables["master"]:
        key = row["id"]
        # Omit repeated unknown values; the reader explicitly reconstructs all seven topics and clinical fields.
        info = {k: v for k, v in row.items() if v not in (None, "", "Unknown")}
        items.append(dict(info=info, topics=topics[key], clinical=clinical[key], evidence=evidence[key]))
    payload = dict(items=items, rankings=tables["rankings"], stats=stats)
    data = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    data = data.replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e")
    (Path(root) / "index.html").write_text(PAGE.replace("%%RESOURCE_JSON%%", data), encoding="utf-8")


PAGE = r'''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>眼底影像与衰老研究资源库</title>
<style>
:root {color-scheme:light;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;color:#19332e;background:#f7f8f3;line-height:1.5}
* {box-sizing:border-box}
body {margin:0} button,select,input {font:inherit} button,a,select,input {touch-action:manipulation}
a {color:#09695d} button {cursor:pointer} button:disabled {cursor:default;opacity:.4} [hidden] {display:none!important}
:focus-visible {outline:3px solid #ca7939;outline-offset:2px}
header {background:#103b32;color:#f5f8ed;border-bottom:5px solid #b4cda3}
.head,main {max-width:1170px;margin:auto;padding:23px 32px}
.head {display:flex;align-items:flex-end;justify-content:space-between;gap:16px}.kicker {font-size:.8rem;letter-spacing:.07em;color:#b7d4bc}
h1 {font-size:clamp(1.65rem,3.5vw,2.65rem);font-weight:650;margin:7px 0 4px;line-height:1.28}
.head p {margin:6px 0 0;color:#d8e6da}.head a {color:#f8fff7;white-space:nowrap;font-size:.9rem}
main {padding-top:17px}.tabs {display:flex;gap:7px;border-bottom:1px solid #cad6c9;margin-bottom:17px;padding-bottom:8px}
.tabs button,.mode-btn {border:0;background:transparent;border-radius:6px;padding:7px 12px;color:#365448}
.tabs button[aria-pressed=true],.mode-btn[aria-pressed=true] {color:#fff;background:#225c49}
.filters,.rankbar {display:grid;grid-template-columns:minmax(210px,2.6fr) repeat(3,minmax(130px,1fr));gap:13px;align-items:end}
label {font-size:.84rem;color:#375247} input[type=search],select {width:100%;background:#fff;border:1px solid #b5c8ba;border-radius:6px;padding:8px 9px;color:#173e31}
.bar {display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin:14px 0}
.count {font-weight:650}.spacer {flex:1}
.quiet {color:#51645b;font-size:.9rem}.subtle,.pager button,.close {border:1px solid #c0cec2;background:white;color:#235644;border-radius:6px;padding:5px 10px}
.grid {display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}.card {display:flex;flex-direction:column;align-items:flex-start;background:white;border:1px solid #d1dbce;border-radius:9px;padding:14px 16px;min-width:0}
.card h3 {line-height:1.35;margin:5px 0 6px;overflow-wrap:anywhere}.link-button {font-size:inherit;text-align:left;color:#164b3c;font-weight:650;background:none;border:0;padding:0}.link-button:hover {text-decoration:underline}
.id,.tag,.mono {font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.78rem}.id {color:#53645b;overflow-wrap:anywhere}
.meta,.chips {display:flex;align-items:center;gap:6px;flex-wrap:wrap}.chips {margin-top:auto;padding-top:10px}.tag {background:#ecf2e9;border-radius:4px;padding:2px 6px;color:#395342}.tag.direct {background:#d5eadd;color:#19523a}.meta {font-size:.85rem;color:#465b50}.desc {color:#526458;font-size:.89rem;margin:4px 0;overflow-wrap:anywhere}
.pager {display:flex;justify-content:center;align-items:center;gap:12px;padding:18px 0}
.export {display:flex;gap:12px;align-items:center;flex-wrap:wrap;border-top:1px solid #cad6c9;padding-top:15px;font-size:.85rem}
.rankbar {display:flex;align-items:end;gap:16px;flex-wrap:wrap}.switches {display:flex;gap:4px;align-items:center}
.scroll {overflow-x:auto}.ranktable {background:#fff;min-width:690px}
table {width:100%;border-collapse:collapse;text-align:left;font-size:.9rem} th,td {padding:8px 6px;border-bottom:1px solid #e0e7df;vertical-align:top}
thead {background:#edf3eb;color:#34513c} .ranktable th:first-child {width:3rem}
dialog {width:min(920px,96vw);max-height:88vh;border:1px solid #bccdbd;border-radius:10px;padding:0;color:#203b2d;box-shadow:0 12px 55px #102d2f30}
dialog::backdrop {background:#18362d80}.modal-head {display:flex;align-items:center;gap:12px;padding:12px 20px;background:#eef4ec;position:sticky;top:0;z-index:2;border-bottom:1px solid #d1dece}
.modal-head b {flex:1;overflow-wrap:anywhere}.modal-body {padding:7px 20px 22px}.modal-body h3 {font-size:1.05rem;border-bottom:1px solid #bbd1bf;padding-bottom:5px;margin:20px 0 8px}
.modal-body p {overflow-wrap:anywhere}.facts {display:grid;grid-template-columns:8rem minmax(0,1fr);gap:5px 13px;font-size:.91rem;margin:8px 0}
.facts dt {color:#53665c}.facts dd {margin:0;overflow-wrap:anywhere}.sources li {margin-bottom:9px;overflow-wrap:anywhere;scroll-margin-top:64px}
.sources li:target,.source-highlight {background:#fff4d9}.ref {background:none;border:0;text-decoration:underline;color:#17664e;padding:0 3px;font-size:.8rem}
.empty {padding:24px;background:white;border:1px dashed #c3d2c2;border-radius:8px;color:#496156}
@media(max-width:800px){.filters{grid-template-columns:repeat(2,minmax(0,1fr))}.head,main{padding-left:18px;padding-right:18px}}
@media(max-width:600px){.grid{grid-template-columns:1fr}.head{display:block}.head a{display:inline-block;margin-top:10px}.facts{grid-template-columns:5rem minmax(0,1fr)}.bar{gap:8px}.rankbar{gap:6px}.tabs button{padding:7px 9px}.modal-body{padding:5px 12px 18px}}
</style>
</head>
<body>
<header><div class="head"><div><div class="kicker">科研数据目录 · 离线快照</div><h1>眼底影像与衰老研究资源库</h1>
<p id="overview"></p></div><a href="RESEARCH_GUIDE.md">阅读研究指南 ↗</a></div></header>
<main>
<nav class="tabs" aria-label="主要视图"><button id="catalogTab" aria-pressed="true">资源检索</button><button id="rankTab" aria-pressed="false">专题排名</button></nav>
<section id="catalogPane">
<div class="filters">
<label>关键词<input type="search" id="query" placeholder="数据集、国家、疾病、字段或证据"></label>
<label>研究专题<select id="topic"><option value="">全部专题</option></select></label>
<label>该专题的证据等级<select id="tier"><option value="">全部等级</option><option>Tier 1</option><option>Tier 2</option><option>Tier 3</option><option value="Excluded">Excluded · 排除</option><option value="Unknown">Unknown · 未判定</option></select></label>
<label>获取方式<select id="access"><option value="">全部获取方式</option></select></label>
</div>
<div class="bar"><label><input id="reviewed" type="checkbox"> 仅看经过原始来源核验的资源</label><span class="spacer"></span><button id="reset" class="subtle">清空筛选</button></div>
<p class="quiet">选定专题后可查该专题的 T1 直接关联、T2 待确认关联、T3 辅助资源或排除项。未选专题时，等级按每条资源的最高证据判断。</p>
<div id="count" class="bar count" aria-live="polite"></div><div class="grid" id="cards"></div>
<div class="pager"><button id="prev">上一页</button><span id="page"></span><button id="next">下一页</button></div>
</section>
<section id="rankPane" hidden>
<div class="rankbar"><label>科研方向<select id="track"><option>Retinal Aging</option><option>Eye–Stroke</option><option>Eye–Neurodegeneration</option></select></label>
<div class="switches"><button class="mode-btn" id="science" aria-pressed="true">科学价值</button><button class="mode-btn" id="ready" aria-pressed="false">近期可用</button></div></div>
<p class="quiet">科学价值按研究适配、标签、队列和多中心价值计分。近期可用另计获取可行性，并须通过该科研方向的影像和标签门槛。评分针对已评审候选，分项及分母可在表内核对。</p>
<div id="ranking"></div>
</section>
<footer class="export" aria-label="本地数据文件"><strong>本地文件</strong><a href="output/master.csv">资源主表 CSV</a><a href="output/phenotypes.csv">临床字段</a><a href="output/topics.csv">专题判定</a><a href="output/evidence.csv">证据表</a><a href="output/relationships.csv">资源关系</a><a href="output/search_log.csv">检索日志</a><a href="output/rankings.csv">排名明细</a><a href="output/resources.sqlite">SQLite 数据库</a></footer>
</main>
<dialog id="detail" aria-labelledby="detailTitle"><div class="modal-head"><b id="detailTitle">资源详情</b><button class="close" id="close">关闭</button></div><div class="modal-body" id="body"></div></dialog>
<noscript>交互筛选需要启用 JavaScript。完整记录可通过上方本地 CSV 和 SQLite 链接读取。</noscript>
<script id="payload" type="application/json">%%RESOURCE_JSON%%</script>
<script>
'use strict';
const library=JSON.parse(document.getElementById('payload').textContent);
const byId=new Map(library.items.map(x=>[x.info.id,x]));
const topicNames={A:'年龄与衰老',B:'脑卒中与脑血管风险',C:'脑 MRI 与小血管病',D:'AD、认知与痴呆',E:'其他神经系统疾病',F:'心血管、代谢与死亡',G:'多中心与基础模型'};
const clinicalNames={age:'年龄 / 衰老',sex:'性别',hypertension:'高血压',diabetes:'糖尿病',cardiovascular:'心血管病',stroke_type:'卒中分型 / 中风',stroke_time:'卒中事件时间',brain_mri:'脑 MRI / 脑磁共振',csvd:'脑小血管病 / 白质高信号 / CSVD',ad:'阿尔茨海默病 / Alzheimer',dementia:'痴呆',cognition:'认知功能 / 评分',parkinson:'帕金森病',frailty:'衰弱',health:'健康状态',mortality:'死亡结局',followup:'纵向随访'};
const accessNames={'Open download':'开放下载','Registration':'注册或确认条款','Controlled access':'受控访问','Application':'提交申请','Author contact':'联系作者','Unavailable':'不可获取','Unknown':'未知'};
const statusNames={Confirmed:'Confirmed · 已确认',Uncertain:'Uncertain · 待确认','Not available':'Not available · 不提供'};
const unknown='Unknown · 未核实',pageSize=16;
const $=id=>document.getElementById(id);
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const validURL=s=>/^https?:\/\//i.test(s||'');
function link(url,label){return validURL(url)?'<a href="'+esc(url)+'" target="_blank" rel="noopener noreferrer">'+esc(label)+'</a>':esc(label);}
const shown=v=>v && v!=='Unknown'?esc(v):unknown;
const norm=v=>String(v??'').normalize('NFKC').toLowerCase();
const az=Object.keys(topicNames);
for(const [k,v] of Object.entries(topicNames)) $('topic').add(new Option(k+' · '+v,k));
for(const [k,v] of Object.entries(accessNames)) $('access').add(new Option(v,k));
const stats=library.stats;
$('overview').textContent=stats.master+' 条资源记录 · '+stats.source_reviewed+' 条经过来源核验 · '+stats.baseline+' 条 EyeDataHub 基线记录';
const aliases=[
 [/fundus|fundus photograph|眼底彩照|视网膜彩照/i,'眼底照片 眼底彩照 视网膜彩色摄影 CFP'],
 [/OCTA|OCT.angiography|OCT-Angiography/i,'光学相干断层血管成像 OCTA'],
 [/\bOCT\b|SD.OCT|SS.OCT|光学相干断层/i,'光学相干断层扫描 OCT'],
 [/ultra.?widefield|UWF/i,'超广角眼底 超广域 UWF'],
 [/\bMRI\b|magnetic resonance/i,'磁共振 脑MRI'],
 [/UK Biobank/i,'英国生物银行 UKB'], [/NHANES/i,'美国国家健康与营养调查'],
 [/stroke/i,'脑卒中 中风'], [/Alzheimer/i,'阿尔茨海默病 AD'],
 [/Parkinson/i,'帕金森病 PD'], [/white matter hyperintens|\bWMH\b/i,'白质高信号 WMH'],
 [/dementia/i,'痴呆'], [/cognit/i,'认知'], [/mortality/i,'死亡 死亡率'],
 [/diabetes|diabetic/i,'糖尿病'], [/\baging\b|\bageing\b/i,'衰老 老龄 生物年龄']
];
function makeIndex(item){
 const a=item.info;
 const text=Object.values(a).join(' ')+' '+item.topics.map(t=>t.join(' ')+' '+topicNames[t[0]]).join(' ')+' '+
  item.clinical.map(p=>p.join(' ')+' '+(clinicalNames[p[0]]||p[0])).join(' ')+' '+item.evidence.map(e=>e.join(' ')).join(' ');
 return norm(text+' '+(accessNames[a.access]||'')+' '+aliases.filter(([re])=>re.test(text)).map(x=>x[1]).join(' '));
}
const listing=library.items.map(item=>({item,idx:makeIndex(item)})).sort((a,b)=>
 (a.item.info.review_depth!=='Source-reviewed')-(b.item.info.review_depth!=='Source-reviewed') ||
 ({'Tier 1':1,'Tier 2':2,'Tier 3':3,Excluded:4}[a.item.info.best_tier]||5)-({'Tier 1':1,'Tier 2':2,'Tier 3':3,Excluded:4}[b.item.info.best_tier]||5) ||
 a.item.info.name.localeCompare(b.item.info.name));
let page=1, practical=false;
function topicTier(item,topic){return item.topics.find(t=>t[0]===topic)?.[1]||'Unknown';}
function matches(entry,words,topic,tier,access,reviewed){
 const it=entry.item,a=it.info;
 if(reviewed && a.review_depth!=='Source-reviewed') return false;
 if(access && (a.access||'Unknown')!==access) return false;
 if(!words.every(w=>entry.idx.includes(w))) return false;
 if(!topic) return !tier || a.best_tier===tier;
 const value=topicTier(it,topic);
 return tier ? value===tier : value.startsWith('Tier ');
}
function card(it){
 const a=it.info, tags=it.topics.filter(t=>t[1].startsWith('Tier '));
 return '<article class="card"><span class="id">'+esc(a.id)+'</span><h3><button class="link-button" data-record="'+esc(a.id)+'">'+esc(a.name)+'</button></h3>'+
 '<div class="meta"><span>'+shown(a.country)+'</span><span>·</span><span>'+esc(accessNames[a.access]||a.access||'未知获取方式')+'</span><span>·</span><span>'+esc(a.review_depth==='Source-reviewed'?'已核验来源':'基线筛查')+'</span></div>'+
 '<div class="desc">'+shown(a.modalities)+'</div><div class="chips">'+(tags.length?tags.map(t=>'<span class="tag '+(t[1]==='Tier 1'?'direct':'')+'">'+esc(t[0]+' '+t[1].replace('Tier ','T'))+'</span>').join(''):'<span class="tag">Excluded</span>')+'</div></article>';
}
function showCatalog(){
 const words=norm($('query').value.trim()).split(/\s+/).filter(Boolean);
 const matchesNow=listing.filter(e=>matches(e,words,$('topic').value,$('tier').value,$('access').value,$('reviewed').checked));
 const pages=Math.max(1,Math.ceil(matchesNow.length/pageSize));
 page=Math.max(1,Math.min(page,pages));
 $('count').textContent='匹配 '+matchesNow.length+' 条资源记录';
 $('cards').innerHTML=matchesNow.length?matchesNow.slice((page-1)*pageSize,page*pageSize).map(e=>card(e.item)).join(''):'<p class="empty">当前筛选没有匹配记录。</p>';
 $('page').textContent='第 '+page+' / '+pages+' 页';$('prev').disabled=page===1;$('next').disabled=page===pages;
}
function facts(a,fields){return '<dl class="facts">'+fields.map(([k,label])=>'<dt>'+esc(label)+'</dt><dd>'+shown(a[k])+'</dd>').join('')+'</dl>';}
function refs(ids){if(!ids||ids==='Unknown') return '';
 return ids.split(' | ').map(id=>'<button class="ref" data-ref="'+esc(id)+'">'+esc(id.slice(id.lastIndexOf('#')+1))+'</button>').join('');}
function details(it){
 const a=it.info,topics=az.map(k=>it.topics.find(t=>t[0]===k)||[k,'Unknown','该专题未单独判定。','Unknown']);
 const known=new Map(it.clinical.map(field=>[field[0],field]));
 const clinical=[...new Set([...Object.keys(clinicalNames),...known.keys()])].map(k=>known.get(k)||[k,'Uncertain','无该字段的专门证据。','Unknown']);
 const evidence=it.evidence.map(([id,url,loc,date])=>'<li data-anchor="'+esc(id)+'"><b>'+esc(id.slice(id.lastIndexOf('#')+1))+'</b> · '+link(url,'原始来源 ↗')+' · '+shown(date)+'<br>'+esc(loc)+'</li>').join('');
 return '<div class="meta"><span class="mono">'+esc(a.id)+'</span> · '+esc(a.review_depth)+' · '+shown(a.checked)+'</div>'+
 '<p>'+link(a.official_url,'官方资源 ↗')+'　'+link(a.access_url,'访问或申请入口 ↗')+'</p>'+
 '<h3>科研用途及配对条件</h3>'+facts(a,[['pairing','配对依据'],['strengths','主要优点'],['limitations','关键限制'],['experiment','建议实验'],['screen_reason','筛查依据']])+
 '<h3>专题判定</h3><div class="scroll"><table><thead><tr><th>专题</th><th>等级</th><th>判定依据</th></tr></thead><tbody>'+topics.map(t=>'<tr><td>'+esc(t[0]+' · '+topicNames[t[0]])+'</td><td>'+esc(t[1])+'</td><td>'+esc(t[2])+' '+refs(t[3])+'</td></tr>').join('')+'</tbody></table></div>'+
 '<h3>获取与用途</h3>'+facts({...a,accessLabel:accessNames[a.access]||a.access},[['accessLabel','获取方式'],['image_access','影像文件'],['label_access','个体标签'],['license','数据许可'],['research_terms','科研条件'],['commercial_terms','商业用途'],['terms_scope','条款范围'],['route_last_checked','上游路径复核']])+
 '<h3>影像与来源</h3>'+facts(a,[['country','国家或地区'],['institution','机构'],['year','年份'],['citation','原始引用'],['doi','DOI'],['dataset_doi','数据 DOI'],['modalities','模态'],['images','图像'],['participants','参与者'],['eyes','眼别'],['device','设备'],['resolution','分辨率'],['quality','质量控制'],['multivisit','多时点'],['multimodal','多模态'],['multicenter','多中心'],['family','数据家族'],['relation','家族关系'],['duplicate_status','独立性'],['origin','收录来源']])+
 '<h3>临床表型</h3><div class="scroll"><table><thead><tr><th>字段</th><th>状态</th><th>适用范围 / 证据</th></tr></thead><tbody>'+
 clinical.map(p=>'<tr><td>'+esc(clinicalNames[p[0]]||p[0])+'</td><td>'+esc(statusNames[p[1]]||p[1])+'</td><td>'+esc(p[2])+' '+refs(p[3])+'</td></tr>').join('')+'</tbody></table></div>'+
 '<h3>核验来源</h3><ol class="sources">'+evidence+'</ol>';
}
function openDetail(id){
 const it=byId.get(id);if(!it)return;
 $('detailTitle').textContent=it.info.name;$('body').innerHTML=details(it);
 if(!$('detail').open)$('detail').showModal();
 $('detail').scrollTop=0;
}
function showRanks(){
 const track=$('track').value;
 const rs=library.rankings.filter(r=>r.track===track && (!practical||r.near_term==='Yes')).sort((a,b)=>Number(a[practical?'practical_rank':'scientific_rank'])-Number(b[practical?'practical_rank':'scientific_rank']));
 $('science').setAttribute('aria-pressed',String(!practical));$('ready').setAttribute('aria-pressed',String(practical));
 if(!rs.length){$('ranking').innerHTML='<p class="empty">'+(practical?'本快照中没有通过该方向近期可用门槛的资源。可切换到科学价值视图查看合作或申请候选。':'本快照在该方向未收录排名。')+'</p>';return;}
 $('ranking').innerHTML='<div class="scroll"><table class="ranktable"><thead><tr><th>排名</th><th>资源与实验终点</th><th>得分</th><th>R / L / Q / X / M</th><th>样本量口径</th></tr></thead><tbody>'+
 rs.map(r=>'<tr><td>'+esc(r[practical?'practical_rank':'scientific_rank'])+'</td><td><button class="link-button" data-record="'+esc(r.id)+'">'+esc(r.name)+'</button><br>'+esc(r.endpoint)+'</td><td>'+esc(r[practical?'practical_score':'scientific_score'])+'</td><td>'+[r.R,r.L,r.Q,r.X,r.M].map(esc).join(' / ')+'</td><td>'+esc(r.paired_n_basis||unknown)+'</td></tr>').join('')+'</tbody></table></div>'+
 '<p class="quiet">R 研究问题适配度 · L 标签丰富度 · Q 队列质量 · X 获取可行性 · M 多中心价值。分项为 0–4 分。</p>';
}
function setTab(ranks){$('rankPane').hidden=!ranks;$('catalogPane').hidden=ranks;$('rankTab').setAttribute('aria-pressed',String(ranks));$('catalogTab').setAttribute('aria-pressed',String(!ranks));if(ranks)showRanks();}
for(const id of ['topic','tier','access','reviewed']) $(id).addEventListener('change',()=>{page=1;showCatalog();});
$('query').addEventListener('input',()=>{page=1;showCatalog();});
$('reset').addEventListener('click',()=>{for(const id of ['query','topic','tier','access'])$(id).value='';$('reviewed').checked=false;page=1;showCatalog();});
$('prev').addEventListener('click',()=>{page--;showCatalog();$('count').scrollIntoView({block:'start'});});
$('next').addEventListener('click',()=>{page++;showCatalog();$('count').scrollIntoView({block:'start'});});
$('rankTab').addEventListener('click',()=>setTab(true));$('catalogTab').addEventListener('click',()=>setTab(false));
$('science').addEventListener('click',()=>{practical=false;showRanks();});$('ready').addEventListener('click',()=>{practical=true;showRanks();});
$('track').addEventListener('change',showRanks);$('close').addEventListener('click',()=>$('detail').close());
document.addEventListener('click',event=>{
 const button=event.target.closest('[data-record],[data-ref]');
 if(!button)return;
 if(button.hasAttribute('data-record')){openDetail(button.dataset.record);return;}
 const anchors=Array.from($('body').querySelectorAll('[data-anchor]'));
 anchors.forEach(el=>el.classList.toggle('source-highlight',el.dataset.anchor===button.dataset.ref));
 anchors.find(el=>el.dataset.anchor===button.dataset.ref)?.scrollIntoView({block:'center'});
});
showCatalog();
</script></body></html>'''
