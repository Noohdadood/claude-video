---
name: roblox-kids-eligibility
description: Work out whether a Roblox game is visible to players under 16 (Roblox Kids and Select audiences), how far it is from the highly engaged player threshold that unlocks them, when the threshold next changes, and the fastest route there (organic, Engagement ad goal, or paid Expedited Review). Use this whenever a Roblox developer asks why kids or younger players cannot find their game, mentions "highly engaged players", the Audience Reach dashboard, the 500/250/100 threshold, age-checked players, Kids and Select, Expedited Review, or asks whether to run Engagement ads.
license: MIT
allowed-tools: Bash, Read, AskUserQuestion
metadata:
  version: "0.1.0"
  derived-from: "The new rules of the Roblox algorithm (youtube.com/watch?v=RC19PKdRt1Y), fact-checked against Roblox announcements, Oct 2026"
---

# Roblox Kids and Select eligibility

Since mid-2026, players under 16 (the Roblox Kids and Select audiences) only see games that have completed evaluation. Evaluation completes when enough **highly engaged, age-checked players** have played the game inside a rolling 60-day window. Most of Roblox's audience is young, so a game that has not cleared the bar is invisible to most of the platform and its developer often does not know. This skill reads the numbers, explains them, and lays out the options.

## Steps

1. **Get the two numbers** from Creator Hub → Audience Reach dashboard: unique highly engaged plays in the last 60 days, and whether the game currently shows as eligible for Kids and Select. If the developer only knows roughly, use their estimate and say so.
2. **Run the calculator.** `SKILL_DIR` is the directory containing this file.

   ```bash
   python3 "${SKILL_DIR}/scripts/eligibility.py" --hep 140 --status out --daily-hep 3
   ```

   It reports the entry and maintenance thresholds in force on the given date (`--date`, default today), the gap, the projected date to cross organically from `--daily-hep`, and whether a scheduled threshold drop arrives sooner than the projection. `--list-thresholds` prints the schedule; `--json` gives structured output.
3. **Explain the result in the developer's terms**: what is unlocked, what is missing, and which route is cheapest in time and Robux.
4. **Recommend one route** and the metric that would tell them it is working.

## How the bar works (as of October 2026)

| Date in force | Entry threshold (to become eligible) | Maintenance threshold (to stay eligible) |
|---|---|---|
| until 15 July 2026 | 500 | 100 |
| from 16 July 2026 | 500 | 25 |
| from 19 August 2026 | 250 | 25 |
| November 2026 (reported, exact day to confirm) | 100 | 25 |

- "Highly engaged" means an age-checked user who met a minimum purchase amount anywhere on Roblox in the last 60 days. The definition was relaxed in mid-2026. It is about the player, not about spending in this game.
- The window is rolling: plays older than 60 days fall out, which is why a game can drop below the maintenance bar after a quiet month.
- Entry and maintenance bars are separate. Once in, the game only needs the lower maintenance number.

## Routes to the threshold

- **Organic.** Roblox says many games get there on their own. The calculator's projection shows whether waiting for a scheduled threshold drop is faster than any paid route; often it is.
- **Engagement ad goal (Ads Manager).** Targets age-checked highly engaged players whose sessions count toward the threshold. It costs more per play than the Plays goal because the audience is smaller, and it does **not** pause itself when the threshold is reached. Tell the developer to set a reminder to pause it. Treat it as a separate budget from Plays campaigns, which exist to seed Recommended for You.
- **Expedited Review.** A paid, refundable review (up to 48 hours) that grants access without the threshold, aimed at studios that have not yet met it. Worth it when a launch window matters more than the fee.

## Judgement calls

- A game under the bar is not "shadow-banned"; it is reaching the over-16 audience only. Say which audience is missing and how large it is for that genre.
- Impressions in Recommended for You dropping after an ad campaign is expected, because converted players move to the Continue row. Do not read it as a penalty.
- Thresholds have changed three times in 2026. Quote the number with its date. If today is after January 2027, ask the developer to confirm the current values in the Creator Hub "Roblox Kids and Select" page and update `scripts/eligibility.py`'s `SCHEDULE` if they have moved.

## Sources

- Creator Hub, Roblox Kids and Select: https://create.roblox.com/docs/production/publishing/kids-and-select
- DevForum, "Roblox Kids and Select Global Launch": https://devforum.roblox.com/t/roblox-kids-and-select-global-launch-upcoming-updates-to-eligibility-ads-manager-and-expedited-review/4685717
- DevForum, "Highly Engaged Player Threshold Drops to 250" (19 August 2026): https://devforum.roblox.com/t/highly-engaged-player-threshold-drops-to-250/4820164
- Bloxy News, threshold to 100 in November 2026 (11 September 2026): https://x.com/Bloxy_News/status/2098519640951705762
- Creator Hub, Ads Manager (Engagement goal): https://create.roblox.com/docs/production/promotion/ads-manager
