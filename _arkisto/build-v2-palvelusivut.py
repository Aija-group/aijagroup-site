# -*- coding: utf-8 -*-
"""Staattinen sivustogeneraattori Äijä Group Oy:n sivustolle.
Aja:  python3 build.py   -> tuottaa site/-kansion."""
import os, shutil, json, html
from content import (SITE, NAV, HERO, CLAIMS, SERVICES, PROCESS, MODELS, AUDIENCES, SITUATIONS,
                     PRINCIPLES, ABOUT, FAQ_GENERAL, PRIVACY, TOOLS)

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "site")
SRC = os.path.join(ROOT, "src")
ACT = ' class="active"'

def esc(t):
    return html.escape(t, quote=True)

def img_exists(name):
    return os.path.exists(os.path.join(SRC, "img", name))

# ---------------------------------------------------------------------------
# Ikonit
# ---------------------------------------------------------------------------
_S = 'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"'
ICONS = {
    "target": f'<svg {_S}><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.2" fill="currentColor"/><path d="M12 3v3M21 12h-3"/></svg>',
    "chart": f'<svg {_S}><path d="M4 20h16"/><path d="M6 16l4-5 3 3 5-7"/><path d="M18 7h-3M18 7v3"/></svg>',
    "meta": f'<svg {_S}><path d="M3 15c0-4 2-9 4.5-9S11 11 12 13c1-2 2-7 4.5-7S21 11 21 15c0 2-1 3-2.5 3-3 0-4-6-6.5-6s-3.5 6-6.5 6C4 18 3 17 3 15z"/></svg>',
    "search": f'<svg {_S}><circle cx="11" cy="11" r="6.5"/><path d="m20 20-4.3-4.3"/></svg>',
    "spark": f'<svg {_S}><path d="M12 3c.6 4 2.5 6.4 7 7-4.5.6-6.4 3-7 7-.6-4-2.5-6.4-7-7 4.5-.6 6.4-3 7-7z"/><path d="M19 15c.3 1.7 1 2.7 3 3-2 .3-2.7 1.3-3 3-.3-1.7-1-2.7-3-3 2-.3 2.7-1.3 3-3z"/></svg>',
    "chat": f'<svg {_S}><path d="M4 6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H9l-5 4z"/><path d="M8 9h8M8 12h5"/></svg>',
    "users": f'<svg {_S}><circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14.2c2.9.4 5 2.8 5 5.8"/></svg>',
    "megaphone": f'<svg {_S}><path d="M3 11v2a2 2 0 0 0 2 2h2l7 4V5L7 9H5a2 2 0 0 0-2 2z"/><path d="M17 9a4 4 0 0 1 0 6"/><path d="M7 15v4a1 1 0 0 0 1 1h1"/></svg>',
    "browser": f'<svg {_S}><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18"/><circle cx="6.5" cy="6.5" r=".6" fill="currentColor"/><circle cx="9" cy="6.5" r=".6" fill="currentColor"/><path d="M7 13h6M7 16h10"/></svg>',
    "cart": f'<svg {_S}><path d="M3 4h2l2.5 11h11L21 7H6"/><circle cx="9" cy="19" r="1.4"/><circle cx="17" cy="19" r="1.4"/></svg>',
    "box": f'<svg {_S}><path d="M3 8l9-4 9 4-9 4z"/><path d="M3 8v8l9 4 9-4V8"/><path d="M12 12v8"/></svg>',
    "rocket": f'<svg {_S}><path d="M12 3c3 2 5 6 5 10l-5 4-5-4c0-4 2-8 5-10z"/><circle cx="12" cy="10" r="1.6"/><path d="M7 13l-3 3 3 .5M17 13l3 3-3 .5M12 17v4"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5 10 17.5 19 7"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "mail": f'<svg {_S}><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
    "linkedin": f'<svg {_S}><rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10v7M8 7v.1M12 17v-4a2 2 0 0 1 4 0v4M12 10v7"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
    "close": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>',
    "chev": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>',
    "x": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M7 7l10 10M17 7 7 17"/></svg>',
}
def ic(name, cls="ic"):
    return f'<span class="{cls}" aria-hidden="true">{ICONS[name]}</span>'

# Logomerkki: kaksi pistettä (ä:n umlaut) ja viiva
MARK = '<svg viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="9" fill="var(--ink)"/><circle cx="14" cy="14" r="4" fill="var(--accent)"/><circle cx="26" cy="14" r="4" fill="var(--accent)"/><rect x="9" y="24" width="22" height="5" rx="2.5" fill="var(--paper)"/></svg>'
def logo(cls="logo"):
    return f'<a class="{cls}" href="/" aria-label="{esc(SITE["name"])} – etusivu"><span class="mark">{MARK}</span><span class="word">ÄIJÄ<small>Group</small></span></a>'

# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------
CSS = r"""
:root{
  --paper:#f4f1ea;--paper2:#ebe7dd;--ink:#14130f;--ink2:#23221d;--line:#d9d4c8;--line-dark:#34322b;
  --text:#14130f;--muted:#5c5a54;--faint:#8b887f;--accent:#ff4d1a;--accent-dark:#d63a0c;--accent-ink:#fff;
  --font:'Inter',system-ui,-apple-system,'Segoe UI',sans-serif;--display:'Bricolage Grotesque','Inter',system-ui,sans-serif;
  --r:8px;--r2:18px;--w:1240px;
}
*{box-sizing:border-box}html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--text);font-family:var(--font);font-size:17px;line-height:1.6;overflow-x:hidden}
img{max-width:100%;height:auto;display:block}
a{color:var(--ink);text-decoration:none}a:hover{text-decoration:underline;text-decoration-thickness:1.5px;text-underline-offset:3px}
h1,h2,h3,h4{font-family:var(--display);font-weight:700;line-height:1.02;margin:0 0 .5em;letter-spacing:-.025em}
h1{font-size:clamp(2.7rem,6.4vw,5.6rem);font-weight:800}
h2{font-size:clamp(2rem,4vw,3.4rem)}
h3{font-size:clamp(1.3rem,2vw,1.6rem);letter-spacing:-.015em}
p{margin:0 0 1em}
.wrap{max-width:var(--w);margin:0 auto;padding:0 clamp(18px,4vw,44px)}
.ic{display:inline-flex;width:1.1em;height:1.1em;vertical-align:-.2em}.ic svg{width:100%;height:100%}
.eyebrow{font-family:var(--font);font-weight:600;font-size:.8rem;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);margin-bottom:16px;display:flex;align-items:center;gap:10px}
.eyebrow::before{content:"";width:22px;height:2px;background:var(--accent);display:inline-block}
.lead{font-size:clamp(1.1rem,1.5vw,1.3rem);color:var(--muted);max-width:60ch;line-height:1.55}
.muted{color:var(--muted)}.small{font-size:.9rem;color:var(--faint)}
section{padding:clamp(64px,8vw,120px) 0}
.sec-dark{background:var(--ink);color:var(--paper)}
.sec-dark h2,.sec-dark h3,.sec-dark a{color:var(--paper)}.sec-dark .lead,.sec-dark .muted,.sec-dark p{color:#bdb9ad}
.sec-alt{background:var(--paper2)}
.sec-head{max-width:820px;margin-bottom:clamp(36px,5vw,64px)}
.sec-head.center{margin-left:auto;margin-right:auto;text-align:center}.sec-head.center .eyebrow{justify-content:center}
.sec-head.row{max-width:none;display:grid;grid-template-columns:1.2fr 1fr;gap:40px;align-items:end}
@media(max-width:900px){.sec-head.row{grid-template-columns:1fr}}
.sec-head.row .lead{margin:0}
/* buttons */
.btn{display:inline-flex;align-items:center;gap:10px;padding:15px 24px;border-radius:999px;font-weight:600;font-size:1rem;border:1.5px solid transparent;transition:.2s;cursor:pointer;line-height:1;text-decoration:none!important;font-family:var(--font)}
.btn .ic{transition:.2s}.btn:hover .ic{transform:translateX(4px)}
.btn-primary{background:var(--accent);color:var(--accent-ink)}.btn-primary:hover{background:var(--accent-dark)}
.btn-ink{background:var(--ink);color:var(--paper)}.btn-ink:hover{background:var(--ink2)}
.btn-ghost{border-color:var(--ink);color:var(--ink);background:transparent}.btn-ghost:hover{background:var(--ink);color:var(--paper)}
.sec-dark .btn-ghost{border-color:var(--paper);color:var(--paper)}.sec-dark .btn-ghost:hover{background:var(--paper);color:var(--ink)}
.btn-lg{padding:18px 30px;font-size:1.05rem}
.more{display:inline-flex;align-items:center;gap:8px;font-weight:600;color:var(--ink);margin-top:auto}
.more .ic{color:var(--accent);transition:.2s}.more:hover .ic{transform:translateX(4px)}
/* header */
header.top{position:sticky;top:0;z-index:50;background:rgba(244,241,234,.88);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;height:74px;gap:20px}
.logo{display:flex;align-items:center;gap:12px;text-decoration:none!important;color:var(--ink)}
.logo .mark{width:38px;height:38px;flex:none;display:block}.logo .mark svg{width:100%;height:100%;display:block}
.logo .word{font-family:var(--display);font-weight:800;font-size:1.45rem;letter-spacing:-.02em;line-height:1;display:flex;align-items:baseline;gap:7px}
.logo .word small{font-family:var(--font);font-weight:500;font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
nav.main ul{list-style:none;margin:0;padding:0;display:flex;gap:6px;align-items:center}
nav.main a{padding:10px 14px;font-weight:500;font-size:.98rem;border-radius:999px;color:var(--ink);text-decoration:none!important}
nav.main a:hover{background:var(--paper2)}nav.main a.active{background:var(--ink);color:var(--paper)}
nav.main li.cta a{background:var(--accent);color:#fff;font-weight:600;margin-left:8px}nav.main li.cta a:hover{background:var(--accent-dark)}
.burger{display:none;background:none;border:1.5px solid var(--ink);color:var(--ink);width:44px;height:44px;border-radius:50%;align-items:center;justify-content:center;cursor:pointer}
.burger .ic{width:22px;height:22px}
@media(max-width:960px){
  .burger{display:flex}
  nav.main{position:absolute;top:100%;left:0;right:0;background:var(--paper);border-bottom:1px solid var(--line);display:none;padding:14px 18px 22px;box-shadow:0 20px 40px rgba(0,0,0,.08)}
  nav.main.open{display:block}
  nav.main ul{flex-direction:column;align-items:stretch;gap:2px}
  nav.main a{display:block;font-size:1.15rem;padding:14px 12px;border-radius:10px}
  nav.main li.cta a{margin:10px 0 0;text-align:center}
  .logo .word small{display:none}
}
/* hero */
.hero{position:relative;padding:clamp(70px,9vw,130px) 0 clamp(40px,5vw,70px);overflow:hidden}
.hero .wrap{position:relative}
.hero h1{max-width:16ch;margin-bottom:.35em}
.hero h1 .b{display:block;color:var(--accent)}
.hero .lead{max-width:56ch;margin-bottom:34px}
.hero .actions{display:flex;gap:12px;flex-wrap:wrap}
.hero-grid{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,.75fr);gap:clamp(30px,5vw,80px);align-items:end}
@media(max-width:960px){.hero-grid{grid-template-columns:1fr}}
.hero-side{display:grid;gap:14px}
.hero-side .tile{border:1px solid var(--line);border-radius:var(--r2);padding:20px 22px;background:rgba(255,255,255,.35)}
.hero-side .tile b{font-family:var(--display);font-weight:700;font-size:1.05rem;letter-spacing:-.01em;display:block;margin-bottom:4px}
.hero-side .tile span{color:var(--muted);font-size:.95rem}
.hero-side .tile .k{display:inline-block;width:10px;height:10px;border-radius:50%;background:var(--accent);margin-right:10px;vertical-align:1px}
.hero-mark{position:absolute;right:-6%;top:-12%;width:min(48vw,620px);opacity:.06;pointer-events:none}
@media(max-width:960px){.hero-mark{display:none}}
/* ticker */
.ticker{border-top:1px solid var(--line);border-bottom:1px solid var(--line);overflow:hidden;padding:16px 0;background:var(--paper)}
.ticker .track{display:flex;gap:0;width:max-content;animation:tick 40s linear infinite}
.ticker span{font-family:var(--display);font-weight:700;font-size:1.05rem;letter-spacing:-.01em;padding:0 22px;white-space:nowrap;color:var(--ink)}
.ticker span::after{content:"";display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--accent);margin-left:44px;vertical-align:2px}
@keyframes tick{to{transform:translateX(-50%)}}
@media(prefers-reduced-motion:reduce){.ticker .track{animation:none}}
/* grids & cards */
.grid{display:grid;gap:20px}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}.g3{grid-template-columns:repeat(3,minmax(0,1fr))}.g4{grid-template-columns:repeat(4,minmax(0,1fr))}
@media(max-width:1000px){.g3,.g4{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:640px){.g2,.g3,.g4{grid-template-columns:minmax(0,1fr)}}
.card{background:#fff;border:1px solid var(--line);border-radius:var(--r2);padding:30px 28px;display:flex;flex-direction:column;transition:.25s;position:relative}
a.card{text-decoration:none!important;color:inherit}
a.card:hover{transform:translateY(-3px);box-shadow:0 22px 44px -22px rgba(20,19,15,.25);border-color:#c9c3b3}
.card .ico{width:48px;height:48px;border-radius:12px;background:var(--paper);border:1px solid var(--line);display:flex;align-items:center;justify-content:center;color:var(--ink);margin-bottom:22px}
.card .ico .ic{width:24px;height:24px}
.card h3{margin-bottom:.45em}.card p{color:var(--muted);flex:1;margin-bottom:18px;font-size:1rem}
.card .num{font-family:var(--display);font-weight:800;font-size:.85rem;letter-spacing:.1em;color:var(--accent);margin-bottom:14px}
.sec-dark .card{background:var(--ink2);border-color:var(--line-dark)}
.sec-dark .card .ico{background:var(--ink);border-color:var(--line-dark);color:var(--paper)}
.sec-dark .card p{color:#bdb9ad}
.sec-dark a.card:hover{border-color:#55524a;box-shadow:none}
a.card.wide{grid-column:1/-1;flex-direction:row;align-items:center;gap:30px;flex-wrap:wrap;background:var(--ink);color:var(--paper);border-color:var(--ink);padding:36px 34px}
a.card.wide .ico{margin:0;background:var(--ink2);border-color:var(--line-dark);color:var(--paper)}
a.card.wide h3{margin:0;flex:1 1 260px;color:var(--paper);font-size:clamp(1.5rem,2.4vw,2rem)}
a.card.wide p{margin:0;flex:2 1 360px;color:#bdb9ad}
a.card.wide .num{margin:0;order:-1;flex:0 0 auto}
a.card.wide .more{color:var(--paper);flex:0 0 auto}
a.card.wide:hover{box-shadow:none;border-color:#55524a}
.tools{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-top:36px}
.tools .lbl{font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;font-weight:600;color:var(--faint);margin-right:8px}
.chip{border:1px solid var(--line);border-radius:999px;padding:8px 15px;font-weight:500;font-size:.9rem;background:#fff;color:var(--muted)}
/* claims */
.claims{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0;border:1px solid var(--line);border-radius:var(--r2);overflow:hidden;background:#fff}
.claims>div{padding:32px 30px;border-left:1px solid var(--line)}.claims>div:first-child{border-left:0}
@media(max-width:900px){.claims{grid-template-columns:1fr}.claims>div{border-left:0;border-top:1px solid var(--line)}.claims>div:first-child{border-top:0}}
.claims h3{font-size:1.25rem}.claims p{color:var(--muted);margin:0;font-size:1rem}
.claims .n{font-family:var(--display);font-weight:800;color:var(--accent);font-size:.85rem;letter-spacing:.1em;margin-bottom:14px}
/* steps */
.steps{display:grid;gap:0;border-top:1px solid var(--line-dark)}
.step{display:grid;grid-template-columns:110px minmax(0,1fr) 160px;gap:30px;padding:30px 0;border-bottom:1px solid var(--line-dark);align-items:start}
@media(max-width:760px){.step{grid-template-columns:70px minmax(0,1fr)}.step .dur{grid-column:2}}
.step .n{font-family:var(--display);font-size:clamp(2.2rem,4vw,3.2rem);font-weight:800;color:var(--accent);line-height:1;letter-spacing:-.03em}
.step h3{font-size:1.5rem;margin-bottom:.35em}.step p{margin:0;max-width:64ch}
.step .dur{font-family:var(--font);font-size:.82rem;letter-spacing:.1em;text-transform:uppercase;color:#bdb9ad;font-weight:600;text-align:right;padding-top:8px}
@media(max-width:760px){.step .dur{text-align:left}}
.sec-alt .steps{border-top-color:var(--line)}.sec-alt .step{border-bottom-color:var(--line)}.sec-alt .step .dur{color:var(--faint)}
/* situations */
.situations{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
@media(max-width:760px){.situations{grid-template-columns:1fr}}
.situations li{background:#fff;border:1px solid var(--line);border-radius:var(--r2);padding:18px 20px;display:flex;gap:14px;align-items:flex-start;font-size:1.02rem}
.situations .ic{flex:none;width:26px;height:26px;color:var(--accent);background:rgba(255,77,26,.1);border-radius:8px;padding:5px;margin-top:1px}
/* founder */
.founder{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:clamp(30px,5vw,80px);align-items:center}
@media(max-width:900px){.founder{grid-template-columns:1fr}}
.portrait{aspect-ratio:4/5;border-radius:var(--r2);background:var(--ink);position:relative;overflow:hidden;display:flex;align-items:flex-end;padding:28px}
.portrait img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.portrait .init{position:absolute;left:28px;top:20px;font-family:var(--display);font-weight:800;font-size:clamp(6rem,14vw,11rem);color:var(--paper);opacity:.08;letter-spacing:-.05em;line-height:1}
.portrait .cap{position:relative;color:var(--paper);z-index:2}
.portrait .cap b{display:block;font-family:var(--display);font-size:1.5rem;font-weight:700;letter-spacing:-.02em}
.portrait .cap span{color:#bdb9ad;font-size:.95rem}
.portrait .dots{position:absolute;right:28px;top:28px;display:flex;gap:10px}.portrait .dots i{width:16px;height:16px;border-radius:50%;background:var(--accent);display:block}
blockquote{margin:0 0 22px;font-family:var(--display);font-size:clamp(1.4rem,2.3vw,2rem);font-weight:600;line-height:1.25;letter-spacing:-.02em}
blockquote::before{content:"“";color:var(--accent)}blockquote::after{content:"”";color:var(--accent)}
/* models */
.models{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
@media(max-width:900px){.models{grid-template-columns:1fr}}
.model{background:#fff;border:1px solid var(--line);border-radius:var(--r2);padding:32px 30px;display:flex;flex-direction:column}
.model .tag{font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;font-weight:600;color:var(--faint);margin-bottom:18px}
.model h3{font-size:1.6rem}.model p{color:var(--muted);flex:1}
.model.hi{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.model.hi h3{color:var(--paper)}.model.hi p{color:#bdb9ad}.model.hi .tag{color:var(--accent)}
/* faq */
.faq{border-top:1px solid var(--line)}
.faq details{border-bottom:1px solid var(--line)}
.faq summary{cursor:pointer;list-style:none;padding:22px 0;display:flex;justify-content:space-between;gap:20px;align-items:center;font-family:var(--display);font-size:1.2rem;font-weight:600;letter-spacing:-.01em}
.faq summary::-webkit-details-marker{display:none}
.faq summary .ic{flex:none;transition:.2s;color:var(--accent);width:22px;height:22px}
.faq details[open] summary .ic{transform:rotate(180deg)}
.faq .a{padding:0 0 24px;color:var(--muted);max-width:72ch}
.sec-dark .faq,.sec-dark .faq details{border-color:var(--line-dark)}
/* cta band */
.cta-band{background:var(--accent);color:#fff;padding:clamp(60px,7vw,100px) 0}
.cta-band .wrap{display:grid;grid-template-columns:1.3fr 1fr;gap:40px;align-items:center}
@media(max-width:900px){.cta-band .wrap{grid-template-columns:1fr}}
.cta-band h2{color:#fff;margin-bottom:.3em}.cta-band p{color:rgba(255,255,255,.85);max-width:56ch;font-size:1.1rem}
.cta-band .eyebrow{color:#fff}.cta-band .eyebrow::before{background:#fff}
.cta-band .actions{display:flex;gap:12px;flex-wrap:wrap;justify-content:flex-end}
@media(max-width:900px){.cta-band .actions{justify-content:flex-start}}
.cta-band .btn-ink:hover{background:#000}
.cta-band .btn-ghost{border-color:#fff;color:#fff}.cta-band .btn-ghost:hover{background:#fff;color:var(--accent)}
/* page hero */
.phero{padding:clamp(60px,8vw,110px) 0 clamp(40px,5vw,70px);border-bottom:1px solid var(--line)}
.phero h1{max-width:20ch;font-size:clamp(2.4rem,5.4vw,4.6rem)}
.crumbs{font-size:.85rem;color:var(--faint);margin-bottom:26px;display:flex;flex-wrap:wrap;gap:0 .6em}
.crumbs a{color:var(--muted)}
/* layout w/ sidebar */
.cols{display:grid;grid-template-columns:minmax(0,1fr) 360px;gap:clamp(30px,5vw,80px);align-items:start}
@media(max-width:960px){.cols{grid-template-columns:minmax(0,1fr)}}
.cols>*,.f2>*{min-width:0}select{min-width:0;max-width:100%}
.prose p{color:var(--muted);font-size:1.1rem;max-width:68ch;line-height:1.65}
.prose h2{font-size:clamp(1.6rem,2.6vw,2.3rem);margin-top:1.6em}
.side{position:sticky;top:96px;display:grid;gap:18px}
.side .box{background:#fff;border:1px solid var(--line);border-radius:var(--r2);padding:28px}
.side .box.dark{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.side .box.dark h3{color:var(--paper)}.side .box.dark p{color:#bdb9ad}
.side h3{font-size:1.3rem}.side .box p{color:var(--muted);font-size:.98rem}
.side .box .btn{width:100%;justify-content:center;margin-top:8px}
.side ul.links{list-style:none;padding:0;margin:0}
.side ul.links li{border-top:1px solid var(--line)}
.side ul.links a{display:flex;justify-content:space-between;align-items:center;padding:12px 0;color:var(--ink);font-weight:500;text-decoration:none!important}
.side ul.links a .ic{color:var(--faint);width:18px;height:18px}
.side ul.links a.active,.side ul.links a:hover{color:var(--accent)}
.contact-lines{display:grid;gap:10px}
.contact-lines a{display:flex;gap:10px;align-items:center;color:inherit;font-size:1.02rem}
.contact-lines .ic{color:var(--accent);width:22px;height:22px;flex:none}
/* features */
.features{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin:30px 0}
@media(max-width:640px){.features{grid-template-columns:1fr}}
.feat{background:#fff;border:1px solid var(--line);border-radius:var(--r2);padding:22px 24px}
.feat b{display:block;font-family:var(--display);font-size:1.15rem;letter-spacing:-.01em;margin-bottom:6px;font-weight:700}
.feat b::before{content:"";display:inline-block;width:8px;height:8px;background:var(--accent);border-radius:50%;margin-right:10px;vertical-align:2px}
.feat span{color:var(--muted);font-size:.98rem}
/* principles */
.principles{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0;border-top:1px solid var(--line-dark)}
@media(max-width:760px){.principles{grid-template-columns:1fr}}
.principle{padding:32px 30px 32px 0;border-bottom:1px solid var(--line-dark)}
.principle:nth-child(odd){border-right:1px solid var(--line-dark);padding-right:40px}
.principle:nth-child(even){padding-left:40px}
@media(max-width:760px){.principle:nth-child(odd){border-right:0;padding-right:0}.principle:nth-child(even){padding-left:0}}
.principle h3{font-size:1.4rem}.principle p{margin:0}
.principle .n{font-family:var(--display);font-weight:800;color:var(--accent);font-size:.85rem;letter-spacing:.1em;margin-bottom:14px}
/* form */
form.contact{display:grid;gap:16px;grid-template-columns:minmax(0,1fr)}
.f2{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px}@media(max-width:600px){.f2{grid-template-columns:minmax(0,1fr)}}
label{display:block;font-size:.85rem;color:var(--muted);margin-bottom:6px;font-weight:600}
input,textarea,select{width:100%;min-width:0;background:#fff;border:1.5px solid var(--line);color:var(--ink);border-radius:10px;padding:14px 15px;font:inherit;font-size:1rem}
input:focus,textarea:focus,select:focus{outline:none;border-color:var(--ink);box-shadow:0 0 0 3px rgba(20,19,15,.08)}
textarea{min-height:150px;resize:vertical}
.consent{display:flex;gap:10px;align-items:flex-start;font-size:.92rem;color:var(--muted)}
.consent input{width:auto;margin-top:5px}
.hp{position:absolute;left:-9999px}
/* footer */
footer{background:var(--ink);color:#bdb9ad;padding:clamp(56px,7vw,90px) 0 30px}
footer .grid{grid-template-columns:1.5fr 1fr 1fr 1fr}
@media(max-width:900px){footer .grid{grid-template-columns:1fr 1fr}}@media(max-width:560px){footer .grid{grid-template-columns:1fr}}
footer .logo{color:var(--paper)}footer .logo .word small{color:#8b887f}
footer h4{color:var(--paper);font-size:.85rem;letter-spacing:.12em;text-transform:uppercase;font-family:var(--font);font-weight:600;margin-bottom:1.1em}
footer ul{list-style:none;margin:0;padding:0}footer li{margin-bottom:9px}footer a{color:#bdb9ad}footer a:hover{color:var(--paper)}
footer .bottom{margin-top:48px;padding-top:22px;border-top:1px solid var(--line-dark);display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;font-size:.86rem;color:#8b887f}
footer .bottom a{color:#8b887f}
.reveal{opacity:0;transform:translateY(14px);transition:opacity .6s ease,transform .6s ease}
.reveal.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none}}
"""

