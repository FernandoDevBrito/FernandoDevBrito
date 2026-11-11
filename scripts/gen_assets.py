"""Builds the animated SVGs in assets/ for this profile README.

Run: python scripts/gen_assets.py   (Python 3.8+, no dependencies)

Same visual language as the portfolio: #26d970 on #050508, Matrix rain with the
hero3d.js glyphs, diagrams with flowing data streams. SVGs are self-contained:
GitHub serves them through <img>, so no scripts and no web fonts, only inline CSS + SMIL.
"""
import random
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"

ACCENT, BG, PANEL, CARD = "#26d970", "#050508", "#0a0a0f", "#13131a"
TEXT, TEXT2, TEXT3 = "#eef2f7", "#8b99ae", "#738095"
MONO = ("'Cascadia Code','JetBrains Mono','IBM Plex Mono',ui-monospace,'SF Mono',Menlo,"
        "Consolas,'Liberation Mono','DejaVu Sans Mono',monospace")
SANS = ("'IBM Plex Sans','Segoe UI',system-ui,-apple-system,BlinkMacSystemFont,"
        "'Helvetica Neue',Arial,sans-serif")
RAINF = ("'MS Gothic','Yu Gothic','Hiragino Sans','Hiragino Kaku Gothic ProN',"
         "'Noto Sans Mono CJK JP','Noto Sans CJK JP',monospace")
GLYPHS = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン0123456789Z:=*+<>"

CSS_BASE = f"""
.mono{{font-family:{MONO}}}
.sans{{font-family:{SANS}}}
.rain{{font-family:{RAINF}}}
.col{{animation:fall linear infinite}}
.cur{{animation:blink 1.06s steps(1) infinite}}
.pulse{{animation:pulse 2.4s ease-in-out infinite}}
.base{{stroke:#fff;stroke-opacity:.12;stroke-width:2}}
.stream{{stroke:{ACCENT};stroke-width:2.2;stroke-dasharray:8 18;stroke-linecap:round;animation:flow 1.6s linear infinite}}
@keyframes blink{{50%{{opacity:0}}}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.3}}}}
@keyframes flow{{from{{stroke-dashoffset:52}}to{{stroke-dashoffset:0}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
"""

GLOW = """<filter id="glow" x="-20%" y="-60%" width="140%" height="220%">
  <feGaussianBlur in="SourceAlpha" stdDeviation="{b}" result="b"/>
  <feFlood flood-color="#26d970" flood-opacity="{o}"/>
  <feComposite in2="b" operator="in" result="g"/>
  <feMerge><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>"""

GRID = f"""<pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
  <path d="M24 0H0V24" fill="none" stroke="{ACCENT}" stroke-opacity=".05"/>
</pattern>"""


def svg(w, h, title, body, css="", defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{escape(title)}">\n<title>{escape(title)}</title>\n'
            f'<defs>\n<style>{CSS_BASE}{css}</style>\n{defs}\n</defs>\n{body}\n</svg>\n')


def rain(rng, w, h, step=20, fill=0.9):
    """Falling glyph columns at three depths. Each column keeps a random static
    offset (shown when motion is reduced) and a negative delay, so the rain is
    already mid-fall on the first frame."""
    out = []
    for i in range(int(w / step) + 1):
        if rng.random() > fill:
            continue
        x = i * step + step / 2 + rng.uniform(-3, 3)
        depth = rng.choice((0, 0, 1, 1, 1, 2))
        size, op = (13, 16, 20)[depth], (0.5, 0.75, 1)[depth]
        lh = size * 1.3
        n = rng.randint(10, 20)
        dur = rng.uniform(*((13, 18), (9, 13), (6, 9))[depth])
        glyphs = [rng.choice(GLYPHS) for _ in range(n)]
        xs = " ".join([f"{x:.1f}"] * (n - 1))
        ys = " ".join(f"{k * lh:.0f}" for k in range(n - 1))
        mirror = f"matrix(-1 0 0 1 {2 * x:.1f} 0)"  # mirrored like in the film
        static = rng.uniform(-n * lh, h)
        out.append(
            f'<g class="col" transform="translate(0 {static:.0f})" '
            f'style="animation-duration:{dur:.1f}s;animation-delay:-{rng.uniform(0, dur):.1f}s">'
            f'<text class="rain" font-size="{size}" text-anchor="middle" fill="url(#trail)" opacity="{op}" '
            f'transform="{mirror}" x="{xs}" y="{ys}">{escape("".join(glyphs[:-1]))}</text>'
            f'<text class="rain" font-size="{size}" text-anchor="middle" fill="#c9ffdf" opacity="{min(1, op + .1):.2f}" '
            f'transform="{mirror}" x="{x:.1f}" y="{(n - 1) * lh:.0f}">{escape(glyphs[-1])}</text></g>')
    css = f"@keyframes fall{{from{{transform:translateY(-520px)}}to{{transform:translateY({h + 20}px)}}}}"
    trail = (f'<linearGradient id="trail" x1="0" y1="0" x2="0" y2="1">'
             f'<stop offset="0" stop-color="{ACCENT}" stop-opacity="0"/>'
             f'<stop offset=".35" stop-color="{ACCENT}" stop-opacity=".3"/>'
             f'<stop offset=".75" stop-color="{ACCENT}" stop-opacity=".75"/>'
             f'<stop offset="1" stop-color="{ACCENT}" stop-opacity="1"/></linearGradient>')
    return "\n".join(out), css, trail


