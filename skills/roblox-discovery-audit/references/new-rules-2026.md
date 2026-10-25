# Roblox discovery rules, 2026 fact sheet

Compiled 25 October 2026 from a creator explainer ("The new rules of the Roblox algorithm", Rebloxed) and checked against Roblox's own announcements. Each item carries a verification mark:

- **Official**: stated in a Roblox newsroom post, DevForum announcement, Creator Hub documentation or roadmap.
- **Reported**: reported by creator news accounts or trackers; consistent with official material but not quoted from it.
- **Creator claim**: the explainer's own data or reading; treat as a hypothesis.

Dates are the best available; Roblox describes roadmap windows as estimates.

## Shift 1 · Retention is judged over 28 days, in three windows

- **Official.** RFY moved from a 7-day view to a 28-day view, measuring Day 1, Days 2–7 and Days 8–28 separately. Announced in the Roblox newsroom on 15 June 2026 and on the DevForum ("Recommended For You Algorithm Improvements That Better Value Long-Term Retention"). The explainer dates the switch to 18 June.
- **Official.** Signals per window: playtime, play days, qualified play sessions, intentional co-play days, spend days, Robux spent.
- **Official.** New games do not wait 28 days before Home can recommend them (Discovery FAQ). Benchmarks and benchmark games do not affect the algorithm.
- **Reported.** Signals are measured for players who arrived through Home recommendations. The explainer's stronger wording, that ad, search, friend and feature arrivals never count, is a paraphrase.
- **Creator claim.** Steal an Egg's event spikes (~10M concurrent; trackers show a 14.3M peak on 19 Sept 2026) with normal days falling from ~2.5M to ~1.4M, versus NFL Universe Football's steady weekly climb (23K → 38K), as the picture of what the new windows punish and reward.
- **Practical rule.** Plan the Day 8 reason to return (update, event, unlock) before launch. One-time plays with no return hurt more than they help.

## Shift 2 · Win the click, then keep the click

- **Official.** Qualified play-through rate was removed. Play-through rate (top-priority positive signal) and first-play bounce rate (negative signal, split into under 60 s and 61–180 s) replaced it. Source: the same DevForum post and the Creator Hub Discovery page.
- **Reported.** Roblox's stated reason: a system that looked only at the click could favour games that win attention with exciting thumbnails but do not keep players. The exact quote used in the explainer was not retrievable.
- **Practical rule.** The icon is a promise; the first 30 seconds must deliver it. Test the icon against the live front page before launch.

## Shift 3 · Solo players → friends

- **Official.** "Intentional co-play days" is one of the six retention signals.
- **Official.** RDC 2026 (10–12 September, San Jose) announced a Friends chat tab that follows players across games so they can coordinate and join together.
- **Practical rule.** Games that are better with a friend, and that give players a moment to invite one, get the boost twice: more co-play days and more spend.

## Shift 4 · Icons → gameplay video

- **Official.** Gameplay videos are fully rolled out on Home inside RFY. Upload in Creator Hub under place settings, Videos tab; the video needs approval before it is eligible to play. Source: DevForum, "Gameplay Videos on Home: Help Your Games Get Discovered".
- **Official, but a case study.** The widely quoted "+39%" is Notoriety: A PAYDAY Experience, which saw +41% RFY plays and +39% RFY playtime with a video present. Superstar Baseball saw +31% playtime. It is not a platform average.
- **Official.** Moments, Roblox's short-form gameplay feed with a Join button, launched September 2025 from Search and the More tab. The dedicated Moments tab arrived with the 2026 app redesign, rolling out from 28 July 2026 starting in Canada, New Zealand and Singapore. The explainer calls it a US feature; that is not confirmed.
- **Reported.** Content rules as creators describe them: real, current gameplay; no cinematic trailer; no voice-over or narration; no graphics better than what players see. Roblox's thumbnail documentation requires real gameplay footage; the specific prohibitions were not verified verbatim.
- **Creator claim.** Search results show the first 16:9 image from the gallery rather than the square icon, so the 16:9 image matters as much as the icon.

## Shift 5 · Everyone sees you → you earn the under-16 audience

