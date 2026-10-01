"""Check meaningful publishing risks: broken local links/assets and missing requested content."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.links=[];self.images=[];self.ids=set();self.h1=0;self.current=0;self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.add(a['id'])
  if tag=='h1':self.h1+=1
  if a.get('aria-current')=='page':self.current+=1
  if tag=='a':self.links.append(a.get('href',''))
  if tag=='img':self.images.append(a)
errors=[];docs={p.name:Page(p.read_text()) for p in ROOT.glob('*.html')}
for name,p in docs.items():
 if p.h1!=1:errors.append(f'{name}: expected one h1, found {p.h1}')
 if p.current!=1:errors.append(f'{name}: expected one current nav item')
 for url in p.links:
  u=urlsplit(url)
  if u.scheme:continue
  file=unquote(u.path) or name
  if not (ROOT/file).exists():errors.append(f'{name}: missing link {url}')
  if u.fragment and file in docs and u.fragment not in docs[file].ids:errors.append(f'{name}: missing anchor {url}')
 for img in p.images:
  if not img.get('alt'):errors.append(f'{name}: missing image alt')
  if img.get('src') and not (ROOT/img['src']).is_file():errors.append(f'{name}: missing image {img["src"]}')
texts={p.name:p.read_text() for p in ROOT.glob('*.html')}
required={'index.html':['Spire Motorsports','Windsor Racing','Lady Elizabeth EV','ShreveHart Racing','first annual Women with Drive case competition','Andretti Global','Utilimaster'], 'organizations.html':['Purdue Collegiate EV Grand Prix','High School EV Grand Prix','Collegiate iRacing League','eNASCAR College iRacing Series','Women with Drive Summit','NABME','National Association of Intercollegiate Racing'], 'resources.html':['10Iy0Ycy1hV00RteSvgVl-vmbamHn3wUH','ME 54255','MIA School of Race Engineering','pandas','Matplotlib','Kaggle'], 'careers.html':['Human Resources','Accountant','Truck Driver','Machinist','Car Chief','Crew Chief','Sponsorships'], 'vehicle-dynamics.html':['Damper shaft-velocity guide','Crossweight','Stagger','Rake' if False else 'rake','Differential','Tire pressures'], 'experience.html':['Internships','mechanic','data analyst','pit-crew']}
for name,terms in required.items():
 for term in terms:
  if term not in texts[name]:errors.append(f'{name}: missing {term}')
if 'Strategy Engineer' in texts['careers.html']:errors.append('Strategy Engineer must be absent')
if texts['books.html'].count('class="book ')!=27:errors.append('Expected 27 books')
if texts['books.html'].count('class="book recommended"')!=4:errors.append('Expected first four book outlines')
for name,t in texts.items():
 for bad in ['Details to verify','unpublished draft','COMING SOON']:
  if bad.lower() in t.lower():errors.append(f'{name}: unwanted {bad}')
assert len(docs)==9,f'Expected 9 pages; got {len(docs)}'
assert not errors,'\n'.join(errors)
print(f'PASS: {len(docs)} pages; local links and images resolve; 27 books / 4 highlighted; required content present.')
print(f'{sum(len(p.images) for p in docs.values())} image elements.')
