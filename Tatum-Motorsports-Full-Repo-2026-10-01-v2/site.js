// Local image previews are intentionally not public uploads. Permanent images live in assets/.
document.querySelectorAll('[data-image-slot]').forEach(slot=>{
 const input=slot.querySelector('input'), img=slot.querySelector('img'), status=slot.querySelector('[role=status]');let url;
 input.addEventListener('change',()=>{const file=input.files[0];if(!file)return;if(!['image/jpeg','image/png','image/webp'].includes(file.type)){status.textContent='Choose a JPG, PNG, or WebP image.';return;}if(url)URL.revokeObjectURL(url);url=URL.createObjectURL(file);img.src=url;img.style.display='block';status.textContent='Preview only. To publish this photo, add it to the site project.';});
});
const current=document.querySelector('.nav [aria-current="page"]');if(current){const nav=current.parentElement;nav.scrollLeft=Math.max(0,current.offsetLeft-nav.clientWidth/2+current.clientWidth/2);}
// Opening a topic link also reveals that topic; ordinary page loads stay collapsed.
function revealDynamicsHash(){const id=decodeURIComponent(location.hash.slice(1));const target=document.getElementById(id);if(target?.matches('details.dynamics-section'))target.open=true;}
window.addEventListener('hashchange',revealDynamicsHash);
document.querySelectorAll('.topic-nav a').forEach(a=>a.addEventListener('click',()=>{const target=document.getElementById(a.hash.slice(1));if(target?.matches('details'))target.open=true;}));
revealDynamicsHash();
