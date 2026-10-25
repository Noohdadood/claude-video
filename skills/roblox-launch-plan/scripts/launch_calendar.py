#!/usr/bin/env python3
"""Print a dated 28-day Roblox launch calendar aligned to RFY's three retention windows.

Pure standard library. Usage:
    python3 launch_calendar.py --launch 2026-11-14 --name "My Game" [--weekly-day Saturday] [--json]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys

WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

SIGNALS = [
    "playtime",
    "play days",
    "qualified play sessions",
    "intentional co-play days (days played with friends)",
    "spend days",
    "Robux spent",
]

PRELAUNCH = [
    (-14, "Lock the icon and first 16:9 thumbnail; test the icon against the live front page."),
    (-14, "Record and submit the gameplay video (real gameplay, no trailer, no narration) so approval lands before launch."),
    (-10, "Build the Day 8 update now. It must be finished before launch week."),
    (-7, "Write the Day 1 first-30-seconds checklist: what the icon promises must happen immediately."),
    (-3, "Set up a Plays ad campaign to seed Recommended for You; leave the Engagement goal off until the threshold is the goal."),
    (-1, "Dry-run with a group of friends: measure time to first fun moment and to first invite moment."),
]


def parse_date(value: str) -> dt.date:
    try:
        return dt.date.fromisoformat(value)
    except ValueError as exc:
        raise SystemExit(f"--launch must be YYYY-MM-DD, got {value!r}") from exc


def shift_to_weekday(day: dt.date, weekday: str | None) -> dt.date:
    if not weekday:
        return day
    target = WEEKDAYS.index(weekday.lower())
    delta = (target - day.weekday()) % 7
    return day + dt.timedelta(days=delta)


def build(launch: dt.date, name: str, weekly_day: str | None) -> dict:
    day = lambda n: launch + dt.timedelta(days=n - 1)  # Day 1 == launch
    windows = [
        {"window": "Window 1 · Day 1", "start": day(1), "end": day(1), "goal": "Icon promise kept in the first 30 seconds; low first-play bounce."},
        {"window": "Window 2 · Days 2–7", "start": day(2), "end": day(7), "goal": "Players come back on more than one day; first co-play moments."},
        {"window": "Window 3 · Days 8–28", "start": day(8), "end": day(28), "goal": "Weekly peaks rise each week; spend days accumulate."},
    ]
    beats = [
        {"day": 1, "date": day(1), "beat": "Launch. Watch the first-30-seconds checklist, not the player count."},
        {"day": 2, "date": day(2), "beat": "First read: first-play bounce rate (<60 s, 61–180 s) and Day 1 retention. Fix the worst drop-off only."},
        {"day": 7, "date": day(7), "beat": "Tease tomorrow's update in-game and on the thumbnail text, not the icon."},
        {"day": 8, "date": day(8), "beat": "Ship the Day 8 update. Include one reason to bring a friend."},
        {"day": 14, "date": shift_to_weekday(day(14), weekly_day), "beat": "Weekly beat 1: small content drop or limited mode."},
        {"day": 21, "date": shift_to_weekday(day(21), weekly_day), "beat": "Weekly beat 2: progression extension plus a recurring, low-price spend reason."},
        {"day": 28, "date": shift_to_weekday(day(28), weekly_day), "beat": "Weekly beat 3 and the 28-day review: compare weekly peaks; plan the next 28 days."},
    ]
    for b in beats:
        b["day"] = (b["date"] - launch).days + 1
    prelaunch = [{"offset_days": off, "date": launch + dt.timedelta(days=off), "task": task} for off, task in PRELAUNCH]
    return {"name": name, "launch": launch, "windows": windows, "prelaunch": prelaunch, "beats": beats, "signals": SIGNALS}


def fmt(d: dt.date) -> str:
    return d.strftime("%a %d %b %Y")


def render(plan: dict) -> str:
    out = [f"# 28-day launch plan: {plan['name']}", "", f"Launch (Day 1): **{fmt(plan['launch'])}**", "",
           "Recommended for You scores each window separately on: " + ", ".join(plan["signals"]) + ".",
           "Only players who arrived through recommendations feed these signals.", "",
           "## Windows", "", "| Window | Dates | Goal |", "|---|---|---|"]
    for w in plan["windows"]:
        dates = fmt(w["start"]) if w["start"] == w["end"] else f"{fmt(w['start'])} → {fmt(w['end'])}"
        out.append(f"| {w['window']} | {dates} | {w['goal']} |")
    out += ["", "## Before launch", "", "| Date | Task | Done |", "|---|---|---|"]
    for p in plan["prelaunch"]:
        out.append(f"| {fmt(p['date'])} (T{p['offset_days']:+d}) | {p['task']} | ☐ |")
    out += ["", "## Beats", "", "| Day | Date | Beat | What ships (fill in) |", "|---|---|---|---|"]
    for b in plan["beats"]:
        out.append(f"| {b['day']} | {fmt(b['date'])} | {b['beat']} | |")
    out += ["", "## Metric per window", "",
            "- Window 1: first-play bounce rate and play-through rate (Creator Hub → Home personalization metrics).",
            "- Window 2: Day 1 and Day 7 retention (Creator Hub → Retention); days played with friends.",
            "- Window 3: weekly peak players, week over week; spend days.", ""]
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--launch", default=dt.date.today().isoformat(), help="Launch date, YYYY-MM-DD (default: today)")
    ap.add_argument("--name", default="Untitled game")
    ap.add_argument("--weekly-day", choices=[w.capitalize() for w in WEEKDAYS] + WEEKDAYS, help="Pin the Day 14/21/28 beats to this weekday (on or after the nominal day)")
    ap.add_argument("--json", action="store_true", help="Emit JSON instead of Markdown")
    args = ap.parse_args(argv)
    plan = build(parse_date(args.launch), args.name, args.weekly_day)
    if args.json:
        json.dump(plan, sys.stdout, indent=1, default=lambda d: d.isoformat())
        print()
    else:
        print(render(plan))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