JS = r"""
(function(){
  var b=document.querySelector('.burger'),n=document.querySelector('nav.main');
  if(b&&n){b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);});}
  if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{rootMargin:'0px 0px -8% 0px'});
    document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});}
  else{document.querySelectorAll('.reveal').forEach(function(el){el.classList.add('in');});}
})();
"""

# ---------------------------------------------------------------------------
# Yhteiset palat
# ---------------------------------------------------------------------------
def org_jsonld():
    d = {
        "@context": "https://schema.org", "@type": "ProfessionalService", "@id": SITE["domain"] + "/#org",
        "name": SITE["name"], "alternateName": SITE["short"], "url": SITE["domain"] + "/",
        "logo": SITE["domain"] + "/img/logo.png", "image": SITE["domain"] + "/img/og.png",
        "description": SITE["description"], "email": SITE["email"],
        "founder": {"@type": "Person", "name": SITE["founder"], "jobTitle": SITE["founder_title"]},
        "areaServed": "FI", "address": {"@type": "PostalAddress", "addressCountry": "FI"},
        "knowsAbout": ["markkinointistrategia", "positiointi", "liidienhankinta", "brändimainonta", "sisältöstrategia", "sosiaalinen media", "verkkokauppa", "Meta-mainonta", "Google Ads", "ChatGPT Ads"],
    }
    if SITE.get("linkedin"):
        d["sameAs"] = [SITE["linkedin"]]
    if SITE.get("ytunnus"):
        d["vatID"] = "FI" + SITE["ytunnus"].replace("-", "")
    return d

