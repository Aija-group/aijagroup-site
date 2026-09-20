# -*- coding: utf-8 -*-
"""Äijä Group Oy – yksisivuinen sivusto. Aja: python3 build.py -> site/"""
import os, re, shutil, json, html
from content import (SITE, NAV, TITLE, HERO, WHY, RECOGNIZE, RECOGNIZE_CLOSING, POSITIONING, MESSAGE, SERVICES, DELIVERABLES_INTRO,
                     DELIVERABLES, PROCESS, MODELS_TITLE, MODELS, MEDIA, FOUNDER, CONTACT, FOOTER_LINE, PRIVACY)

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "site")
SRC = os.path.join(ROOT, "src")

def esc(t): return html.escape(t, quote=True)
def img_exists(name): return os.path.exists(os.path.join(SRC, "img", name))

_S = 'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
ICONS = {
    "arrow": f'<svg {_S}><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "mail": f'<svg {_S}><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
    "check": f'<svg {_S}><path d="M5 12.5 10 17.5 19 7"/></svg>',
    "menu": f'<svg {_S}><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
    "linkedin": f'<svg {_S}><rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10v7M8 7v.1M12 17v-4a2 2 0 0 1 4 0v4M12 10v7"/></svg>',
}
def ic(n): return f'<span class="ic" aria-hidden="true">{ICONS[n]}</span>'

MARK = '<svg viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="9" fill="var(--ink)"/><circle cx="14" cy="14" r="4" fill="var(--accent)"/><circle cx="26" cy="14" r="4" fill="var(--accent)"/><rect x="9" y="24" width="22" height="5" rx="2.5" fill="var(--paper)"/></svg>'
def logo(): return f'<a class="logo" href="/" aria-label="{esc(SITE["name"])}"><span class="mark">{MARK}</span><span class="word">ÄIJÄ<small>Group</small></span></a>'

