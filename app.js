import issues from "./data.js";

const FILTERS = ["All","New Concepts","Cyber-Elegance","Bio-Futurism","Neo-Brutalist","Digital Surrealism","Gothic Luxury"];
const pillMap = {
  "All": null,
  "New Concepts": "New Concepts",
  "Cyber-Elegance": "Cyber-Elegance",
  "Bio-Futurism": "Bio-Futurism",
  "Neo-Brutalist": "Neo-Brutalist",
  "Digital Surrealism": "Digital Surrealism",
  "Gothic Luxury": "Gothic Luxury"
};

let activeFilter = "All";
let filtered = [...issues];
let currentIdx = 0;

const filterBar = document.getElementById("filterBar");
const grid = document.getElementById("grid");
const countLabel = document.getElementById("countLabel");

// --- render filter pills ---
FILTERS.forEach(f=>{
  const b = document.createElement("button");
  b.className = "pill" + (f===activeFilter ? " active":"");
  b.textContent = f;
  b.addEventListener("click", ()=>{
    activeFilter = f;
    document.querySelectorAll(".pill").forEach(p=>p.classList.toggle("active", p.textContent===f));
    applyFilter();
  });
  filterBar.appendChild(b);
});

// search via "/" key — simple prompt
document.addEventListener("keydown",(e)=>{
  if(e.key==="/" && !e.metaKey && !e.ctrlKey && document.activeElement.tagName!=="INPUT"){
    e.preventDefault();
    const q = prompt("Search covers (title, collection, tag, story):");
    if(q){
      filtered = issues.filter(it=> (it.title+" "+it.collection+" "+it.tag+" "+it.story+" "+it.hook).toLowerCase().includes(q.toLowerCase()));
      activeFilter = "Search: "+q;
      renderGrid();
    }
  }
});

function applyFilter(){
  const want = pillMap[activeFilter];
  if(!want) filtered = [...issues];
  else filtered = issues.filter(i=> i.pillar===want);
  renderGrid();
}

function renderGrid(){
  grid.innerHTML="";
  countLabel.textContent = `Showing ${filtered.length} of ${issues.length} issues` + (activeFilter!=="All"? ` · ${activeFilter}`:"");
  filtered.forEach((it, idx)=>{
    const card = document.createElement("div");
    card.className="card";
    card.dataset.idx = idx;
    // accent dot: if palette is gradient, use middle
    const dotBg = it.palette.startsWith("linear") ? "#A855F7" : it.palette;
    card.innerHTML = `
      <img src="${it.src}" alt="${it.title}" loading="lazy" />
      <div class="grad"></div>
      <div class="info">
        <div class="tag mono"><span class="dot" style="background:${dotBg}"></span>${it.tag}</div>
        <h4>${it.title}</h4>
        <div class="sub">${it.collection}</div>
      </div>
    `;
    card.addEventListener("click", ()=> openLightbox(idx));
    grid.appendChild(card);
  });
}

// hero click
document.getElementById("heroCard").addEventListener("click", ()=>{
  const idx = filtered.findIndex(f=>f.id==="ferrofluid-obsidian");
  if(idx>=0) openLightbox(idx);
  else openLightbox(0);
});
document.getElementById("randomBtn").addEventListener("click", ()=>{
  const r = Math.floor(Math.random()*filtered.length);
  openLightbox(r);
});

// lightbox
const lb = document.getElementById("lightbox");
const lbImg = document.getElementById("lbImg");
const lbKicker = document.getElementById("lbKicker");
const lbTitle = document.getElementById("lbTitle");
const lbMeta = document.getElementById("lbMeta");
const lbHook = document.getElementById("lbHook");
const lbStory = document.getElementById("lbStory");
const lbCTA = document.getElementById("lbCTA");
const lbPrompt = document.getElementById("lbPrompt");
const lbHashtags = document.getElementById("lbHashtags");
const dlLink = document.getElementById("dlLink");

function openLightbox(idx){
  currentIdx = idx;
  const it = filtered[idx];
  lbImg.src = it.src;
  lbImg.alt = it.title;
  lbKicker.textContent = it.tag + " · " + it.collection;
  lbTitle.textContent = it.title;
  lbMeta.innerHTML = `
    <span class="chip" style="border-color:${it.palette.includes('#')?it.palette:'#2a2a2a'}">Masthead: ${it.masthead}</span>
    <span class="chip">${it.pillar}</span>
    <span class="chip">${it.palette.startsWith('linear')? 'Iridescent': it.palette}</span>
  `;
  lbHook.textContent = it.hook || "";
  lbStory.textContent = it.story || "";
  lbCTA.textContent = it.cta ? "CTA: " + it.cta : "";
  lbPrompt.textContent = it.prompt || "Prompt coming soon — see playbook.";
  lbHashtags.textContent = it.hashtags || "";
  dlLink.href = it.src;
  dlLink.download = it.id + ".jpg";
  lb.classList.add("open");
  lb.setAttribute("aria-hidden","false");
  document.body.style.overflow="hidden";
}
function closeLightbox(){
  lb.classList.remove("open");
  lb.setAttribute("aria-hidden","true");
  document.body.style.overflow="";
}
document.getElementById("lbClose").addEventListener("click", closeLightbox);
lb.addEventListener("click", (e)=>{ if(e.target===lb) closeLightbox(); });
document.getElementById("lbPrev").addEventListener("click", (e)=>{ e.stopPropagation(); currentIdx = (currentIdx-1+filtered.length)%filtered.length; openLightbox(currentIdx); });
document.getElementById("lbNext").addEventListener("click", (e)=>{ e.stopPropagation(); currentIdx = (currentIdx+1)%filtered.length; openLightbox(currentIdx); });
document.addEventListener("keydown",(e)=>{
  if(!lb.classList.contains("open")) return;
  if(e.key==="Escape") closeLightbox();
  if(e.key==="ArrowLeft") { currentIdx=(currentIdx-1+filtered.length)%filtered.length; openLightbox(currentIdx); }
  if(e.key==="ArrowRight") { currentIdx=(currentIdx+1)%filtered.length; openLightbox(currentIdx); }
});
document.getElementById("copyCaption").addEventListener("click", ()=>{
  const it = filtered[currentIdx];
  const caption = `${it.hook}\n\n${it.story}\n\n${it.cta || ""}\n\n${it.hashtags||""}\n\n— ${it.title} · ${it.collection}`;
  navigator.clipboard.writeText(caption).then(()=>{
    const b=document.getElementById("copyCaption"); const t=b.textContent; b.textContent="Copied ✓"; setTimeout(()=>b.textContent=t,1400);
  });
});
document.getElementById("copyPrompt").addEventListener("click", ()=>{
  const it = filtered[currentIdx];
  navigator.clipboard.writeText(it.prompt||"").then(()=>{
    const b=document.getElementById("copyPrompt"); const t=b.textContent; b.textContent="Copied ✓"; setTimeout(()=>b.textContent=t,1400);
  });
});
document.getElementById("shareBtn").addEventListener("click", async ()=>{
  const it = filtered[currentIdx];
  const data = { title: it.title, text: it.hook + " — " + it.collection, url: location.href };
  if(navigator.share){ try{ await navigator.share(data);}catch{} } else {
    await navigator.clipboard.writeText(location.href + "\n" + it.title + " — " + it.src);
    const b=document.getElementById("shareBtn"); const t=b.textContent; b.textContent="Link copied ✓"; setTimeout(()=>b.textContent=t,1400);
  }
});

// init
renderGrid();

// expose for debug
window._issues = issues;