def head(title, description, path, image="img/og.png", extra_ld=None, noindex=False):
    url = SITE["domain"] + path
    ld = [org_jsonld()] + (extra_ld or [])
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    robots = '<meta name="robots" content="noindex">\n' if noindex else ""
    return f"""<!DOCTYPE html>
<html lang="fi">
<head>
<meta charset="utf-8">
{robots}<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{esc(SITE['name'])}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE['domain']}/{image}">
<meta property="og:locale" content="fi_FI">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#f4f1ea">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">
{lds}
</head>
<body>
"""

def header(active=""):
    items = "".join(f'<li><a href="{h}"{ACT if h == active else ""}>{esc(t)}</a></li>' for t, h in NAV)
    return f"""<header class="top">
<div class="wrap">
{logo()}
<button class="burger" aria-label="Valikko" aria-expanded="false">{ic('menu')}</button>
<nav class="main" aria-label="Päävalikko"><ul>{items}<li class="cta"><a href="/yhteys/#kartoitus">Varaa kartoitus</a></li></ul></nav>
</div>
</header>
<main>
"""

def footer():
    svc = "".join(f'<li><a href="/palvelut/{s["slug"]}/">{esc(s["nav"])}</a></li>' for s in SERVICES)
    yt = f'<p class="small">Y-tunnus {SITE["ytunnus"]}</p>' if SITE.get("ytunnus") else ""
    li = f'<li><a href="{SITE["linkedin"]}" rel="noopener" target="_blank">{ic("linkedin")} LinkedIn</a></li>' if SITE.get("linkedin") else ""
    return f"""</main>
<footer>
<div class="wrap">
<div class="grid">
<div>
{logo()}
<p style="margin-top:20px;max-width:40ch">{esc(SITE['tagline'])}. Strategia ja positiointi, liidienhankinta, brändimainonta, orgaaninen some ja verkkokauppaprojektit.</p>
{yt}
</div>
<div><h4>Mitä teemme</h4><ul>{svc}</ul></div>
<div><h4>Yritys</h4><ul>
<li><a href="/toimintamalli/">Toimintamalli</a></li><li><a href="/kenelle/">Kenelle</a></li><li><a href="/yritys/">Yritys</a></li><li><a href="/ukk/">Usein kysyttyä</a></li><li><a href="/yhteys/">Yhteys</a></li></ul></div>
<div><h4>Ota yhteyttä</h4><ul>
<li><a href="mailto:{SITE['email']}">{ic('mail')} {SITE['email']}</a></li>
{li}</ul></div>
</div>
<div class="bottom"><span>© 2026 {esc(SITE['name'])}</span><span><a href="/tietosuoja/">Tietosuojaseloste</a></span></div>
</div>
</footer>
<script src="/js/main.js" defer></script>
</body>
</html>
"""

def crumbs(items):
    parts = ['<a href="/">Etusivu</a>']
    for t, h in items:
        parts.append(f'<a href="{h}">{esc(t)}</a>' if h else f"<span>{esc(t)}</span>")
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Etusivu", "item": SITE["domain"] + "/"}] + [
        {"@type": "ListItem", "position": i + 2, "name": t, **({"item": SITE["domain"] + h} if h else {})} for i, (t, h) in enumerate(items)]}
    return f'<div class="crumbs">{"<span>/</span>".join(parts)}</div>', ld

def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

def faq_block(items, title="Usein kysyttyä"):
    d = "".join(f'<details><summary>{esc(q)}{ic("chev")}</summary><div class="a">{esc(a)}</div></details>' for q, a in items)
    return f'<h2>{esc(title)}</h2><div class="faq">{d}</div>'

def phero(title, lead, crumb_items, eyebrow=None):
    c, ld = crumbs(crumb_items)
    eb = f'<div class="eyebrow">{esc(eyebrow)}</div>' if eyebrow else ""
    return f'<div class="phero"><div class="wrap">{c}{eb}<h1>{esc(title)}</h1><p class="lead">{esc(lead)}</p></div></div>', ld

def cta_band(title="Kerro, missä kasvu jumittaa", text="Varaa tunnin kartoituskeskustelu. Käymme läpi tilanteesi, markkinoinnin ja sivuston – ja sanomme suoraan, mitä tekisimme seuraavaksi. Ilman myyntipuhetta."):
    return f"""<section class="cta-band"><div class="wrap">
<div><div class="eyebrow">Ota yhteyttä</div><h2>{esc(title)}</h2><p>{esc(text)}</p></div>
<div class="actions"><a class="btn btn-ink btn-lg" href="/yhteys/#kartoitus">Varaa kartoituskeskustelu {ic('arrow')}</a><a class="btn btn-ghost" href="mailto:{SITE['email']}">{ic('mail')} {SITE['email']}</a></div>
</div></section>"""