CSS = r"""
:root{--paper:#f4f1ea;--paper2:#ebe7dd;--ink:#14130f;--ink2:#23221d;--line:#d9d4c8;--line-dark:#34322b;--muted:#5c5a54;--faint:#8b887f;--accent:#ff4d1a;--accent-dark:#d63a0c;
--font:'Inter',system-ui,-apple-system,'Segoe UI',sans-serif;--display:'Bricolage Grotesque','Inter',system-ui,sans-serif;--r:18px;--w:1140px}
*{box-sizing:border-box}html{scroll-behavior:smooth;-webkit-text-size-adjust:100%;scroll-padding-top:90px}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--font);font-size:17px;line-height:1.6;overflow-x:hidden}
img{max-width:100%;height:auto;display:block}
a{color:var(--ink);text-decoration:none}a:hover{text-decoration:underline;text-decoration-thickness:1.5px;text-underline-offset:3px}
h1,h2,h3{font-family:var(--display);font-weight:700;line-height:1.02;margin:0 0 .5em;letter-spacing:-.025em}
h1{font-size:clamp(2.8rem,7vw,6rem);font-weight:800}h2{font-size:clamp(2rem,4vw,3.2rem)}h3{font-size:1.35rem;letter-spacing:-.015em}
p{margin:0 0 1em}
.wrap{max-width:var(--w);margin:0 auto;padding:0 clamp(18px,4vw,44px)}
.ic{display:inline-flex;width:1.1em;height:1.1em;vertical-align:-.2em}.ic svg{width:100%;height:100%}
.eyebrow{font-weight:600;font-size:.8rem;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);margin-bottom:18px;display:flex;align-items:center;gap:10px}
.eyebrow::before{content:"";width:22px;height:2px;background:var(--accent)}
.lead{font-size:clamp(1.1rem,1.5vw,1.3rem);color:var(--muted);max-width:60ch;line-height:1.55}
section{padding:clamp(64px,8vw,120px) 0}
.dark{background:var(--ink);color:var(--paper)}.dark h2,.dark h3,.dark a{color:var(--paper)}.dark p,.dark .lead{color:#bdb9ad}
.alt{background:var(--paper2)}
.head{display:grid;grid-template-columns:1.1fr 1fr;gap:40px;align-items:end;margin-bottom:clamp(36px,5vw,64px)}
@media(max-width:900px){.head{grid-template-columns:1fr;gap:10px}}
.head .lead{margin:0}
.btn{display:inline-flex;align-items:center;gap:10px;padding:16px 26px;border-radius:999px;font-weight:600;font-size:1rem;border:1.5px solid transparent;transition:.2s;text-decoration:none!important;line-height:1}
.btn .ic{transition:.2s}.btn:hover .ic{transform:translateX(4px)}
.btn-primary{background:var(--accent);color:#fff}.btn-primary:hover{background:var(--accent-dark)}
.btn-ink{background:var(--ink);color:var(--paper)}.btn-ink:hover{background:var(--ink2)}
.btn-ghost{border-color:var(--ink);color:var(--ink)}.btn-ghost:hover{background:var(--ink);color:var(--paper)}
.dark .btn-ghost{border-color:var(--paper);color:var(--paper)}.dark .btn-ghost:hover{background:var(--paper);color:var(--ink)}
/* header */
header{position:sticky;top:0;z-index:50;background:rgba(244,241,234,.88);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
header .wrap{display:flex;align-items:center;justify-content:space-between;height:74px;gap:20px}
.logo{display:flex;align-items:center;gap:12px;text-decoration:none!important}
.logo .mark{width:38px;height:38px;display:block}.logo .mark svg{width:100%;height:100%;display:block}
.logo .word{font-family:var(--display);font-weight:800;font-size:1.5rem;letter-spacing:-.02em;line-height:.9;display:flex;flex-direction:column;align-items:flex-start}
.logo .word small{font-family:var(--font);font-weight:600;font-size:.56rem;letter-spacing:.34em;text-transform:uppercase;color:var(--muted);margin-top:4px;padding-left:.1em}
nav ul{list-style:none;margin:0;padding:0;display:flex;gap:6px;align-items:center}
nav a{padding:10px 14px;font-weight:500;font-size:.98rem;border-radius:999px;text-decoration:none!important}nav a:hover{background:var(--paper2)}
nav li.cta a{background:var(--ink);color:var(--paper);font-weight:600;margin-left:8px}nav li.cta a:hover{background:var(--ink2)}
.burger{display:none;background:none;border:1.5px solid var(--ink);color:var(--ink);width:44px;height:44px;border-radius:50%;align-items:center;justify-content:center;cursor:pointer}
.burger .ic{width:22px;height:22px}
@media(max-width:860px){.burger{display:flex}
nav{position:absolute;top:100%;left:0;right:0;background:var(--paper);border-bottom:1px solid var(--line);display:none;padding:14px 18px 22px;box-shadow:0 20px 40px rgba(0,0,0,.08)}
nav.open{display:block}nav ul{flex-direction:column;align-items:stretch;gap:2px}nav a{display:block;font-size:1.15rem;padding:14px 12px;border-radius:10px}
nav li.cta a{margin:10px 0 0;text-align:center}}
/* hero */
.hero{position:relative;padding:clamp(80px,11vw,160px) 0 clamp(60px,8vw,110px);overflow:hidden}
.hero h1{max-width:14ch;margin-bottom:.35em}.hero h1 .b{display:block;color:var(--accent)}
.hero .lead{max-width:58ch;margin-bottom:36px;font-size:clamp(1.15rem,1.7vw,1.4rem)}
.hero .actions{display:flex;gap:12px;flex-wrap:wrap}
.hero-mark{position:absolute;right:-6%;top:-14%;width:min(46vw,600px);opacity:.06;pointer-events:none}
@media(max-width:900px){.hero-mark{display:none}}
/* why */
.why{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));border:1px solid var(--line);border-radius:var(--r);overflow:hidden;background:#fff}
.why>div{padding:34px 30px 30px;border-left:1px solid var(--line);display:flex;flex-direction:column}.why>div:first-child{border-left:0}
@media(max-width:900px){.why{grid-template-columns:1fr}.why>div{border-left:0;border-top:1px solid var(--line)}.why>div:first-child{border-top:0}}
.why h3{font-size:1.45rem;margin-bottom:.5em}.why h3::before{content:"";display:block;width:26px;height:3px;background:var(--accent);margin-bottom:16px}
.why p{color:var(--muted);margin:0 0 22px;font-size:1rem;flex:1}
.why .fix{font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;font-weight:600;color:var(--faint)}.why .fix b{color:var(--ink);font-weight:600;margin-left:6px}
.why .fix::before{content:"→";margin-right:6px;color:var(--accent)}
/* chain */
.chain{position:relative;display:grid;gap:0}
.chain::before{content:"";position:absolute;left:31px;top:40px;bottom:40px;width:2px;background:var(--line-dark)}
.stepc{display:grid;grid-template-columns:64px minmax(0,1fr);gap:clamp(20px,3vw,40px);padding:clamp(28px,3.5vw,44px) 0;border-bottom:1px solid var(--line-dark);position:relative}
.stepc:last-child{border-bottom:0}
.stepc .n{width:64px;height:64px;border-radius:50%;background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;font-family:var(--display);font-weight:800;font-size:1.5rem;position:relative;z-index:1;letter-spacing:-.02em}
.stepc .body{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:clamp(20px,3vw,50px);align-items:start}
@media(max-width:820px){.stepc .body{grid-template-columns:1fr;gap:12px}}
.stepc h3{font-size:clamp(1.6rem,2.6vw,2.2rem);margin:6px 0 .4em;color:var(--paper)}
.stepc .q{color:#e6e2d8;font-size:1.08rem;margin:0}
.stepc .lbl{font-size:.75rem;letter-spacing:.14em;text-transform:uppercase;font-weight:600;color:var(--accent);margin:8px 0 8px}
.stepc .out{color:#bdb9ad;margin:0 0 16px;font-size:1rem}
.chips{display:flex;flex-wrap:wrap;gap:8px}.chip{border:1px solid var(--line-dark);border-radius:999px;padding:6px 13px;font-size:.85rem;color:#e6e2d8;font-weight:500}
.tools{margin-top:clamp(30px,4vw,50px);padding-top:26px;border-top:1px solid var(--line-dark);color:#8b887f;font-size:.95rem;max-width:70ch}
@media(max-width:560px){.chain::before{left:21px}.stepc{grid-template-columns:44px minmax(0,1fr);gap:16px}.stepc .n{width:44px;height:44px;font-size:1.1rem}}
/* recognize */
.recog{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
@media(max-width:800px){.recog{grid-template-columns:1fr}}
.recog li{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:22px 24px;display:flex;gap:16px;align-items:flex-start;font-size:1.05rem;line-height:1.5}
.recog .ic{flex:none;width:28px;height:28px;color:var(--accent);background:rgba(255,77,26,.1);border-radius:8px;padding:5px;margin-top:2px}
/* thesis */
.thesis{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.2fr);gap:clamp(30px,6vw,90px);align-items:start}
@media(max-width:900px){.thesis{grid-template-columns:1fr}}
.thesis h2{font-size:clamp(2.2rem,4.6vw,3.8rem);position:sticky;top:100px}
@media(max-width:900px){.thesis h2{position:static}}
.thesis p{font-size:clamp(1.05rem,1.4vw,1.2rem);line-height:1.65;color:#d5d1c7;margin-bottom:1.3em}
.thesis p:first-child{color:var(--paper)}
.thesis p strong{color:var(--paper);font-weight:600}
/* deliverables */
.deliv{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}
@media(max-width:800px){.deliv{grid-template-columns:1fr}}
.deliv>div{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:32px 30px}
.deliv .n{font-family:var(--display);font-weight:800;color:var(--accent);font-size:.85rem;letter-spacing:.1em;margin-bottom:14px}
.deliv h3{font-size:1.55rem}.deliv p{color:var(--muted);margin:0}
/* chain on light */
.alt .chain::before,.alt .stepc{border-color:var(--line)}.alt .chain::before{background:var(--line)}
.alt .stepc h3{color:var(--ink)}.alt .stepc .q{color:var(--muted)}.alt .stepc .dur{color:var(--faint)}
.stepc .dur{font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;font-weight:600;color:#8b887f;margin-top:10px}
.alt .tools{border-color:var(--line);color:var(--faint)}
/* models */
.models{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
@media(max-width:900px){.models{grid-template-columns:1fr}}
.model{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:32px 30px}
.model .n{font-size:.78rem;font-weight:600;color:var(--accent);letter-spacing:.12em;text-transform:uppercase;margin-bottom:16px}
.model h3{font-size:1.6rem}.model p{color:var(--muted);margin:0}
.model.hi{background:var(--ink);color:var(--paper);border-color:var(--ink)}.model.hi h3{color:var(--paper)}.model.hi p{color:#bdb9ad}
/* for */
.cols{display:grid;grid-template-columns:1fr 1fr;gap:clamp(30px,5vw,80px);align-items:start}
@media(max-width:860px){.cols{grid-template-columns:1fr}}
.checks{list-style:none;padding:0;margin:0;display:grid;gap:14px}
.checks li{display:flex;gap:14px;align-items:flex-start;font-size:1.08rem}
.checks .ic{flex:none;width:28px;height:28px;color:var(--accent);background:rgba(255,77,26,.1);border-radius:8px;padding:5px;margin-top:1px}
.note{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:28px 30px}
.note h3{font-size:1.2rem}.note p{color:var(--muted);margin:0}
/* founder */
.founder{display:grid;grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr);gap:clamp(30px,5vw,80px);align-items:center}
@media(max-width:900px){.founder{grid-template-columns:1fr}}
.portrait{aspect-ratio:4/5;border-radius:var(--r);background:var(--ink);position:relative;overflow:hidden;display:flex;align-items:flex-end;padding:28px;max-width:440px}
.portrait img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 20%}
.portrait::after{content:"";position:absolute;left:0;right:0;bottom:0;height:45%;background:linear-gradient(180deg,rgba(20,19,15,0),rgba(20,19,15,.85));z-index:1}
.portrait .init{position:absolute;left:28px;top:20px;font-family:var(--display);font-weight:800;font-size:clamp(6rem,14vw,11rem);color:var(--paper);opacity:.08;letter-spacing:-.05em;line-height:1}
.portrait .cap{position:relative;color:var(--paper);z-index:2}.portrait .cap b{display:block;font-family:var(--display);font-size:1.5rem;letter-spacing:-.02em}.portrait .cap span{color:#bdb9ad;font-size:.95rem}
.portrait .dots{position:absolute;right:28px;top:28px;display:flex;gap:10px}.portrait .dots i{width:16px;height:16px;border-radius:50%;background:var(--accent);display:block}
blockquote{margin:0 0 24px;font-family:var(--display);font-size:clamp(1.4rem,2.3vw,2rem);font-weight:600;line-height:1.25;letter-spacing:-.02em}
blockquote::before{content:"“";color:var(--accent)}blockquote::after{content:"”";color:var(--accent)}
.prose p{color:var(--muted);font-size:1.08rem;max-width:62ch}
/* contact */
.contact{background:var(--accent);color:#fff}
.contact .wrap{display:grid;grid-template-columns:1.2fr 1fr;gap:40px;align-items:center}
@media(max-width:900px){.contact .wrap{grid-template-columns:1fr}}
.contact h2{color:#fff;margin-bottom:.3em}.contact p{color:rgba(255,255,255,.88);max-width:52ch;font-size:1.1rem}
.contact .eyebrow{color:#fff}.contact .eyebrow::before{background:#fff}
.contact .actions{display:grid;gap:12px;justify-items:start}
@media(min-width:900px){.contact .actions{justify-items:end}}
.contact .big{font-family:var(--display);font-weight:700;font-size:clamp(1.4rem,2.6vw,2.2rem);color:#fff;letter-spacing:-.02em;text-decoration:none!important;border-bottom:3px solid rgba(255,255,255,.5);padding-bottom:4px}
.contact .big:hover{border-color:#fff}
.contact .btn-ghost{border-color:#fff;color:#fff}.contact .btn-ghost:hover{background:#fff;color:var(--accent)}
/* long-copy helpers */
.hero h1{font-size:clamp(2.3rem,5.2vw,4.4rem);max-width:20ch}
.hero .copy{max-width:64ch}.hero .copy p{font-size:clamp(1.05rem,1.35vw,1.2rem);color:var(--muted);line-height:1.6;margin-bottom:1em}
.hero .copy p.strong{color:var(--ink)}.hero .copy strong{color:var(--ink);font-weight:600}
.q{font-family:var(--display);font-weight:700;letter-spacing:-.02em;line-height:1.15;font-size:clamp(1.5rem,2.6vw,2.2rem);margin:1.1em 0 1.1em;color:var(--ink)}
.q::before{content:"";display:block;width:34px;height:3px;background:var(--accent);margin-bottom:18px}
.dark .q{color:var(--paper)}
.two{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.25fr);gap:clamp(30px,6vw,90px);align-items:start}
@media(max-width:900px){.two{grid-template-columns:1fr}}
.two h2{font-size:clamp(2rem,3.8vw,3.2rem);position:sticky;top:100px}
@media(max-width:900px){.two h2{position:static}}
.prose-l p{font-size:clamp(1.05rem,1.35vw,1.18rem);line-height:1.65;color:var(--muted);margin-bottom:1em;max-width:62ch}
.dark .prose-l p{color:#d5d1c7}
.closing{font-family:var(--display);font-weight:700;font-size:clamp(1.3rem,2.2vw,1.9rem);letter-spacing:-.02em;line-height:1.2;margin-top:1.4em}
.closing span{display:block}.closing .acc{color:var(--accent)}
.recog li{font-size:1.02rem}.recog .ic{color:var(--faint);background:var(--paper2)}
.qa{display:grid;gap:0;border-top:1px solid var(--line);margin-top:10px}
.qa>div{padding:22px 0;border-bottom:1px solid var(--line);display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:24px}
@media(max-width:700px){.qa>div{grid-template-columns:1fr;gap:6px}}
.qa b{font-family:var(--display);font-weight:700;font-size:1.2rem;letter-spacing:-.01em;line-height:1.25}
.qa span{color:var(--muted);font-size:1rem}
.qlist{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:28px 30px}
.qlist h3{font-size:.8rem;letter-spacing:.14em;text-transform:uppercase;font-weight:600;color:var(--accent);margin-bottom:16px}
.qlist ol{margin:0;padding:0;list-style:none;counter-reset:qq}
.qlist li{counter-increment:qq;padding:10px 0 10px 40px;border-top:1px solid var(--line);position:relative;font-size:1.02rem}
.qlist li:first-child{border-top:0}
.qlist li::before{content:counter(qq,decimal-leading-zero);position:absolute;left:0;top:11px;font-family:var(--display);font-weight:800;color:var(--accent);font-size:.85rem;letter-spacing:.05em}
.bigquote{font-family:var(--display);font-weight:700;font-size:clamp(1.6rem,3vw,2.6rem);letter-spacing:-.025em;line-height:1.15;margin:1.2em 0 .6em;max-width:24ch}
.bigquote::before{content:"“";color:var(--accent)}.bigquote::after{content:"”";color:var(--accent)}
.svc{display:grid;gap:0;border-top:1px solid var(--line-dark)}
.svc>div{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:clamp(20px,4vw,60px);padding:clamp(32px,4vw,52px) 0;border-bottom:1px solid var(--line-dark)}
@media(max-width:860px){.svc>div{grid-template-columns:1fr;gap:14px}}
.svc .n{font-family:var(--display);font-weight:800;color:var(--accent);font-size:.9rem;letter-spacing:.12em;margin-bottom:10px}
.svc h3{font-size:clamp(1.6rem,2.6vw,2.2rem);margin:0;color:var(--paper)}
.svc p{color:#bdb9ad;margin:0 0 .9em;font-size:1.02rem;max-width:62ch}
.svc .q{font-size:clamp(1.25rem,2vw,1.6rem);margin:.6em 0 0;color:var(--paper)}.svc .q::before{display:none}
.svc .q{padding-left:18px;border-left:3px solid var(--accent)}
.dl{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 clamp(30px,5vw,70px);border-top:1px solid var(--line)}
@media(max-width:760px){.dl{grid-template-columns:1fr}}
.dl>div{padding:22px 0;border-bottom:1px solid var(--line)}
.dl b{display:block;font-family:var(--display);font-weight:700;font-size:1.25rem;letter-spacing:-.01em;margin-bottom:6px}
.dl b::before{content:"";display:inline-block;width:8px;height:8px;background:var(--accent);border-radius:50%;margin-right:12px;vertical-align:2px}
.dl span{color:var(--muted);font-size:1rem}
.stepc .q{margin:0}.stepc p{color:var(--muted);margin:0 0 .8em;font-size:1.02rem}
.models{grid-template-columns:repeat(2,minmax(0,1fr))}
@media(max-width:760px){.models{grid-template-columns:1fr}}
.model{display:flex;flex-direction:column}.model p{flex:1;margin-bottom:22px}
.model .btn{align-self:flex-start}
.model.hi .btn-ghost{border-color:var(--paper);color:var(--paper)}.model.hi .btn-ghost:hover{background:var(--paper);color:var(--ink)}
.media .checks li{font-size:1.1rem;color:var(--paper)}.media .checks .ic{background:rgba(255,77,26,.18)}
.founder{align-items:start}.founder .portrait{position:sticky;top:100px}
@media(max-width:900px){.founder .portrait{position:static}}
.founder .prose-l p strong{color:var(--ink);font-weight:600}
footer .tag{color:#8b887f;font-size:.9rem;margin-top:10px}
/* form */
.contact .wrap{grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);align-items:start}
.formcard{background:var(--paper);color:var(--ink);border-radius:var(--r);padding:clamp(22px,3vw,34px)}
form.contact-form{display:grid;gap:14px;grid-template-columns:minmax(0,1fr)}
.f2{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:14px}@media(max-width:600px){.f2{grid-template-columns:minmax(0,1fr)}}
.f2>*,form.contact-form>*{min-width:0}
label{display:block;font-size:.85rem;color:var(--muted);margin-bottom:6px;font-weight:600}
input,textarea{width:100%;min-width:0;background:#fff;border:1.5px solid var(--line);color:var(--ink);border-radius:10px;padding:13px 14px;font:inherit;font-size:1rem}
input:focus,textarea:focus{outline:none;border-color:var(--ink);box-shadow:0 0 0 3px rgba(20,19,15,.08)}
textarea{min-height:130px;resize:vertical}
.consent{display:flex;gap:10px;align-items:flex-start;font-size:.88rem;color:var(--muted)}.consent input{width:auto;margin-top:4px}
.consent a{color:var(--ink)}
.hp{position:absolute;left:-9999px}
.contact .alt-mail{margin-top:18px;color:rgba(255,255,255,.85);font-size:.95rem}.contact .alt-mail a{color:#fff;font-weight:600}
/* footer */
footer{background:var(--ink);color:#bdb9ad;padding:44px 0 30px}
footer .wrap{display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap}
footer .logo{color:var(--paper)}footer .logo .word small{color:#8b887f}
footer .meta{display:flex;gap:22px;flex-wrap:wrap;font-size:.9rem}footer a{color:#bdb9ad}footer a:hover{color:var(--paper)}
/* privacy */
.page{padding:clamp(60px,8vw,110px) 0}.page h1{font-size:clamp(2.2rem,5vw,4rem)}.page h2{font-size:1.5rem;margin-top:1.6em}
.reveal{opacity:0;transform:translateY(14px);transition:opacity .6s ease,transform .6s ease}.reveal.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none}}
"""

