#!/usr/bin/env python3
"""Roblox Kids and Select threshold calculator (pure standard library).

Usage:
    python3 eligibility.py --hep 140 [--status in|out] [--date 2026-10-25] [--daily-hep 3] [--json]
    python3 eligibility.py --list-thresholds

Thresholds are unique plays by highly engaged, age-checked users in a rolling 60-day window.
Update SCHEDULE when Roblox announces a change; each entry is (effective date, entry bar, maintenance bar, source note).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys

SCHEDULE = [
    (dt.date(2026, 6, 1), 500, 100, "Kids and Select global launch (official)"),
    (dt.date(2026, 7, 16), 500, 25, "maintenance bar lowered to 25 (official)"),
    (dt.date(2026, 8, 19), 250, 25, "entry bar lowered to 250 (official)"),
    (dt.date(2026, 11, 1), 100, 25, "entry bar to 100, 'November 2026' per Bloxy News; exact day unconfirmed"),
]
WINDOW_DAYS = 60


def thresholds_on(day: dt.date):
    current = SCHEDULE[0]
    for entry in SCHEDULE:
        if entry[0] <= day:
            current = entry
    return current


def next_change_after(day: dt.date):
    for entry in SCHEDULE:
        if entry[0] > day:
            return entry
    return None


def assess(hep: int, status: str, day: dt.date, daily_hep: float | None) -> dict:
    eff, entry, maint, note = thresholds_on(day)
    bar = maint if status == "in" else entry
    gap = max(0, bar - hep)
    result = {
        "date": day.isoformat(),
        "status": status,
        "hep_last_60_days": hep,
        "rules_effective": eff.isoformat(),
        "rules_note": note,
        "entry_threshold": entry,
        "maintenance_threshold": maint,
        "applicable_threshold": bar,
        "gap": gap,
        "meets_threshold": gap == 0,
        "verdict": "",
        "projection": None,
        "next_change": None,
        "waiting_is_faster": None,
    }
    if gap == 0:
        result["verdict"] = ("Eligible and above the maintenance bar." if status == "in"
                             else "Meets the entry bar; evaluation should complete and unlock Kids and Select audiences.")
    else:
        result["verdict"] = (f"Below the {'maintenance' if status == 'in' else 'entry'} bar by {gap} highly engaged plays"
                             f" (rolling {WINDOW_DAYS}-day window).")
    if daily_hep and daily_hep > 0 and gap > 0:
        days = -(-gap // daily_hep)  # ceil
        result["projection"] = {"daily_hep": daily_hep, "days_to_cross": int(days), "date": (day + dt.timedelta(days=int(days))).isoformat()}
    nxt = next_change_after(day)
    if nxt:
        nxt_bar = nxt[2] if status == "in" else nxt[1]
        result["next_change"] = {"date": nxt[0].isoformat(), "entry_threshold": nxt[1], "maintenance_threshold": nxt[2],
                                 "applicable_threshold": nxt_bar, "note": nxt[3], "already_meets_it": hep >= nxt_bar}
        if result["projection"]:
            result["waiting_is_faster"] = hep >= nxt_bar and dt.date.fromisoformat(result["projection"]["date"]) > nxt[0]
    return result


def render(r: dict) -> str:
    lines = [f"Roblox Kids and Select check for {r['date']} (rules from {r['rules_effective']}: {r['rules_note']})", "",
             f"Highly engaged plays, last {WINDOW_DAYS} days: {r['hep_last_60_days']}",
             f"Entry bar: {r['entry_threshold']} · Maintenance bar: {r['maintenance_threshold']} · Applies to you ({'already eligible' if r['status']=='in' else 'not yet eligible'}): {r['applicable_threshold']}",
             "", r["verdict"]]
    if r["projection"]:
        p = r["projection"]
        lines.append(f"At {p['daily_hep']} new highly engaged plays/day you cross in about {p['days_to_cross']} days, around {p['date']}.")
    if r["next_change"]:
        n = r["next_change"]
        lines.append(f"Next scheduled change: {n['date']} → entry {n['entry_threshold']}, maintenance {n['maintenance_threshold']} ({n['note']}).")
        if n["already_meets_it"] and not r["meets_threshold"]:
            lines.append("You already meet that future bar; if nothing changes you become eligible when it takes effect.")
        if r["waiting_is_faster"]:
            lines.append("Waiting for the scheduled drop is faster than the organic projection.")
    if not r["meets_threshold"]:
        lines += ["", "Routes: keep growing organically; run an Ads Manager campaign with the Engagement goal (higher cost per play, pause it yourself once you cross);",
                  "or request the paid, refundable Expedited Review (up to 48 h) if a launch window matters more than the fee."]
    lines.append("Confirm current thresholds in Creator Hub → Roblox Kids and Select if this is being read after January 2027.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--hep", type=int, help="Unique highly engaged plays in the last 60 days (Audience Reach dashboard)")
    ap.add_argument("--status", choices=["in", "out"], default="out", help="Currently eligible for Kids and Select? (default: out)")
    ap.add_argument("--date", default=dt.date.today().isoformat(), help="Date to evaluate, YYYY-MM-DD (default: today)")
    ap.add_argument("--daily-hep", type=float, help="Average new highly engaged plays per day, for a projection")
    ap.add_argument("--list-thresholds", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    if args.list_thresholds:
        for eff, entry, maint, note in SCHEDULE:
            print(f"{eff.isoformat()}  entry {entry:>4}  maintenance {maint:>4}  {note}")
        return 0
    if args.hep is None:
        ap.error("--hep is required (or use --list-thresholds)")
    try:
        day = dt.date.fromisoformat(args.date)
    except ValueError:
        ap.error("--date must be YYYY-MM-DD")
    r = assess(args.hep, args.status, day, args.daily_hep)
    if args.json:
        json.dump(r, sys.stdout, indent=1)
        print()
    else:
        print(render(r))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
