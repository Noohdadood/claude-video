---
name: roblox-launch-plan
description: Build a dated 28-day launch or relaunch plan for a Roblox game that matches how Recommended for You now scores retention (Day 1, Days 2–7, Days 8–28 judged separately), with the Day 8 update planned before launch and a reason to return in every window. Use this whenever a Roblox developer mentions launching, releasing, relaunching, soft-launching or updating a game, asks what to ship after launch, asks for a content roadmap or update schedule, or wants to know how to keep players coming back, even if they do not mention the algorithm.
license: MIT
allowed-tools: Bash, Read, AskUserQuestion
metadata:
  version: "0.1.0"
  derived-from: "The new rules of the Roblox algorithm (youtube.com/watch?v=RC19PKdRt1Y), fact-checked against Roblox announcements, Oct 2026"
---

# Roblox 28-day launch plan

Since June 2026 Roblox's Home recommendations judge a game's first 28 days in three windows: Day 1, Days 2–7 and Days 8–28. Each window measures playtime, play days, play sessions, days played with friends, spend days and Robux spent for players who arrived through recommendations. A huge Day 1 no longer carries a game; a game that gives people a reason to return in every window outranks one that spiked once. This skill turns a launch date into a dated plan built around that scoring.

## Steps

1. **Pin the facts.** Launch date (or the date of the relaunch update), genre, session length, whether the game is better with friends, and what content is already finished. Ask once for anything missing; otherwise state assumptions in the plan.
2. **Generate the calendar.** `SKILL_DIR` is the directory containing this file.

   ```bash
   python3 "${SKILL_DIR}/scripts/launch_calendar.py" --launch 2026-11-14 --name "Shop Tycoon"
   ```

   The script prints a Markdown skeleton: the three windows with real dates, the pre-launch checklist, and one dated slot per beat (Day 1, Day 2 read, Day 7 teaser, Day 8 update, Days 14, 21 and 28). Add `--json` for machine-readable output or `--weekly-day Saturday` to pin the weekly beats to a weekday.
3. **Fill every slot with something concrete** for this game. "Update" is not a plan; "Day 8: second biome with a new tool that only drops when two players dig together" is. Keep each beat small enough to ship and honest enough to put on the icon.
4. **Check the plan against the four traps** below and revise.
5. **Deliver** the filled plan plus a three-line summary: the Day 8 beat, the weekly beat, and the one metric to watch each window.

## What makes a beat work

- **Day 1 is the promise test.** Players bounce in the first 60 seconds when the icon oversells. The Day 1 slot is for making the first 30 seconds match the icon, not for a launch party.
- **Day 2 is the first honest read.** Look at first-play bounce rate and Day 1 retention in Creator Hub (Retention, Home personalization metrics) before changing anything else.
- **Day 7 teases, Day 8 ships.** Window two ends on Day 7. Something new arriving on Day 8 gives window three a reason to exist. Plan it before launch, because it must be built while Day 1 is being polished.
- **Weekly beats in Days 8–28.** Three weekly reasons to return (Days 14, 21, 28) keep the slope positive. Weekly peaks that rise each week are the pattern recommendations reward; the creator explainer's "who's winning" examples all looked like this.
- **Co-play is a multiplier.** Days played with friends is its own signal, and friends chat now follows players between games. Put one invite moment into the Day 8 or Day 14 beat.
- **Spend days count, Robux counts.** A cheap, recurring reason to spend across days beats one big launch bundle.

## Four traps

1. **The spike.** Events that pull a crowd for one weekend show up as a spike followed by decay in all three windows. Prefer smaller beats that compound.
2. **The silent Day 8.** Shipping nothing between Day 2 and Day 14 wastes window three entirely.
3. **The moving icon.** Changing the icon to chase clicks mid-plan breaks the promise test and raises bounce.
4. **Paid cover.** Ads keep concurrency up while the organic signals decay underneath, because only recommendation-sourced players feed the windows. Use ads to seed, not to hide.

## Date caveat

The rules are current as of October 2026. If today is later than January 2027, check the Creator Hub Discovery page before quoting the window structure, and keep the plan's shape even if the numbers move.