def typed(x, y, size, prompt, command, begin=0.6, per=0.15):
    """Prompt + command typed once, char by char, through a SMIL clip.
    textLength pins every glyph to a 0.6em cell, so the reveal lines up in any font."""
    cw = size * 0.6
    cx = x + (len(prompt) + 1) * cw
    n = len(command)
    total = begin + per * n + 0.01
    times = ";".join(["0"] + [f"{(begin + per * k) / total:.3f}" for k in range(1, n + 1)])
    widths = ";".join(f"{cw * k + (2 if k == n else 0):.1f}" for k in range(n + 1))
    xs = ";".join(f"{cx + cw * k:.1f}" for k in range(n + 1))
    user, rest = prompt.split(":", 1)
    return f"""<text class="mono" x="{x}" y="{y}" font-size="{size}" textLength="{cw * len(prompt):.1f}" lengthAdjust="spacing"><tspan fill="{ACCENT}">{escape(user)}</tspan><tspan fill="{TEXT2}">:{escape(rest)}</tspan></text>
<clipPath id="typeclip"><rect x="{cx - 1:.1f}" y="{y - size - 4}" height="{size + 12}" width="{cw * n + 2:.1f}"><animate attributeName="width" values="{widths}" keyTimes="{times}" calcMode="discrete" dur="{total:.2f}s" fill="freeze"/></rect></clipPath>
<text class="mono" x="{cx:.1f}" y="{y}" font-size="{size}" fill="{TEXT}" textLength="{cw * n:.1f}" lengthAdjust="spacing" clip-path="url(#typeclip)">{escape(command)}</text>
<rect class="cur" x="{cx + cw * n + 3:.1f}" y="{y - size + 3}" width="{cw - 1:.1f}" height="{size + 1}" fill="{ACCENT}" opacity=".9"><animate attributeName="x" values="{xs}" keyTimes="{times}" calcMode="discrete" dur="{total:.2f}s" fill="freeze"/></rect>"""