- **Official.** Roblox Kids and Select audiences (players under 16) see only games that have completed evaluation or passed a paid, refundable Expedited Review (up to 48 hours). The global launch was announced in April 2026; the DevForum thread "Roblox Kids and Select Global Launch" is dated mid-June with updates on 6 and 16 July. The explainer dates visibility gating to 16 June.
- **Official.** Evaluation completes at a number of unique plays by highly engaged, age-checked users within a rolling 60-day window. Highly engaged means the user met a minimum purchase amount anywhere on Roblox in the last 60 days; the definition was relaxed in mid-2026, which Roblox said raised new catalog entries by 33%.
- **Official.** Entry threshold: 500, cut to 250 on 19 August 2026 (DevForum, "Highly Engaged Player Threshold Drops to 250").
- **Official.** Maintenance threshold to stay eligible: 100, cut to 25 on 16 July 2026.
- **Reported.** Entry threshold drops to 100 in November 2026 (Bloxy News, 11 September 2026). Confirm the exact date against the Creator Hub before quoting it.
- **Where to look.** Creator Hub → Audience Reach dashboard shows progress toward the threshold.

## Shift 6 · Free discovery → paid and picked

- **Official.** Ads Manager's Plays goal seeds RFY ("initial traffic to help recommendation systems learn"). The Engagement goal targets age-checked highly engaged players whose sessions count toward the Kids and Select threshold, typically at a higher cost per play, and it does not pause itself when the threshold is reached. Roblox calls it optional: many games reach the threshold organically.
- **Creator claim.** Ads are blended into the RFY sort and ad-sourced players do not change organic ranking. Not found in public documentation.
- **Official.** Standout Games is a curated Home sort for novel games, chosen daily by Roblox's curation team. Nomination is by survey and asks for gameplay video. Under-represented genres named in the docs (updated 16 October 2026): RPG, strategy, puzzle, shooter. Copies and reskins are a hard sell. Whether it replaced a Home sort called Today's Picks was not confirmed; Today's Picks on Marketplace is a separate avatar-item program.
- **Creator claim.** A drop in recommended impressions after an ad or feature is normal because those players now see the game in their Continue row instead.

## Shift 7 · Copying gets punished

- **Official.** Creator Roadmap, late 2026: "Deceptive game copy takedowns". Games that impersonate an existing game's experience detail page may be taken down automatically after publishing; protections apply to the creators and groups that own the original. The Spring 2026 roadmap update announced ramped-up moderation against games that deceptively copy existing titles.
- **Creator claim.** A copy of a popular game peaked near 928K players in August 2026 and fell to ~6K by late October, while the original held roughly 200K. Game names were unclear in the source.
- **Practical rule.** Novelty is now rewarded twice: Standout Games prefers it, and takedowns punish its absence.

## Delivery lesson from the explainer's "who's winning" list

Four small games grew steadily over four weeks of weekly peaks (Find or Die 2.0K → 7.3K, Build a House 2.1K → 6.2K, Wanted 7.1K → 19.7K, Lethal Ape Experience 17K → 31K). None spiked; each shipped a reason to come back. **Creator claim** for the numbers; the pattern matches what the 28-day windows reward.

## Sources

- Roblox newsroom, "Optimizing discovery: how great games reach millions of players on Roblox" (June 2026): https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox
- DevForum, "Recommended For You Algorithm Improvements That Better Value Long-Term Retention": https://devforum.roblox.com/t/recommended-for-you-algorithm-improvements-that-better-value-long-term-retention/4684575
- Creator Hub, Discovery and Discovery FAQ: https://create.roblox.com/docs/discovery · https://create.roblox.com/docs/discovery-faq
- DevForum, "Gameplay Videos on Home: Help Your Games Get Discovered": https://devforum.roblox.com/t/gameplay-videos-on-home-help-your-games-get-discovered/4842601
- Roblox newsroom, Moments (September 2025): https://about.roblox.com/newsroom/2025/09/roblox-moments-user-generated-discovery
- DevForum, "Roblox Kids and Select Global Launch": https://devforum.roblox.com/t/roblox-kids-and-select-global-launch-upcoming-updates-to-eligibility-ads-manager-and-expedited-review/4685717
- DevForum, "Highly Engaged Player Threshold Drops to 250": https://devforum.roblox.com/t/highly-engaged-player-threshold-drops-to-250/4820164
- Creator Hub, Roblox Kids and Select: https://create.roblox.com/docs/production/publishing/kids-and-select
- Bloxy News, threshold to 100 in November 2026: https://x.com/Bloxy_News/status/2098519640951705762
- Creator Hub, Ads Manager: https://create.roblox.com/docs/production/promotion/ads-manager
- Creator Hub, Standout Games: https://create.roblox.com/docs/creator-programs/standout-games
- Roblox Creator Roadmap and Spring 2026 update: https://create.roblox.com/roadmap · https://devforum.roblox.com/t/creator-roadmap-2026-spring-update/4625473
- DevForum, "RDC26: What We Announced": https://devforum.roblox.com/t/rdc26-what-we-announced/4865880
- RoWatcher, Steal An Egg: https://rowatcher.com/games/10563114921/steal-an-egg