def contact_box():
    return f"""<div class="box dark"><h3>Varaa kartoituskeskustelu</h3><p>Tunti aikaa, ei myyntipuhetta. Käymme läpi tilanteesi ja sanomme, mitä tekisimme.</p>
<a class="btn btn-primary" href="/yhteys/#kartoitus">Varaa aika {ic('arrow')}</a>
<div class="contact-lines" style="margin-top:18px"><a href="mailto:{SITE['email']}">{ic('mail')} {SITE['email']}</a></div></div>"""

def service_links(active=None):
    li = "".join(f'<li><a href="/palvelut/{s["slug"]}/"{ACT if s["slug"] == active else ""}>{esc(s["nav"])}{ic("arrow")}</a></li>' for s in SERVICES)
    return f'<div class="box"><h3>Mitä teemme</h3><ul class="links">{li}</ul></div>'

def svc_card(s, num=None, wide=False):
    n = f'<div class="num">0{num}</div>' if num else ""
    return f'<a class="card reveal{" wide" if wide else ""}" href="/palvelut/{s["slug"]}/">{n}<div class="ico">{ic(s["icon"])}</div><h3>{esc(s["title"])}</h3><p>{esc(s["short"])}</p><span class="more">Lue lisää {ic("arrow")}</span></a>'

def services_grid():
    cards = "".join(svc_card(s, i + 1, wide=s.get("wide", False)) for i, s in enumerate(SERVICES))
    return f'<div class="grid g4">{cards}</div>'

def tools_row():
    return '<div class="tools reveal"><span class="lbl">Työkalut ja kanavat</span>' + "".join(f'<span class="chip">{esc(t)}</span>' for t in TOOLS) + "</div>"

def steps_block():
    return '<div class="steps">' + "".join(
        f'<div class="step reveal"><div class="n">0{i+1}</div><div><h3>{esc(t)}</h3><p>{esc(x)}</p></div><div class="dur">{esc(d)}</div></div>'
        for i, (t, x, d) in enumerate(PROCESS)) + "</div>"

def models_block():
    out = ""
    for i, (t, x, tag) in enumerate(MODELS):
        hi = " hi" if i == 2 else ""
        out += f'<div class="model{hi} reveal"><div class="tag">{esc(tag)}</div><h3>{esc(t)}</h3><p>{esc(x)}</p><a class="more" href="/yhteys/#kartoitus" style="color:inherit">Kysy lisää {ic("arrow")}</a></div>'
    return f'<div class="models">{out}</div>'

def contact_form():
    return f"""<form class="contact" name="kartoitus" method="POST" action="/kiitos/" data-netlify="true" netlify-honeypot="bot-field">
<input type="hidden" name="form-name" value="kartoitus">
<p class="hp"><label>Älä täytä tätä: <input name="bot-field"></label></p>
<div class="f2"><div><label for="nimi">Nimi *</label><input id="nimi" name="nimi" required autocomplete="name"></div>
<div><label for="yritys">Yritys / brändi *</label><input id="yritys" name="yritys" required autocomplete="organization"></div></div>
<div class="f2"><div><label for="email">Sähköposti *</label><input id="email" type="email" name="email" required autocomplete="email"></div>
<div><label for="puhelin">Puhelin</label><input id="puhelin" type="tel" name="puhelin" autocomplete="tel"></div></div>
<div class="f2"><div><label for="www">Verkkosivu / verkkokauppa</label><input id="www" name="www" placeholder="https://" inputmode="url"></div>
<div><label for="budjetti">Mediabudjetti / kk</label><select id="budjetti" name="budjetti"><option value="">Valitse</option><option>Alle 3 000 €</option><option>3 000–10 000 €</option><option>10 000–30 000 €</option><option>Yli 30 000 €</option><option>Ei vielä mainontaa</option><option>Kyse on projektista (esim. verkkokauppa)</option></select></div></div>
<div><label for="tilanne">Mikä on tilanne? *</label><textarea id="tilanne" name="tilanne" required placeholder="Mitä myytte, kenelle, mitä markkinointia teette nyt ja mitä haluatte saada aikaan?"></textarea></div>
<label class="consent"><input type="checkbox" name="suostumus" required> <span>Hyväksyn tietojeni käsittelyn <a href="/tietosuoja/">tietosuojaselosteen</a> mukaisesti.</span></label>
<div><button class="btn btn-primary btn-lg" type="submit">Lähetä ja varaa aika {ic('arrow')}</button></div>
</form>"""

# ---------------------------------------------------------------------------
# Sivut
# ---------------------------------------------------------------------------
def page_home():
    title = "Äijä Group – Markkinointistrategioihin erikoistunut toimisto kuluttajabrändeille"
    desc = SITE["description"]
    h = head(title, desc, "/") + header("/")
    tiles = "".join(f'<div class="tile reveal"><b><span class="k"></span>{esc(t)}</b><span>{esc(x)}</span></div>' for t, x in [
        ("Strategia → viesti → kanavat → sivusto", "Yksi logiikka mainoksesta kassalle."),
        ("Tavoite ratkaisee kanavan", "Liidit, tunnettuus, some tai verkkokauppa – työkalut valitaan sen mukaan."),
        ("Raportointi liiketoiminnan luvuilla", "Liidin tai tilauksen hinta, kate ja kokonaistuotto – ei pelkkä ROAS."),
    ])
    ticker_items = ["Markkinointistrategia", "Positiointi", "Liidienhankinta", "Brändimainonta", "Orgaaninen some", "Verkkokauppaprojektit", "Strateginen kumppanuus", "Kuluttajabrändit"]
    ticker = "".join(f"<span>{esc(t)}</span>" for t in ticker_items) * 2
    claims = "".join(f'<div class="reveal"><div class="n">0{i+1}</div><h3>{esc(t)}</h3><p>{esc(x)}</p></div>' for i, (t, x) in enumerate(CLAIMS))
    auds = "".join(f'<div class="card reveal"><div class="ico">{ic(i)}</div><h3>{esc(t)}</h3><p>{esc(x)}</p></div>' for t, x, i in AUDIENCES)
    sits = "".join(f'<li class="reveal">{ic("check")}<span>{esc(s)}</span></li>' for s in SITUATIONS)
    portrait = f'<img src="/img/sulo-maki.jpg" alt="{esc(SITE["founder"])}, {esc(SITE["founder_title"].lower())}" loading="lazy">' if img_exists("sulo-maki.jpg") else '<div class="init">SM</div><div class="dots"><i></i><i></i></div>'
    h += f"""
<section class="hero">
<div class="hero-mark">{MARK}</div>
<div class="wrap">
<div class="hero-grid">
<div>
<div class="eyebrow">{esc(HERO['eyebrow'])}</div>
<h1>{esc(HERO['h1_a'])}<span class="b">{esc(HERO['h1_b'])}</span></h1>
<p class="lead">{esc(HERO['lead'])}</p>
<div class="actions"><a class="btn btn-primary btn-lg" href="/yhteys/#kartoitus">{esc(HERO['cta'])} {ic('arrow')}</a><a class="btn btn-ghost btn-lg" href="/palvelut/">{esc(HERO['cta2'])}</a></div>
</div>
<div class="hero-side">{tiles}</div>
</div>
</div>
</section>
<div class="ticker" aria-hidden="true"><div class="track">{ticker}</div></div>

<section>
<div class="wrap">
<div class="sec-head row"><div><div class="eyebrow">Miksi Äijä Group</div><h2>Kuluttajabrändin kasvu ei ole kanavaongelma</h2></div><p class="lead">Se on strategia-, viesti- ja toteutusongelma samaan aikaan. Siksi ratkaisemme ne yhdessä – emme lisää kampanjoita tai julkaisuja epäselvän suunnan taakse.</p></div>
<div class="claims">{claims}</div>
</div>
</section>

<section class="sec-alt">
<div class="wrap">
<div class="sec-head row"><div><div class="eyebrow">Mitä teemme</div><h2>Strategia ensin – sitten se, mitä tavoite vaatii</h2></div><p class="lead">Liidejä, tunnettuutta, toimivaa somea tai uusi verkkokauppa. Tavoite ratkaisee, mitä tehdään ja missä kanavissa – ja kaikki johdetaan samasta strategiasta.</p></div>
{services_grid()}
{tools_row()}
</div>
</section>

<section class="sec-dark">
<div class="wrap">
<div class="sec-head row"><div><div class="eyebrow">Toimintamalli</div><h2>Näin strateginen kumppanuus etenee</h2></div><p class="lead">Ensin diagnoosi, sitten päätökset, sitten toteutus. Jokaisessa vaiheessa tiedät, mitä tehdään, miksi ja mitä sen pitäisi tuottaa.</p></div>
{steps_block()}
<div style="margin-top:40px"><a class="btn btn-ghost" href="/toimintamalli/">Lue toimintamallista {ic('arrow')}</a></div>
</div>
</section>

<section>
<div class="wrap">
<div class="sec-head row"><div><div class="eyebrow">Kenelle</div><h2>Kuluttajabrändeille, jotka haluavat kasvaa kannattavasti</h2></div><p class="lead">Työskentelemme brändien kanssa, joilla on toimiva tuote ja halu tehdä markkinointia päätöksinä, ei arvauksina.</p></div>
<div class="grid g3" style="margin-bottom:56px">{auds}</div>
<h3 style="margin-bottom:22px">Tyypillisiä tilanteita, joissa meihin otetaan yhteyttä</h3>
<ul class="situations">{sits}</ul>
</div>
</section>

<section class="sec-alt">
<div class="wrap">
<div class="founder">
<div class="portrait reveal">{portrait}<div class="cap"><b>{esc(SITE['founder'])}</b><span>{esc(SITE['founder_title'])}, Äijä Group Oy</span></div></div>
<div class="reveal">
<div class="eyebrow">Perustaja</div>
<blockquote>Strategia on hyvä vain, jos se näkyy toteutuksessa ja kassassa. Siksi teen molemmat.</blockquote>
<p class="lead">{esc(ABOUT['founder_paragraphs'][0])}</p>
<a class="btn btn-ink" href="/yritys/">Tutustu yritykseen {ic('arrow')}</a>
</div>
</div>
</div>
</section>

<section>
<div class="wrap">
<div class="sec-head row"><div><div class="eyebrow">Yhteistyömallit</div><h2>Aloita kartoituksella tai suoraan kumppanuudella</h2></div><p class="lead">Kolme tapaa työskennellä kanssamme. Kartoituskeskustelun jälkeen ehdotamme, mikä sopii tilanteeseesi – tai sanomme, jos emme ole oikea kumppani.</p></div>
{models_block()}
</div>
</section>

<section class="sec-alt">
<div class="wrap"><div class="cols"><div>{faq_block(FAQ_GENERAL)}</div><aside class="side">{contact_box()}</aside></div></div>
</section>
{cta_band()}
"""
    return h + footer()