# ---------------------------------------------------------------- header
def header():
    w, h = 1200, 400
    cols, rain_css, trail = rain(random.Random(7), w, h)
    defs = f"""{trail}
{GRID}
{GLOW.format(b=9, o=.45)}
<linearGradient id="fade" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity=".1"/><stop offset=".42" stop-color="#fff" stop-opacity=".16"/><stop offset=".64" stop-color="#fff" stop-opacity=".8"/><stop offset="1" stop-color="#fff" stop-opacity="1"/></linearGradient>
<mask id="rainmask"><rect width="{w}" height="{h}" fill="url(#fade)"/></mask>
<radialGradient id="vig" cx=".78" cy=".42" r=".62"><stop offset="0" stop-color="{ACCENT}" stop-opacity=".11"/><stop offset="1" stop-color="{ACCENT}" stop-opacity="0"/></radialGradient>
<linearGradient id="scanband" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{ACCENT}" stop-opacity="0"/><stop offset=".5" stop-color="{ACCENT}" stop-opacity=".07"/><stop offset="1" stop-color="{ACCENT}" stop-opacity="0"/></linearGradient>
<clipPath id="frame"><rect width="{w}" height="{h}" rx="16"/></clipPath>"""
    css = rain_css + ".scan{animation:scan 8s linear infinite}@keyframes scan{from{transform:translateY(-90px)}to{transform:translateY(410px)}}"
    pill_text = "Open to remote roles · Aracaju, Brazil · UTC-3"
    pill_w = 15 * 0.6 * len(pill_text)
    body = f"""<g clip-path="url(#frame)">
<rect width="{w}" height="{h}" fill="{BG}"/>
<rect width="{w}" height="{h}" fill="url(#grid)"/>
<rect width="{w}" height="{h}" fill="url(#vig)"/>
<g mask="url(#rainmask)">
{cols}
</g>
<rect class="scan" y="0" width="{w}" height="90" fill="url(#scanband)"/>
{typed(72, 112, 22, "fernando@brito:~$", "whoami")}
<text class="sans" x="69" y="214" font-size="84" font-weight="700" letter-spacing="-1.5" fill="{TEXT}" filter="url(#glow)">Fernando Brito</text>
<text class="mono" x="72" y="264" font-size="26" fill="{ACCENT}">Full Stack Software Developer</text>
<text class="mono" x="72" y="303" font-size="18" fill="{TEXT2}">.NET · C# · Angular · React · SQL Server · AI-assisted dev</text>
<rect x="72" y="330" width="{pill_w + 54:.0f}" height="36" rx="18" fill="{ACCENT}" fill-opacity=".08" stroke="{ACCENT}" stroke-opacity=".4"/>
<circle class="pulse" cx="92" cy="348" r="5" fill="{ACCENT}"/>
<text class="mono" x="108" y="353" font-size="15" fill="{TEXT}" textLength="{pill_w:.0f}" lengthAdjust="spacing">{escape(pill_text)}</text>
<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="15.5" fill="none" stroke="{ACCENT}" stroke-opacity=".25"/>
</g>"""
    return svg(w, h, "Fernando Brito, Full Stack Software Developer", body, css, defs)


# ---------------------------------------------------------------- impact
def impact():
    tiles = [("4+", "Years in production", "nationwide B2B ERP"),
             ("50k+", "Transactions a month", "bank reconciliation"),
             ("10k+", "E-invoices a month", "SEFAZ tax integration"),
             ("1M+", "Records migrated", "legacy DBs → SQL Server")]
    tw, gap, th = 279, 28, 196
    defs = f"""{GLOW.format(b=6, o=.5)}
<linearGradient id="topline" x1="0" x2="1"><stop offset="0" stop-color="{ACCENT}" stop-opacity="0"/><stop offset=".5" stop-color="{ACCENT}" stop-opacity=".9"/><stop offset="1" stop-color="{ACCENT}" stop-opacity="0"/></linearGradient>"""
    parts = []
    for i, (num, label, sub) in enumerate(tiles):
        x = i * (tw + gap)
        parts.append(f"""<g transform="translate({x} 2)">
<rect x=".5" y=".5" width="{tw - 1}" height="{th - 1}" rx="16" fill="{CARD}" stroke="{ACCENT}" stroke-opacity=".2"/>
<rect x="24" y="0" width="{tw - 48}" height="2" fill="url(#topline)"/>
<text class="sans" x="28" y="92" font-size="58" font-weight="700" fill="{ACCENT}" filter="url(#glow)">{escape(num)}</text>
<text class="sans" x="28" y="134" font-size="19" font-weight="600" fill="{TEXT}">{escape(label)}</text>
<text class="mono" x="28" y="164" font-size="14" fill="{TEXT2}">{escape(sub)}</text>
</g>""")
    return svg(1200, 200, "Impact: 4+ years in production, 50k+ transactions a month, 10k+ e-invoices a month, 1M+ records migrated",
               "\n".join(parts), "", defs)


# ---------------------------------------------------------------- shared diagram bits
def arrow(x1, x2, y):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2 - 8}" y2="{y}" class="base"/>'
            f'<line x1="{x1}" y1="{y}" x2="{x2 - 8}" y2="{y}" class="stream" filter="url(#soft)"/>'
            f'<polygon points="{x2 - 9},{y - 6} {x2},{y} {x2 - 9},{y + 6}" fill="{ACCENT}"/>')


