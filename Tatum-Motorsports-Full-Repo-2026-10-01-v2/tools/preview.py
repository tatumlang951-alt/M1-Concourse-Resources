"""Build a portable, single-file review copy; the published site remains nine pages."""
from pathlib import Path
import re,base64
root=Path(__file__).resolve().parents[1]
pages=[('index','Home'),('organizations','Organizations'),('experience','Get Experience'),('skills','Skills'),('careers','Careers'),('vehicle-dynamics','Vehicle Dynamics'),('projects','Projects'),('resources','Resources'),('books','Books')]
parts=[]
for page,title in pages:
 s=(root/f'{page}.html').read_text().split('<main id="main">',1)[1].split('</main>',1)[0]
 def image(m):
  p=root/m[1];mime='image/jpeg' if p.suffix=='.jpg' else 'image/png';return 'src="data:'+mime+';base64,'+base64.b64encode(p.read_bytes()).decode()+'"'
 s=re.sub(r'src="(assets/[^\"]+)"',image,s)
 s=re.sub(r'href="([a-z-]+)\.html(?:#([^\"]+))?"',lambda m:'href="#'+m[1]+('/'+m[2] if m[2] else '')+'"',s)
 s=re.sub(r'href="#(aero|springs|dampers|alignment|geometry|oval|brakes|differential|tires)"',lambda m:'href="#vehicle-dynamics/'+m[1]+'"',s)
 parts.append(f'<div data-preview-page="{page}"'+(' hidden' if page!='index' else '')+'>'+s+'</div>')
css=(root/'styles.css').read_text()+'\n[hidden]{display:none!important}'
nav=''.join(f'<a href="#{p}">{t}</a>' for p,t in pages)
js=(root/'site.js').read_text()+'''
function route(){const [p,a]=(location.hash.slice(1)||'index').split('/');const key=document.querySelector('[data-preview-page="'+CSS.escape(p)+'"]')?p:'index';document.querySelectorAll('[data-preview-page]').forEach(x=>x.hidden=x.dataset.previewPage!==key);document.querySelectorAll('.nav a').forEach(x=>{if(x.hash==='#'+key)x.setAttribute('aria-current','page');else x.removeAttribute('aria-current');});if(a){const target=document.getElementById(a);if(target?.matches('details'))target.open=true;requestAnimationFrame(()=>target?.scrollIntoView());}else scrollTo(0,0);}window.addEventListener('hashchange',route);document.querySelectorAll('.topic-nav a').forEach(a=>a.addEventListener('click',()=>{const target=document.getElementById(a.hash.split('/')[1]);if(target?.matches('details'))target.open=true;}));route();'''
html='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Tatum Langston — Site preview</title><style>'+css+'</style></head><body><header class="topbar"><nav class="nav" aria-label="Main navigation">'+nav+'</nav></header><main id="main">'+''.join(parts)+'</main><footer class="footer">Tatum Langston · Motorsports resources</footer><script>'+js+'</script></body></html>'
p=root.parent/'Tatum-Motorsports-Preview.html';p.write_text(html);print(p.name,p.stat().st_size)