JS = r"""(function(){
var b=document.querySelector('.burger'),n=document.querySelector('nav');
if(b&&n){b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);});
n.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){n.classList.remove('open');b.setAttribute('aria-expanded',false);});});}
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{rootMargin:'0px 0px -8% 0px'});
document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});}else{document.querySelectorAll('.reveal').forEach(function(el){el.classList.add('in');});}
})();"""

def org_ld():
    d = {"@context": "https://schema.org", "@type": "ProfessionalService", "@id": SITE["domain"] + "/#org", "name": SITE["name"],
         "alternateName": SITE["short"], "url": SITE["domain"] + "/", "logo": SITE["domain"] + "/img/logo.png", "image": SITE["domain"] + "/img/og.png",
         "description": SITE["description"], "email": SITE["email"], "areaServed": "FI", "address": {"@type": "PostalAddress", "addressCountry": "FI"},
         "founder": {"@type": "Person", "name": SITE["founder"], "jobTitle": SITE["founder_title"]},
         "knowsAbout": ["positiointi", "myyntiviestintä", "arvolupaus", "offerin rakentaminen", "copywriting", "mainonnan testaus", "verkkosivut", "Shopify-verkkokaupat"]}
    if SITE.get("linkedin"): d["sameAs"] = [SITE["linkedin"]]
    if SITE.get("ytunnus"): d["vatID"] = "FI" + SITE["ytunnus"].replace("-", "")
    return d