def down_arrow(x, y1, y2):
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2 - 8}" class="base"/>'
            f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2 - 8}" class="stream" filter="url(#soft)"/>'
            f'<polygon points="{x - 6},{y2 - 9} {x},{y2} {x + 6},{y2 - 9}" fill="{ACCENT}"/>')


SOFT = """<filter id="soft" x="-20%" y="-200%" width="140%" height="500%"><feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>"""


def box(x, y, w, h, lines, strong=False, rx=8):
    """lines[0] is the bold title (accent), the rest are dim sub-lines."""
    sw, op = ("1.8", "1") if strong else ("1.2", ".6")
    cx = x + w / 2
    n = len(lines)
    title_y = y + h / 2 + 6 - (n - 1) * 11
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{PANEL}" stroke="{ACCENT}" stroke-width="{sw}" stroke-opacity="{op}"/>']
    for k, line in enumerate(lines):
        if k == 0:
            out.append(f'<text class="mono" x="{cx}" y="{title_y:.0f}" font-size="16" font-weight="700" fill="{ACCENT}" text-anchor="middle">{escape(line)}</text>')
        else:
            out.append(f'<text class="mono" x="{cx}" y="{title_y + 6 + k * 20:.0f}" font-size="14" fill="{TEXT3}" text-anchor="middle">{escape(line)}</text>')
    return "\n".join(out)


# ---------------------------------------------------------------- Lonerchestrator
def lonerchestrator():
    w, h = 1200, 330
    stages = [("SPLIT", "splitter", False), ("PLAN", "planner", False), ("BUILD", "builder", True),
              ("CHECKS", "rules + CI", True), ("REVIEW", "qa + cross", True), ("MERGE", "git + retro", False)]
    bw, gap, top, bh = 136, 38, 108, 100
    cy = top + bh / 2
    x0 = 154
    parts = [f'<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="16" fill="{PANEL}" stroke="{ACCENT}" stroke-opacity=".22"/>',
             f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="15" fill="url(#grid)"/>',
             f'<text class="mono" x="32" y="46" font-size="15" fill="{TEXT3}"><tspan fill="{ACCENT}">●</tspan> lonerchestrator · card pipeline</text>',
             f'<text class="mono" x="{w - 32}" y="46" font-size="15" fill="{TEXT3}" text-anchor="end">Python · MIT · runs locally</text>',
             f'<rect x="40" y="{cy - 20}" width="78" height="40" rx="20" fill="{PANEL}" stroke="{TEXT3}" stroke-opacity=".8"/>',
             f'<text class="mono" x="79" y="{cy + 6}" font-size="17" fill="{TEXT2}" text-anchor="middle">card</text>',
             arrow(118, x0, cy)]
    centers = []
    for i, (name, who, strong) in enumerate(stages):
        x = x0 + i * (bw + gap)
        centers.append(x + bw / 2)
        sw, op = ("1.8", "1") if strong else ("1.2", ".6")
        parts.append(f'<rect x="{x}" y="{top}" width="{bw}" height="{bh}" rx="10" fill="{PANEL}" stroke="{ACCENT}" stroke-width="{sw}" stroke-opacity="{op}"/>')
        parts.append(f'<text class="mono" x="{x + bw / 2}" y="{cy - 4}" font-size="19" font-weight="700" fill="{ACCENT}" text-anchor="middle">{name}</text>')
        parts.append(f'<text class="mono" x="{x + bw / 2}" y="{cy + 22}" font-size="15" fill="{TEXT3}" text-anchor="middle">{escape(who)}</text>')
        if i < len(stages) - 1:
            parts.append(arrow(x + bw, x + bw + gap, cy))
    build, review = centers[2], centers[4]
    loop_y = top + bh + 34
    parts.append(f'<path d="M{review} {top + bh} V{loop_y} H{build} V{top + bh + 9}" fill="none" class="base"/>')
    parts.append(f'<path d="M{review} {top + bh} V{loop_y} H{build} V{top + bh + 9}" fill="none" class="stream" stroke-opacity=".75" filter="url(#soft)"/>')
    parts.append(f'<polygon points="{build - 6},{top + bh + 10} {build},{top + bh + 1} {build + 6},{top + bh + 10}" fill="{ACCENT}"/>')
    parts.append(f'<text class="mono" x="{centers[3]}" y="{loop_y + 26}" font-size="14" fill="{TEXT2}" text-anchor="middle">fix · 3 attempts max, then NEEDS YOU</text>')
    parts.append(f'<text class="mono" x="{w / 2}" y="{h - 22}" font-size="14" fill="{TEXT3}" text-anchor="middle">guardrails in code, not prompts · whoever builds never reviews · never deploys</text>')
    return svg(w, h, "Lonerchestrator pipeline: card, split, plan, build, checks, review, merge, with a fix loop from review back to build",
               "\n".join(parts), "", f"{GRID}\n{SOFT}")


