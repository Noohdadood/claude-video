---
name: roblox-discovery-audit
description: Audit a Roblox game against the 2026 "Recommended for You" discovery rules (28-day retention windows, play-through and first-play bounce rate, intentional co-play, gameplay video, Roblox Kids and Select eligibility, ads and Standout Games, copycat takedowns) and produce a scorecard with fixes. Use this whenever a Roblox developer asks why their game is not getting recommended, how the Roblox algorithm works now, how to get more players, whether their launch or update plan fits the algorithm, or asks for a review of a game's discovery, retention or front-page performance, even if they never say "algorithm" or "audit".
license: MIT
allowed-tools: Bash, Read, AskUserQuestion
metadata:
  version: "0.1.0"
  derived-from: "The new rules of the Roblox algorithm (youtube.com/watch?v=RC19PKdRt1Y), fact-checked against Roblox announcements, Oct 2026"
---

# Roblox discovery audit

Roblox's Home recommendation system ("Recommended for You", RFY) changed in seven ways between June and October 2026. Most developers still optimise for the old system: a big first day, a loud thumbnail, and a one-time spike. This skill checks a game against the new rules and turns the gaps into a prioritised fix list.

Read `references/new-rules-2026.md` before scoring. It holds each rule with its effective date, the official source, and how well it is verified, so the scorecard can say what is settled and what is still the creator community's reading.

## Gather the inputs

Score only from evidence. Ask for what is missing, in one round, and say plainly what you assumed when the developer cannot answer. Useful inputs, in priority order:

1. **Stage and dates.** Pre-launch, launched within 28 days, or mature. For a game inside its first 28 days, the launch date says which window it is in. For a mature game the windows still apply: every new player who arrives through recommendations is scored on their own Day 1, Days 2–7 and Days 8–28, so audit the live game's rolling behaviour (what a newcomer this week experiences and whether they return) rather than the launch history.
2. **How players arrive.** Share of players from RFY versus ads, search, friends, sponsored sorts or features. Only RFY arrivals feed the retention signals, so a game kept alive by ads can look healthy while its organic ranking decays.
3. **Retention shape.** Daily peak or DAU for the last four weeks. A chart or a few numbers is enough. Look for the pattern: spike-and-decay versus a steady climb.
4. **Day 1 experience.** What happens in the first 30 seconds, what the icon and 16:9 thumbnail promise, and whether a gameplay video is uploaded and approved.
5. **Social design.** Whether the game is more fun with friends and has a reason to invite them.
6. **Audience reach.** Highly engaged player count in the last 60 days from the Audience Reach dashboard, and whether the game is currently visible to under-16 players.
7. **Paid discovery.** Ads in use, ad goal (Plays or Engagement), and whether an Engagement campaign is still running after reaching the threshold.
8. **Originality.** Whether the title, icon or thumbnail resembles an existing popular game.

## Score each shift

Give each of the seven shifts one of three marks and one sentence of evidence:

- **Pass**: the game already does what the rule rewards.
- **At risk**: partly covered, or covered by luck rather than by design.
- **Missing**: the game works against the rule, or there is no plan.

| # | Shift | What RFY now rewards | Typical failure |
|---|---|---|---|
| 1 | 7 days → 28 days | Day 1, Days 2–7 and Days 8–28 judged separately on six signals | No planned reason to return after week one |
| 2 | Win the click → keep the click | High play-through rate, low first-play bounce (under 60 s and 61–180 s) | Icon promises something the first 30 seconds do not deliver |
| 3 | Solo → friends | Intentional co-play days | Nothing to do together; no invite moment |
| 4 | Icons → video | Approved real-gameplay video on the RFY tile and in Moments | No video, or a cinematic trailer that gets rejected |
| 5 | Everyone sees you → you earn the kids | Enough highly engaged players to unlock Roblox Kids and Select audiences | Game is invisible to under-16s and the developer does not know |
| 6 | Free → paid and picked | Plays ads to seed RFY, Engagement ads to reach the threshold, Standout Games nomination | Engagement campaign left running; impression drop after an ad read as a penalty |
| 7 | Copying gets punished | Original title, icon and page | Riding a popular game's name or thumbnail |

Weight the fixes by what the developer controls this week. A pre-launch game should hear about Day 8 planning and the icon promise first; a live game with an ad budget should hear about the Engagement goal and the threshold first.

## Scorecard format

Use this template so results are comparable across games and over time:

```markdown
# Discovery audit: <game name> (<date>)

**Stage:** <pre-launch | day N of 28 | mature> · **Main traffic source:** <RFY | ads | ...>
**Headline:** <one sentence: the single biggest gap and what fixing it unlocks>

## Why this is happening
<Three to five short points that answer the developer's actual question in plain language before the table. Lead with the mechanism (what RFY measures, what it sees from this game), not with the rule's name.>

| Shift | Mark | Evidence | Fix (owner, effort) |
|---|---|---|---|
| 1 · 28-day windows | Pass / At risk / Missing | ... | ... |
| 2 · Keep the click | ... | ... | ... |
| 3 · Friends | ... | ... | ... |
| 4 · Gameplay video | ... | ... | ... |
| 5 · Kids and Select | ... | ... | ... |
| 6 · Paid and picked | ... | ... | ... |
| 7 · Originality | ... | ... | ... |

## Do this week
1. ...
2. ...
3. ...

## Watch next
- Metric to check, where to find it in Creator Hub, and the value that would change the plan.

## Assumptions and open questions
- ...
```

## Judgement calls

- **Spikes are not health.** A weekend event that triples concurrent players and then decays is scored by all three windows. The game that climbs 20% each week for a month ranks better than the one that spiked once. Say so when the developer shows a spike chart with pride.
- **Numbers date quickly.** The highly engaged player thresholds changed three times in 2026 and are scheduled to change again. Quote the number with its effective date, and if today is later than January 2027, tell the developer to confirm the current value in the Creator Hub Kids and Select documentation before acting.
- **Separate official from folklore.** The reference marks which claims Roblox has published and which come from creator trackers. Do not present a tracker's observation as a platform rule.
- **No metric, no verdict.** When the developer has no retention or bounce data, mark the shift "At risk" with the reason "unmeasured" and name the Creator Hub page that would measure it (Retention, Home personalization metrics, Audience Reach). Do not invent a plausible-sounding number.
- **Use the companion skills when they are installed.** They ship beside this one: `roblox-launch-plan` (dated 28-day calendar, `scripts/launch_calendar.py`), `roblox-kids-eligibility` (threshold calculator, `scripts/eligibility.py`) and `roblox-gameplay-video` (icon, thumbnail and video review, `scripts/inspect_media.py`). Running their scripts needs Bash. When they are not installed, cover the essentials here and say which deeper check was skipped.