def page_services():
    title = "Mitä teemme – markkinointistrategia, liidienhankinta, brändimainonta, some, verkkokauppa | Äijä Group"
    desc = "Äijä Group kuluttajabrändeille: markkinointistrategia ja positiointi, liidienhankinta ja myynnin kasvattaminen, brändimainonta, orgaaninen some ja sisältöstrategia sekä verkkokauppa- ja sivustoprojektit."
    ph, ld = phero("Mitä teemme", "Olemme markkinointistrategioihin erikoistunut toimisto. Strategia on ydin – sen päälle toteutamme sen, mitä tavoite vaatii: liidejä, tunnettuutta, somea tai verkkokaupan. Yhden osan tai kokonaisuuden.", [("Mitä teemme", None)], eyebrow="Palvelut")
    h = head(title, desc, "/palvelut/", extra_ld=[ld]) + header("/palvelut/") + ph
    h += f'<section><div class="wrap">{services_grid()}{tools_row()}</div></section>'
    h += f'<section class="sec-dark"><div class="wrap"><div class="sec-head"><div class="eyebrow">Toimintamalli</div><h2>Näin yhteistyö etenee</h2></div>{steps_block()}</div></section>'
    h += f'<section><div class="wrap"><div class="sec-head"><div class="eyebrow">Yhteistyömallit</div><h2>Kartoitus, projekti tai kumppanuus</h2></div>{models_block()}</div></section>'
    h += cta_band()
    return h + footer()

def page_service(s):
    title = f"{s['title']} | Äijä Group"
    ph, ld = phero(s["title"], s["lead"], [("Mitä teemme", "/palvelut/"), (s["nav"], None)], eyebrow="Palvelu")
    svc_ld = {"@context": "https://schema.org", "@type": "Service", "name": s["title"], "description": s["meta"],
              "provider": {"@id": SITE["domain"] + "/#org"}, "areaServed": "FI", "url": f"{SITE['domain']}/palvelut/{s['slug']}/"}
    h = head(title, s["meta"], f"/palvelut/{s['slug']}/", extra_ld=[ld, svc_ld, faq_ld(s["faq"])]) + header("/palvelut/") + ph
    intro = "".join(f"<p>{esc(p)}</p>" for p in s["intro"])
    feats = "".join(f'<div class="feat"><b>{esc(t)}</b><span>{esc(x)}</span></div>' for t, x in s["features"])
    others = [o for o in SERVICES if o["slug"] != s["slug"]]
    others = (others[:1] if s["slug"] != "strategia" else []) + [o for o in others if o["slug"] != "strategia"][:3 - (1 if s["slug"] != "strategia" else 0)]
    h += f"""<section><div class="wrap"><div class="cols">
<div class="prose">{intro}
<h2>Mitä palvelu sisältää</h2>
<div class="features">{feats}</div>
{faq_block(s['faq'])}
</div>
<aside class="side">{contact_box()}{service_links(s['slug'])}</aside>
</div></div></section>
<section class="sec-alt"><div class="wrap"><div class="sec-head"><div class="eyebrow">Tutustu myös</div><h2>Muuta, mitä teemme</h2></div><div class="grid g3">{"".join(svc_card(o) for o in others)}</div></div></section>
{cta_band()}"""
    return h + footer()

def page_process():
    title = "Toimintamalli – strateginen kumppanuus kuluttajabrändille | Äijä Group"
    desc = "Näin Äijä Groupin strateginen kumppanuus etenee: diagnoosi, strategia ja positiointi, toteutussuunnitelma, toteutus sekä kuukausittainen mittaus ja optimointi. Periaatteet ja yhteistyömallit."
    ph, ld = phero("Toimintamalli", "Strateginen kumppani ei ole toimisto, joka toteuttaa briiffejä. Se on tekijä, joka vastaa siitä, että strategia, mainonta, sisällöt ja sivusto tuottavat yhdessä – ja sanoo suoraan, kun jokin ei toimi.", [("Toimintamalli", None)], eyebrow="Miten työskentelemme")
    h = head(title, desc, "/toimintamalli/", extra_ld=[ld]) + header("/toimintamalli/") + ph
    princ = "".join(f'<div class="principle reveal"><div class="n">0{i+1}</div><h3>{esc(t)}</h3><p>{esc(x)}</p></div>' for i, (t, x) in enumerate(PRINCIPLES))
    h += f"""<section class="sec-alt"><div class="wrap"><div class="sec-head"><div class="eyebrow">Vaiheet</div><h2>Diagnoosista jatkuvaan optimointiin</h2></div>{steps_block()}</div></section>
<section class="sec-dark"><div class="wrap"><div class="sec-head"><div class="eyebrow">Periaatteet</div><h2>Mihin työmme perustuu</h2></div><div class="principles">{princ}</div></div></section>
<section><div class="wrap"><div class="sec-head row"><div><div class="eyebrow">Yhteistyömallit</div><h2>Kolme tapaa aloittaa</h2></div><p class="lead">Aloitamme useimmiten kartoituksella. Se maksaa vähän, kestää lyhyen ajan ja kertoo molemmille, kannattaako jatkaa. Rajatun projektin – kuten verkkokaupan – voi ostaa myös suoraan.</p></div>{models_block()}</div></section>
{cta_band("Aloitetaan diagnoosista", "Kartoituskeskustelussa käymme läpi numerot, markkinoinnin ja sivuston. Saat rehellisen arvion siitä, missä kasvu jumittaa – vaikka päättäisit jatkaa jonkun muun kanssa.")}"""
    return h + footer()