def head(title, desc, path, noindex=False):
    url = SITE["domain"] + path
    return f"""<!DOCTYPE html>
<html lang="fi">
<head>
<meta charset="utf-8">
{'<meta name="robots" content="noindex">' if noindex else ''}
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="{esc(SITE['name'])}"><meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE['domain']}/img/og.png"><meta property="og:locale" content="fi_FI">
<meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#f4f1ea">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon.ico" sizes="any"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">
<script type="application/ld+json">{json.dumps(org_ld(), ensure_ascii=False)}</script>
</head>
<body>
<header><div class="wrap">{logo()}<button class="burger" aria-label="Valikko" aria-expanded="false">{ic('menu')}</button>
<nav aria-label="Päävalikko"><ul>{"".join(f'<li><a href="/{h}">{esc(t)}</a></li>' for t, h in NAV)}<li class="cta"><a href="mailto:{SITE['email']}">Ota yhteyttä</a></li></ul></nav></div></header>
<main>
"""

def footer():
    yt = f"<span>Y-tunnus {SITE['ytunnus']}</span>" if SITE.get("ytunnus") else ""
    li = f'<a href="{SITE["linkedin"]}" target="_blank" rel="noopener">LinkedIn</a>' if SITE.get("linkedin") else ""
    return f"""</main>
<footer><div class="wrap"><div>{logo()}<div class="tag">{esc(FOOTER_LINE)}</div></div><div class="meta"><span>© 2026 {esc(SITE['name'])}</span>{yt}<a href="mailto:{SITE['email']}">{SITE['email']}</a>{li}<a href="/tietosuoja/">Tietosuoja</a></div></div></footer>
<script src="/js/main.js" defer></script>
</body></html>"""