# ---------------------------------------------------------------- project cards
def wrap(text, width):
    lines, cur = [], ""
    for word in text.split():
        if cur and len(cur) + 1 + len(word) > width:
            lines.append(cur)
            cur = word
        else:
            cur = f"{cur} {word}".strip()
    return lines + [cur]


def flow(left, middle, rights, bottom=None):
    """Three-stage diagram for a 600-wide panel: left box → middle box → one or two right boxes."""
    lx, lw, mx, mw, rx_, rw = 32, 120, 198, 196, 440, 128
    cy = 96
    mh = 34 + 20 * len(middle)
    parts = [box(lx, cy - 35, lw, 70, left), arrow(lx + lw, mx, cy),
             box(mx, cy - mh / 2, mw, mh, middle, strong=True)]
    if len(rights) == 1:
        parts += [arrow(mx + mw, rx_, cy), box(rx_, cy - 35, rw, 70, rights[0])]
    else:
        for k, r in enumerate(rights):
            y = cy - 50 + k * 58
            parts += [arrow(mx + mw, rx_, y + 21), box(rx_, y, rw, 42, r, rx=6)]
    if bottom:
        parts += [down_arrow(mx + mw / 2, cy + mh / 2, 178),
                  f'<text class="mono" x="{mx + mw / 2}" y="196" font-size="14" fill="{TEXT2}" text-anchor="middle">{escape(bottom)}</text>']
    return "\n".join(parts)


def card(eyebrow, title, desc, chips, diagram, alt):
    w, h, ph = 600, 410, 206
    lines = wrap(desc, 50)  # 50 chars keeps wide fallback fonts (DejaVu, Verdana) inside 536px
    assert len(lines) <= 3, (title, lines)
    out = [f'<clipPath id="cardclip"><rect width="{w}" height="{h}" rx="16"/></clipPath>']
    body = [f'<g clip-path="url(#cardclip)">',
            f'<rect width="{w}" height="{h}" fill="{CARD}"/>',
            f'<rect width="{w}" height="{ph}" fill="{PANEL}"/>',
            f'<rect width="{w}" height="{ph}" fill="url(#grid)"/>',
            f'<line x1="0" y1="{ph}" x2="{w}" y2="{ph}" stroke="#fff" stroke-opacity=".06"/>',
            diagram,
            f'<text class="mono" x="32" y="240" font-size="13" letter-spacing="1.4" fill="{ACCENT}">{escape(eyebrow)}</text>',
            f'<text class="sans" x="32" y="274" font-size="26" font-weight="700" fill="{TEXT}">{escape(title)}</text>']
    for k, line in enumerate(lines):
        body.append(f'<text class="sans" x="32" y="{306 + k * 23}" font-size="16.5" fill="{TEXT2}">{escape(line)}</text>')
    x = 32
    for chip in chips:
        cw = len(chip) * 7.8 + 20
        body.append(f'<rect x="{x}" y="372" width="{cw:.0f}" height="26" rx="6" fill="#fff" fill-opacity=".04" stroke="{ACCENT}" stroke-opacity=".25"/>'
                    f'<text class="mono" x="{x + cw / 2:.0f}" y="390" font-size="13" fill="{TEXT}" text-anchor="middle">{escape(chip)}</text>')
        x += cw + 8
    assert x <= w - 24, (title, x)
    body += [f'<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="15.5" fill="none" stroke="{ACCENT}" stroke-opacity=".2"/>', "</g>"]
    return svg(w, h, alt, "\n".join(body), "", "\n".join([GRID, SOFT] + out))