def page_audience():
    title = "Kenelle – D2C- ja kuluttajabrändit | Äijä Group"
    desc = "Äijä Group työskentelee kuluttajabrändien kanssa: D2C-verkkokaupat, jälleenmyyjien kautta myyvät tuotebrändit ja kuluttajapalvelut, joiden kasvu tulee liideistä."
    ph, ld = phero("Kenelle", "Työskentelemme kuluttajabrändien kanssa, joilla on toimiva tuote tai palvelu ja halu kasvaa kannattavasti. Rajaamme asiakasmäärän, jotta perustaja tuntee jokaisen brändin luvut.", [("Kenelle", None)], eyebrow="Asiakkaamme")
    h = head(title, desc, "/kenelle/", extra_ld=[ld]) + header("/kenelle/") + ph
    auds = "".join(f'<div class="card reveal"><div class="ico">{ic(i)}</div><h3>{esc(t)}</h3><p>{esc(x)}</p></div>' for t, x, i in AUDIENCES)
    sits = "".join(f'<li class="reveal">{ic("check")}<span>{esc(s)}</span></li>' for s in SITUATIONS)
    h += f"""<section><div class="wrap"><div class="grid g3">{auds}</div></div></section>
<section class="sec-alt"><div class="wrap"><div class="cols"><div>
<div class="eyebrow">Tilanteet</div><h2>Milloin meihin otetaan yhteyttä</h2>
<p class="lead" style="margin-bottom:30px">Tunnistatko jonkin näistä? Silloin ongelma on todennäköisesti strategiassa, ei yksittäisessä kampanjassa.</p>
<ul class="situations" style="grid-template-columns:1fr">{sits}</ul>
</div><aside class="side">{contact_box()}{service_links()}</aside></div></div></section>
<section class="sec-dark"><div class="wrap"><div class="sec-head"><div class="eyebrow">Rehellisesti</div><h2>Kenelle emme sovi</h2></div>
<div class="grid g3">
<div class="card reveal"><div class="ico">{ic('x')}</div><h3>Testaamaton tuote</h3><p>Jos tuotteella ei ole vielä maksavia asiakkaita, mainonta ei korjaa sitä. Autamme mielellämme lanseerauksen suunnittelussa, mutta emme lupaa skaalausta ennen kuin kysyntä on todistettu.</p></div>
<div class="card reveal"><div class="ico">{ic('x')}</div><h3>Pelkkä toteutus ilman suuntaa</h3><p>Emme ota mainostiliä tai somea hoitoon ilman oikeutta puhua tavoitteesta, positiosta ja sivustosta. Jos haluat vain napin painajan, on halvempia vaihtoehtoja.</p></div>
<div class="card reveal"><div class="ico">{ic('x')}</div><h3>B2B ilman kuluttajalogiikkaa</h3><p>Ydinosaamisemme on kuluttajakaupassa. Pitkän myyntisyklin B2B-yrityksille ohjaamme sopivamman kumppanin.</p></div>
</div></div></section>
{cta_band()}"""
    return h + footer()

def page_company():
    title = "Yritys – Äijä Group Oy ja perustaja Sulo Mäki"
    desc = "Äijä Group Oy on Sulo Mäen perustama, markkinointistrategioihin erikoistunut toimisto kuluttajabrändeille. Strategia, liidienhankinta, brändimainonta, orgaaninen some ja verkkokauppaprojektit yhdellä logiikalla."
    ph, ld = phero(ABOUT["title"], ABOUT["lead"], [("Yritys", None)], eyebrow="Yritys")
    person_ld = {"@context": "https://schema.org", "@type": "Person", "name": SITE["founder"], "jobTitle": SITE["founder_title"],
                 "worksFor": {"@id": SITE["domain"] + "/#org"}, "url": SITE["domain"] + "/yritys/"}
    h = head(title, desc, "/yritys/", extra_ld=[ld, person_ld]) + header("/yritys/") + ph
    paras = "".join(f"<p>{esc(p)}</p>" for p in ABOUT["paragraphs"])
    fparas = "".join(f"<p>{esc(p)}</p>" for p in ABOUT["founder_paragraphs"])
    princ = "".join(f'<div class="principle reveal"><div class="n">0{i+1}</div><h3>{esc(t)}</h3><p>{esc(x)}</p></div>' for i, (t, x) in enumerate(PRINCIPLES))
    portrait = f'<img src="/img/sulo-maki.jpg" alt="{esc(SITE["founder"])}" loading="lazy">' if img_exists("sulo-maki.jpg") else '<div class="init">SM</div><div class="dots"><i></i><i></i></div>'
    facts = f'<div class="feat"><b>Yritys</b><span>{esc(SITE["name"])}{(", Y-tunnus " + SITE["ytunnus"]) if SITE.get("ytunnus") else ""}</span></div><div class="feat"><b>Perustaja</b><span>{esc(SITE["founder"])}, {esc(SITE["founder_title"].lower())}</span></div><div class="feat"><b>Erikoisala</b><span>Kuluttajabrändien markkinointistrategia ja sen toteutus</span></div><div class="feat"><b>Toimialue</b><span>Suomi; työ tehdään pääosin etänä, tapaamiset sovitusti</span></div>'
    h += f"""<section><div class="wrap"><div class="cols"><div class="prose">{paras}
<h2>Perustiedot</h2><div class="features">{facts}</div>
</div><aside class="side">{contact_box()}</aside></div></div></section>
<section class="sec-alt"><div class="wrap"><div class="founder">
<div class="portrait reveal">{portrait}<div class="cap"><b>{esc(SITE['founder'])}</b><span>{esc(SITE['founder_title'])}</span></div></div>
<div class="reveal prose"><div class="eyebrow">Perustaja</div><h2>{esc(SITE['founder'])}</h2>{fparas}
<a class="btn btn-ink" href="/yhteys/#kartoitus">Varaa keskustelu Sulon kanssa {ic('arrow')}</a></div>
</div></div></section>
<section class="sec-dark"><div class="wrap"><div class="sec-head"><div class="eyebrow">Periaatteet</div><h2>Mihin työmme perustuu</h2></div><div class="principles">{princ}</div></div></section>
{cta_band()}"""
    return h + footer()

def page_faq():
    title = "Usein kysyttyä – strategia, toteutus ja yhteistyö | Äijä Group"
    desc = "Vastauksia yleisimpiin kysymyksiin Äijä Groupin palveluista: miten yhteistyö alkaa, mitä se maksaa, kenelle palvelu sopii, kenen nimissä mainostilit ovat ja mitä eri palvelut sisältävät."
    ph, ld = phero("Usein kysyttyä", "Kokosimme vastaukset kysymyksiin, joita kuulemme useimmin. Jos omasi puuttuu, lähetä viesti – vastaamme suoraan.", [("Usein kysyttyä", None)], eyebrow="UKK")
    allq = list(FAQ_GENERAL)
    for s in SERVICES:
        allq += s["faq"]
    h = head(title, desc, "/ukk/", extra_ld=[ld, faq_ld(allq)]) + header("") + ph
    h += f'<section><div class="wrap"><div class="cols"><div>{faq_block(FAQ_GENERAL, "Yleistä")}<div style="height:44px"></div>' + "".join(faq_block(s["faq"], s["nav"]) + '<div style="height:44px"></div>' for s in SERVICES) + f'</div><aside class="side">{contact_box()}{service_links()}</aside></div></div></section>' + cta_band()
    return h + footer()