def md(t):
    """**lihavointi** -> <strong>"""
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", esc(t))

def paras(lst, cls=""):
    c = f' class="{cls}"' if cls else ""
    return "".join(f"<p{c}>{md(p)}</p>" for p in lst)

def mailto(subject):
    return f"mailto:{SITE['email']}?subject={subject.replace(' ', '%20')}"

def contact_form():
    return f"""<form class="contact-form" name="yhteys" method="POST" action="/kiitos/" data-netlify="true" netlify-honeypot="bot-field">
<input type="hidden" name="form-name" value="yhteys">
<p class="hp"><label>Älä täytä tätä: <input name="bot-field"></label></p>
<div class="f2"><div><label for="nimi">Nimi *</label><input id="nimi" name="nimi" required autocomplete="name"></div>
<div><label for="yritys">Yritys</label><input id="yritys" name="yritys" autocomplete="organization"></div></div>
<div class="f2"><div><label for="email">Sähköposti *</label><input id="email" type="email" name="email" required autocomplete="email"></div>
<div><label for="www">Verkkosivu</label><input id="www" name="www" placeholder="https://" inputmode="url"></div></div>
<div><label for="viesti">Mitä asiakkaillesi sanot nyt? *</label><textarea id="viesti" name="viesti" required placeholder="Linkki sivustoon, pari mainosta tai muutama lause siitä, mitä myytte ja kenelle."></textarea></div>
<label class="consent"><input type="checkbox" name="suostumus" required> <span>Hyväksyn tietojeni käsittelyn <a href="/tietosuoja/">tietosuojaselosteen</a> mukaisesti.</span></label>
<div><button class="btn btn-ink" type="submit">Lähetä {ic('arrow')}</button></div>
</form>"""