CARDS = {
    "card-legacy.svg": card(
        "FULL STACK · AI · PRODUCTION", "Legacy Modernization with AI",
        "Moving a DP Sistemas system from .NET Framework 4 and WebForms to .NET 10 and React, with AI agents and human review of every change.",
        ["C#", ".NET 10", "React", "CI/CD", "AI agents"],
        flow([".NET 4", "WebForms"], ["AI Agents", "Implement", "Code review", "Human review"], [[".NET 10", "React"]], "Lint + CI/CD"),
        "Legacy Modernization with AI: .NET Framework 4 and WebForms to .NET 10 and React, with AI agents and human review of every change"),
    "card-etl.svg": card(
        "BACKEND · DATA · PRODUCTION", "ERP Data Migration",
        "C# and Python ETL that moved 1M+ records from PostgreSQL, Oracle, MariaDB and Firebird into one SQL Server with 100% referential integrity.",
        ["C#", "Python", "SQL Server", "PostgreSQL", "Oracle"],
        flow(["Legacy DBs", "4 engines"], ["C# / Python ETL", "Validate", "Transform", "Load"], [["SQL Server", "Unified ERP"]], "Integrity checks"),
        "ERP Data Migration: C# and Python ETL that moved 1M+ records from four legacy databases into SQL Server with 100% referential integrity"),
    "card-sefaz.svg": card(
        "FULL STACK · .NET & ANGULAR · PRODUCTION", "SEFAZ Fiscal Hub",
        "Angular dashboard and C# / .NET XML engine connected to SEFAZ web services, processing 10k+ e-invoices (NF-e) a month.",
        ["Angular", "TypeScript", "C#", ".NET", "SQL Server"],
        flow(["Angular SPA", "Dashboard UI"], ["ASP.NET Core", "XML & REST engine", "Auth · Validation", "10k+ NF-e / month"], [["SEFAZ"], ["SQL Server"]]),
        "SEFAZ Fiscal Hub: Angular dashboard and C# .NET XML engine processing 10k+ e-invoices a month through SEFAZ web services"),
    "card-uk.svg": card(
        "BACKEND · ANALYTICS · LIVE DEMO", "UK Police Analytics API",
        "Async FastAPI service that consumes the official UK Police API, aggregates crime data with Pandas and maps it on a Leaflet dashboard.",
        ["Python", "FastAPI", "HTTPX", "Pandas"],
        flow(["Police API"], ["FastAPI", "HTTPX async", "Pandas engine", "GeoJSON"], [["Dashboard UI", "Leaflet map"]]),
        "UK Police Analytics API: async FastAPI service that aggregates UK Police crime data with Pandas and maps it on a Leaflet dashboard"),
}


# ---------------------------------------------------------------- footer
def footer():
    w, h = 1200, 130
    cols, rain_css, trail = rain(random.Random(11), w, h, step=22, fill=0.8)
    prompt, cmd = "fernando@brito:~$", 'echo "thanks for stopping by"'
    size = 20
    total_w = size * 0.6 * (len(prompt) + 1 + len(cmd))
    x = (w - total_w) / 2
    defs = f"""{trail}
<linearGradient id="fadev" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff" stop-opacity=".75"/></linearGradient>
<mask id="rainmask"><rect width="{w}" height="{h}" fill="url(#fadev)"/></mask>
<clipPath id="frame"><rect width="{w}" height="{h}" rx="16"/></clipPath>"""
    body = f"""<g clip-path="url(#frame)">
<rect width="{w}" height="{h}" fill="{BG}"/>
<g mask="url(#rainmask)">
{cols}
</g>
{typed(round(x, 1), 74, size, prompt, cmd, begin=0.8, per=0.06)}
<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="15.5" fill="none" stroke="{ACCENT}" stroke-opacity=".2"/>
</g>"""
    return svg(w, h, 'fernando@brito:~$ echo "thanks for stopping by"', body, rain_css, defs)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    files = {"header.svg": header(), "impact.svg": impact(), "lonerchestrator.svg": lonerchestrator(),
             "footer.svg": footer(), **CARDS}
    for name, content in files.items():
        (OUT / name).write_text(content, encoding="utf-8")
        print(f"{name:22} {len(content.encode()) / 1024:6.1f} KB")
