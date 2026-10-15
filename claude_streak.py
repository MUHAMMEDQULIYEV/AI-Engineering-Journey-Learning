#!/usr/bin/env python3
"""Claude Code streak page: yearly heatmap + Total, Longest and Current Streak.

Reads ~/.claude/history.jsonl (one line per prompt you typed), counts prompts
per local day, writes ~/claude_streak.html and opens it in the browser.
"""
import html
import json
import sys
import webbrowser
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path

HISTORY = Path.home() / ".claude" / "history.jsonl"
OUT = Path.home() / "claude_streak.html"


def load_counts():
    counts = Counter()
    if not HISTORY.exists():
        return counts
    for line in HISTORY.open(encoding="utf-8", errors="replace"):
        try:
            ts = json.loads(line).get("timestamp")
        except json.JSONDecodeError:
            continue
        if isinstance(ts, (int, float)):
            counts[datetime.fromtimestamp(ts / 1000).date()] += 1
    return counts


def streaks(days, today):
    """Return (longest, longest_start, longest_end, current, current_start)."""
    longest = (0, None, None)
    run_start, prev = None, None
    for d in sorted(days):
        if prev is None or d != prev + timedelta(days=1):
            run_start = d
        length = (d - run_start).days + 1
        if length > longest[0]:
            longest = (length, run_start, d)
        prev = d
    # Current streak may end today or yesterday (today not used yet).
    end = today if today in days else today - timedelta(days=1)
    current, d = 0, end
    while d in days:
        current += 1
        d -= timedelta(days=1)
    current_start = d + timedelta(days=1) if current else None
    return (*longest, current, current_start)


def fmt(d):
    return d.strftime("%b %-d, %Y") if d else "—"


def level(n, peak):
    if n == 0:
        return 0
    return min(4, 1 + int(3 * n / peak)) if peak > 1 else 4


def build(counts, today):
    start = today - timedelta(days=364)
    start -= timedelta(days=(start.weekday() + 1) % 7)  # back to Sunday
    peak = max([counts[d] for d in counts if d >= start] or [1])

    cells, months, col, d = [], [], 0, start
    last_month = None
    while d <= today:
        if d.weekday() == 6:  # Sunday starts a new column
            col += 1
            if d.month != last_month:
                months.append(f'<span style="grid-column:{col}">{d:%b}</span>')
                last_month = d.month
        row = (d.weekday() + 1) % 7 + 1
        n = counts.get(d, 0)
        tip = f"{n} prompt{'s' * (n != 1)} on {fmt(d)}"
        cells.append(
            f'<i class="l{level(n, peak)}" style="grid-column:{col};grid-row:{row}" '
            f'title="{html.escape(tip)}"></i>'
        )
        d += timedelta(days=1)

    days = {d for d, n in counts.items() if n}
    total = sum(counts.values())
    first = min(days) if days else None
    lg, lg_s, lg_e, cur, cur_s = streaks(days, today)
    cur_e = (today if today in days else today - timedelta(days=1)) if cur else None

    def stat(value, label, sub):
        return f'<div class="stat"><b>{value}</b><span>{label}</span><small>{sub}</small></div>'

    stats = "".join([
        stat(f"{total:,}", "Total prompts", f"{fmt(first)} – Present"),
        stat(f"{cur} day{'s' * (cur != 1)}", "Current Streak",
             f"{fmt(cur_s)} – {fmt(cur_e)}" if cur else "Start one today"),
        stat(f"{lg} day{'s' * (lg != 1)}", "Longest Streak",
             f"{fmt(lg_s)} – {fmt(lg_e)}" if lg else "—"),
    ])

    return f"""<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Claude Code Streak</title>
<style>
:root {{ --bg:#fff; --fg:#1f2328; --muted:#59636e; --border:#d1d9e0;
  --l0:#eff2f5; --l1:#f5d6c6; --l2:#eba98a; --l3:#d97757; --l4:#a8492b; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg:#0d1117; --fg:#e6edf3; --muted:#9198a1;
  --border:#3d444d; --l0:#151b23; --l1:#4a2a1d; --l2:#7a3f27; --l3:#c0603c; --l4:#f0956d; }} }}
body {{ margin:0; padding:32px 16px; background:var(--bg); color:var(--fg);
  font:14px/1.4 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }}
.card {{ max-width:900px; margin:auto; border:1px solid var(--border); border-radius:8px; padding:20px; }}
h1 {{ font-size:16px; margin:0 0 16px; font-weight:600; }}
.scroll {{ overflow-x:auto; }}
.months, .grid {{ display:grid; grid-template-columns:repeat(54,12px); gap:3px; }}
.months {{ color:var(--muted); font-size:11px; margin-bottom:4px; }}
.grid {{ grid-template-rows:repeat(7,12px); grid-auto-flow:column; }}
.grid i {{ width:12px; height:12px; border-radius:2px; background:var(--l0); }}
.l1 {{ background:var(--l1)!important }} .l2 {{ background:var(--l2)!important }}
.l3 {{ background:var(--l3)!important }} .l4 {{ background:var(--l4)!important }}
.stats {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
  margin-top:20px; border-top:1px solid var(--border); }}
.stat {{ display:flex; flex-direction:column; align-items:center; padding:16px 8px; text-align:center; }}
.stat b {{ font-size:26px; }} .stat small {{ color:var(--muted); }}
</style></head><body><div class="card">
<h1>Claude Code activity in the last year</h1>
<div class="scroll"><div class="months">{''.join(months)}</div>
<div class="grid">{''.join(cells)}</div></div>
<div class="stats">{stats}</div>
</div></body></html>"""


def main():
    today = date.today()
    OUT.write_text(build(load_counts(), today), encoding="utf-8")
    print(f"Saved {OUT}")
    if "--no-open" not in sys.argv:
        webbrowser.open(OUT.as_uri())


if __name__ == "__main__":
    main()