def page_thanks():
    return head("Kiitos viestistäsi | Äijä Group", "Kiitos viestistäsi. Palaamme asiaan pian.", "/kiitos/", noindex=True) + f'<section class="page"><div class="wrap" style="max-width:760px"><div class="eyebrow">Kiitos</div><h1>Viesti tuli perille.</h1><p class="lead">Käyn sen läpi ja palaan asiaan parin arkipäivän sisällä. Kiireellisissä asioissa: <a href="mailto:{SITE["email"]}">{SITE["email"]}</a>.</p><a class="btn btn-ink" href="/" style="margin-top:20px">Takaisin etusivulle {ic("arrow")}</a></div></section>' + footer()

def page_home():
    recog = "".join(f'<li class="reveal">{ic("check")}<span>{esc(x)}</span></li>' for x in RECOGNIZE)
    qa = "".join(f'<div class="reveal"><b>{esc(q)}</b><span>{esc(a)}</span></div>' for q, a in POSITIONING["qa"])
    qs = "".join(f"<li>{esc(q)}</li>" for q in MESSAGE["questions"])
    svc = ""
    for i, (t, ps, q) in enumerate(SERVICES, 1):
        qq = f'<div class="q">{esc(q)}</div>' if q else ""
        svc += f'<div class="reveal"><div><div class="n">0{i}</div><h3>{esc(t)}</h3></div><div>{paras(ps)}{qq}</div></div>'
    dl = "".join(f'<div class="reveal"><b>{esc(t)}</b><span>{esc(x)}</span></div>' for t, x in DELIVERABLES)
    chain = "".join(f'<div class="stepc reveal"><div class="n">{i+1}</div><div class="body"><div><h3>{esc(t)}</h3></div><div>{paras(ps)}</div></div></div>' for i, (t, ps) in enumerate(PROCESS))
    models = "".join(f'<div class="model reveal{" hi" if i == 3 else ""}"><div class="n">0{i+1}</div><h3>{esc(t)}</h3><p>{esc(x)}</p><a class="btn {"btn-ghost" if i == 3 else "btn-ink"}" href="{mailto(subj)}">{esc(cta)} {ic("arrow")}</a></div>' for i, (t, x, cta, subj) in enumerate(MODELS))
    media_list = "".join(f'<li class="reveal">{ic("check")}<span>{esc(x)}</span></li>' for x in MEDIA["list"])
    portrait = f'<img src="/img/sulo-maki.jpg" alt="{esc(SITE["founder"])}" loading="lazy">' if img_exists("sulo-maki.jpg") else '<div class="init">SM</div><div class="dots"><i></i><i></i></div>'
    li = f'<a class="btn btn-ghost" href="{SITE["linkedin"]}" target="_blank" rel="noopener">{ic("linkedin")} LinkedIn</a>' if SITE.get("linkedin") else ""
    return head(TITLE, SITE["description"], "/") + f"""
<section class="hero"><div class="hero-mark">{MARK}</div><div class="wrap">
<div class="eyebrow">{esc(HERO['eyebrow'])}</div>
<h1>{esc(HERO['h1'])}</h1>
<div class="copy">{paras(HERO['p1'])}
<div class="q">{esc(HERO['question'])}</div>
<p class="strong">{esc(HERO['p2_lead'])}<strong>{esc(HERO['p2_bold'])}</strong></p>
{paras(HERO['p3'])}
<div class="actions" style="margin-top:30px"><a class="btn btn-primary" href="{mailto('Nykyinen viestimme')}">{esc(HERO['cta'])} {ic('arrow')}</a><a class="btn btn-ghost" href="#miksi">Lue miksi</a></div>
</div></div></section>

<section id="miksi" class="dark"><div class="wrap"><div class="two">
<div><div class="eyebrow">Miksi</div><h2>{esc(WHY['title'])}</h2></div>
<div class="prose-l reveal">{paras(WHY['p1'])}<div class="q">{esc(WHY['question'])}</div>{paras(WHY['p2'])}
<div class="closing"><span>{esc(WHY['closing'][0])}</span><span class="acc">{esc(WHY['closing'][1])}</span></div></div>
</div></div></section>

<section id="tunnistatko"><div class="wrap">
<div class="head"><div><div class="eyebrow">Tunnistatko tämän?</div><h2>Näin se yleensä näkyy</h2></div>
<p class="lead">{esc(RECOGNIZE_CLOSING)}</p></div>
<ul class="recog">{recog}</ul>
</div></section>

<section class="alt"><div class="wrap"><div class="two">
<div><div class="eyebrow">Positiointi</div><h2>{esc(POSITIONING['title'])}</h2></div>
<div class="prose-l reveal">{paras(POSITIONING['intro'])}<div class="qa">{qa}</div>
<div class="closing" style="font-size:clamp(1.15rem,1.8vw,1.5rem)"><span>{esc(POSITIONING['closing'][0])}</span><span style="color:var(--muted);font-weight:600">{esc(POSITIONING['closing'][1])}</span></div></div>
</div></div></section>

<section><div class="wrap"><div class="two">
<div><div class="eyebrow">Myyntiviesti</div><h2>{esc(MESSAGE['title'])}</h2>
<div class="prose-l" style="margin-top:26px">{paras(MESSAGE['intro'])}</div></div>
<div class="reveal"><div class="qlist"><h3>{esc(MESSAGE['list_title'])}</h3><ol>{qs}</ol></div>
<div class="prose-l" style="margin-top:34px">{paras(MESSAGE['closing'])}</div>
<div class="bigquote">{esc(MESSAGE['quote'])}</div>
<p class="closing" style="margin-top:.4em;font-size:1.3rem;color:var(--accent)">{esc(MESSAGE['after'])}</p></div>
</div></div></section>

<section id="mita" class="dark"><div class="wrap">
<div class="head"><div><div class="eyebrow">Mitä teemme</div><h2>Positiosta valmiiseen viestiin – ja sen toteutukseen</h2></div>
<p class="lead">Viisi asiaa, joissa autamme. Yhden tai kaikki, tilanteen mukaan.</p></div>
<div class="svc">{svc}</div>
</div></section>

<section><div class="wrap">
<div class="head"><div><div class="eyebrow">Lopputulos</div><h2>Mitä projektista jää käteen?</h2></div>
<div class="prose-l">{paras(DELIVERABLES_INTRO)}</div></div>
<div class="dl">{dl}</div>
</div></section>

<section id="miten" class="alt"><div class="wrap">
<div class="head"><div><div class="eyebrow">Näin työskentelemme</div><h2>Nykytilanteesta toimivaan viestiin</h2></div>
<p class="lead">Viisi vaihetta. Järjestys on tärkeä: sanoja ei kannata kirjoittaa ennen kuin tiedetään, mitä niiden pitää saada aikaan.</p></div>
<div class="chain">{chain}</div>
</div></section>

<section id="yhteistyo"><div class="wrap">
<div class="head"><div><div class="eyebrow">Yhteistyö</div><h2>{esc(MODELS_TITLE)}</h2></div></div>
<div class="models">{models}</div>
</div></section>

<section class="dark media"><div class="wrap"><div class="two">
<div><div class="eyebrow">Näkyvyys</div><h2>{esc(MEDIA['title'])}</h2></div>
<div class="prose-l reveal">{paras(MEDIA['p1'])}<ul class="checks" style="margin:10px 0 28px">{media_list}</ul>{paras(MEDIA['p2'])}</div>
</div></div></section>

<section id="meista" class="alt"><div class="wrap"><div class="founder">
<div class="portrait reveal">{portrait}<div class="cap"><b>{esc(SITE['founder'])}</b><span>{esc(SITE['founder_title'])}, Äijä Group Oy</span></div></div>
<div class="prose-l reveal"><div class="eyebrow">Meistä</div><h2>{esc(SITE['founder'])}</h2>{paras(FOUNDER)}
<div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:22px"><a class="btn btn-ink" href="{mailto('Yhteydenotto')}">{ic('mail')} Ota yhteyttä</a>{li}</div></div>
</div></div></section>

<section id="yhteys" class="contact"><div class="wrap">
<div><div class="eyebrow">Yhteys</div><h2>{esc(CONTACT['title'])}</h2>{paras(CONTACT['text'])}
<p class="alt-mail">Tai lähetä suoraan sähköpostilla: <a href="{mailto('Nykyinen viestimme')}">{SITE['email']}</a></p></div>
<div class="formcard reveal">{contact_form()}</div>
</div></section>
""" + footer()