def page_contact():
    title = "Yhteys – varaa kartoituskeskustelu | Äijä Group"
    desc = f"Ota yhteyttä Äijä Groupiin ja varaa maksuton kartoituskeskustelu. Käymme läpi brändisi tilanteen, mainonnan ja sivuston tunnissa. Sähköposti {SITE['email']}."
    ph, ld = phero("Varaa kartoituskeskustelu", "Tunti aikaa, ei myyntipuhetta. Kerro tilanteesi, niin käymme läpi numerot, mainonnan ja sivuston – ja sanomme suoraan, mitä tekisimme seuraavaksi.", [("Yhteys", None)], eyebrow="Yhteys")
    h = head(title, desc, "/yhteys/", extra_ld=[ld]) + header("/yhteys/") + ph
    h += f"""<section><div class="wrap"><div class="cols">
<div><h2 id="kartoitus">Kerro tilanteesi</h2><p class="muted" style="margin-bottom:26px">Mitä tarkemmin kuvaat tuotteen, nykyisen markkinoinnin ja sen, mikä ei toimi, sitä hyödyllisempi ensimmäinen keskustelu on. Vastaamme kahden arkipäivän sisällä.</p>{contact_form()}</div>
<aside class="side">
<div class="box dark"><h3>Suoraan sähköpostilla</h3><p>Jos lomake ei ole sinun tapasi, lähetä viesti suoraan.</p><div class="contact-lines"><a href="mailto:{SITE['email']}">{ic('mail')} {SITE['email']}</a></div></div>
<div class="box"><h3>Näin kartoitus etenee</h3><p>1. Lähetät viestin.<br>2. Sovimme tunnin videopalaverin.<br>3. Käymme läpi luvut, mainostilit ja sivuston.<br>4. Saat kirjallisen arvion ja ehdotuksen seuraavista askelista.</p></div>
<div class="box"><h3>Ennen palaveria</h3><p>Hyödyllistä, jos voit antaa katseluoikeuden mainostileihin ja analytiikkaan. Ei pakollista – keskustelu onnistuu myös ilman.</p></div>
</aside></div></div></section>"""
    return h + footer()

def page_privacy():
    body = "".join(f"<h2>{esc(t)}</h2><p>{esc(x)}</p>" for t, x in PRIVACY)
    ph, ld = phero("Tietosuojaseloste", "Miten käsittelemme yhteydenottolomakkeella annettuja tietoja.", [("Tietosuojaseloste", None)])
    h = head("Tietosuojaseloste | Äijä Group Oy", "Äijä Group Oy:n tietosuojaseloste: mitä tietoja keräämme, mihin niitä käytetään ja mitkä ovat oikeutesi.", "/tietosuoja/", extra_ld=[ld]) + header("") + ph
    h += f'<section><div class="wrap"><div class="prose" style="max-width:760px">{body}<p class="small">Päivitetty 18.9.2026.</p></div></div></section>'
    return h + footer()

def page_thanks():
    ph, _ = phero("Kiitos viestistäsi", f"Palaamme asiaan kahden arkipäivän sisällä ja ehdotamme aikaa kartoituskeskustelulle. Kiireellisissä asioissa: {SITE['email']}.", [("Kiitos", None)])
    h = head("Kiitos yhteydenotosta | Äijä Group", "Kiitos viestistäsi. Otamme yhteyttä pian.", "/kiitos/", noindex=True) + header("") + ph
    h += f'<section><div class="wrap"><a class="btn btn-ink" href="/">Takaisin etusivulle {ic("arrow")}</a></div></section>'
    return h + footer()

def page_404():
    ph, _ = phero("Sivua ei löytynyt", "Osoite on muuttunut tai sivua ei ole. Etusivulta löydät kaikki palvelut.", [("404", None)])
    h = head("Sivua ei löytynyt | Äijä Group", "Sivua ei löytynyt.", "/404.html", noindex=True) + header("") + ph
    h += f'<section><div class="wrap"><a class="btn btn-ink" href="/">Etusivulle {ic("arrow")}</a></div></section>'
    return h + footer()

# ---------------------------------------------------------------------------
# Favicon, OG, build
# ---------------------------------------------------------------------------
FAVICON = MARK.replace("var(--ink)", "#14130f").replace("var(--accent)", "#ff4d1a").replace("var(--paper)", "#f4f1ea").replace(' aria-hidden="true"', ' xmlns="http://www.w3.org/2000/svg"')

def make_images():
    try:
        from PIL import Image, ImageDraw, ImageFont
    except Exception as e:
        print("PIL puuttuu, kuvat ohitettu:", e); return
    os.makedirs(os.path.join(OUT, "img"), exist_ok=True)
    INK, ACC, PAP = (20, 19, 15), (255, 77, 26), (244, 241, 234)
    def mark(size, bg=INK):
        im = Image.new("RGBA", (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(im); u = size / 40
        d.rounded_rectangle((0, 0, size, size), radius=9 * u, fill=bg)
        d.ellipse((10 * u, 10 * u, 18 * u, 18 * u), fill=ACC); d.ellipse((22 * u, 10 * u, 30 * u, 18 * u), fill=ACC)
        d.rounded_rectangle((9 * u, 24 * u, 31 * u, 29 * u), radius=2.5 * u, fill=PAP)
        return im
    mark(512).save(os.path.join(OUT, "img", "logo.png"))
    mark(180).save(os.path.join(OUT, "apple-touch-icon.png"))
    mark(256).save(os.path.join(OUT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    # OG-kuva
    W, H = 1200, 630
    og = Image.new("RGB", (W, H), PAP); d = ImageDraw.Draw(og)
    m = mark(120); og.paste(m, (80, 80), m)
    def font(sz, bold=True):
        for p in ["/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
                  "/System/Library/Fonts/Helvetica.ttc", "/Library/Fonts/Arial Bold.ttf"]:
            if os.path.exists(p):
                try: return ImageFont.truetype(p, sz)
                except Exception: pass
        return ImageFont.load_default()
    d.text((80, 260), "Strategia ensin.", fill=INK, font=font(66))
    d.text((80, 340), "Sitten toteutus, joka näkyy tuloksissa.", fill=ACC, font=font(52))
    d.text((80, 460), "ÄIJÄ GROUP  ·  Markkinointistrategioihin erikoistunut toimisto", fill=(92, 90, 84), font=font(28, False))
    og.save(os.path.join(OUT, "img", "og.png"))

def write(path, content):
    full = os.path.join(OUT, path.lstrip("/"))
    if path.endswith("/"):
        full = os.path.join(full, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

def build():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "css")); os.makedirs(os.path.join(OUT, "js"))
    if os.path.isdir(os.path.join(SRC, "img")):
        shutil.copytree(os.path.join(SRC, "img"), os.path.join(OUT, "img"), dirs_exist_ok=True)
    open(os.path.join(OUT, "css", "style.css"), "w").write(CSS)
    open(os.path.join(OUT, "js", "main.js"), "w").write(JS)
    open(os.path.join(OUT, "favicon.svg"), "w").write(FAVICON)
    make_images()

    pages = {"/": page_home(), "/palvelut/": page_services(), "/toimintamalli/": page_process(), "/kenelle/": page_audience(),
             "/yritys/": page_company(), "/ukk/": page_faq(), "/yhteys/": page_contact(), "/tietosuoja/": page_privacy(), "/kiitos/": page_thanks()}
    for s in SERVICES:
        pages[f"/palvelut/{s['slug']}/"] = page_service(s)
    for p, c in pages.items():
        write(p, c)
    write("/404.html", page_404())

    urls = [p for p in pages if p not in ("/kiitos/",)]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{SITE['domain']}{u}</loc><changefreq>monthly</changefreq><priority>{'1.0' if u == '/' else '0.8' if u.count('/') == 2 else '0.7'}</priority></url>\n" for u in urls) + "</urlset>\n"
    open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /kiitos/\nSitemap: {SITE['domain']}/sitemap.xml\n")
    open(os.path.join(OUT, "_redirects"), "w").write("/index.html / 301\n/404.html /404.html 404\n")
    open(os.path.join(OUT, "netlify.toml"), "w").write('[build]\n  publish = "."\n[[headers]]\n  for = "/*"\n  [headers.values]\n    X-Frame-Options = "DENY"\n    X-Content-Type-Options = "nosniff"\n    Referrer-Policy = "strict-origin-when-cross-origin"\n[[headers]]\n  for = "/img/*"\n  [headers.values]\n    Cache-Control = "public, max-age=31536000, immutable"\n')
    print(f"OK: {len(pages) + 1} sivua -> {OUT}")

if __name__ == "__main__":
    build()