def page_privacy():
    body = "".join(f"<h2>{esc(t)}</h2><p>{esc(x)}</p>" for t, x in PRIVACY)
    return head("Tietosuoja | Äijä Group Oy", "Äijä Group Oy:n tietosuojaseloste.", "/tietosuoja/") + f'<section class="page"><div class="wrap" style="max-width:760px"><h1>Tietosuoja</h1><div class="prose">{body}<p style="font-size:.9rem;color:var(--faint)">Päivitetty 20.9.2026.</p></div></div></section>' + footer()

def page_404():
    return head("Sivua ei löytynyt | Äijä Group", "Sivua ei löytynyt.", "/404.html", noindex=True) + f'<section class="page"><div class="wrap"><h1>Sivua ei löytynyt</h1><p class="lead">Kaikki on etusivulla.</p><a class="btn btn-ink" href="/">Etusivulle {ic("arrow")}</a></div></section>' + footer()

FAVICON = MARK.replace("var(--ink)", "#14130f").replace("var(--accent)", "#ff4d1a").replace("var(--paper)", "#f4f1ea").replace(' aria-hidden="true"', ' xmlns="http://www.w3.org/2000/svg"')

def make_images():
    try:
        from PIL import Image, ImageDraw, ImageFont
    except Exception as e:
        print("PIL puuttuu:", e); return
    INK, ACC, PAP = (20, 19, 15), (255, 77, 26), (244, 241, 234)
    def mark(size):
        im = Image.new("RGBA", (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(im); u = size / 40
        d.rounded_rectangle((0, 0, size, size), radius=9 * u, fill=INK)
        d.ellipse((10 * u, 10 * u, 18 * u, 18 * u), fill=ACC); d.ellipse((22 * u, 10 * u, 30 * u, 18 * u), fill=ACC)
        d.rounded_rectangle((9 * u, 24 * u, 31 * u, 29 * u), radius=2.5 * u, fill=PAP); return im
    mark(512).save(os.path.join(OUT, "img", "logo.png")); mark(180).save(os.path.join(OUT, "apple-touch-icon.png"))
    mark(256).save(os.path.join(OUT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    def font(sz, bold=True):
        local = os.path.join(SRC, "fonts", "BricolageGrotesque-ExtraBold.ttf" if bold else "Inter-Medium.ttf")
        for p in [local, "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf", "/System/Library/Fonts/Helvetica.ttc"]:
            if os.path.exists(p):
                try: return ImageFont.truetype(p, sz)
                except Exception: pass
        return ImageFont.load_default()
    og = Image.new("RGB", (1200, 630), PAP); d = ImageDraw.Draw(og); m = mark(120); og.paste(m, (80, 80), m)
    d.text((80, 250), "Älä osta lisää näkyvyyttä", fill=INK, font=font(60)); d.text((80, 325), "viestille, joka ei vielä myy.", fill=ACC, font=font(60))
    d.text((80, 460), "ÄIJÄ GROUP  ·  " + HERO["eyebrow"].upper(), fill=(92, 90, 84), font=font(28, False))
    og.save(os.path.join(OUT, "img", "og.png"))

def write(path, content):
    full = os.path.join(OUT, path.lstrip("/")); full = os.path.join(full, "index.html") if path.endswith("/") else full
    os.makedirs(os.path.dirname(full), exist_ok=True); open(full, "w", encoding="utf-8").write(content)

def build():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "css")); os.makedirs(os.path.join(OUT, "js")); os.makedirs(os.path.join(OUT, "img"))
    if os.path.isdir(os.path.join(SRC, "img")): shutil.copytree(os.path.join(SRC, "img"), os.path.join(OUT, "img"), dirs_exist_ok=True)  # fontit (src/fonts) vain OG-kuvaan, ei julkaista
    open(os.path.join(OUT, "css", "style.css"), "w").write(CSS); open(os.path.join(OUT, "js", "main.js"), "w").write(JS)
    open(os.path.join(OUT, "favicon.svg"), "w").write(FAVICON); make_images()
    write("/", page_home()); write("/tietosuoja/", page_privacy()); write("/kiitos/", page_thanks()); write("/404.html", page_404())
    open(os.path.join(OUT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>{SITE["domain"]}/</loc><priority>1.0</priority></url>\n  <url><loc>{SITE["domain"]}/tietosuoja/</loc><priority>0.3</priority></url>\n</urlset>\n')
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /kiitos/\nSitemap: {SITE['domain']}/sitemap.xml\n")
    open(os.path.join(OUT, "_redirects"), "w").write("/index.html / 301\n/404.html /404.html 404\n")
    open(os.path.join(OUT, "netlify.toml"), "w").write('[build]\n  publish = "."\n[[headers]]\n  for = "/*"\n  [headers.values]\n    X-Frame-Options = "DENY"\n    X-Content-Type-Options = "nosniff"\n    Referrer-Policy = "strict-origin-when-cross-origin"\n')
    print("OK: 4 sivua ->", OUT)

if __name__ == "__main__":
    build()
