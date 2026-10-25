---
name: roblox-gameplay-video
description: Review and plan a Roblox game's storefront media so it wins the click and keeps it: the square icon as a promise the first 30 seconds must keep, the first 16:9 thumbnail that search and Home show, and the gameplay video that autoplays in Recommended for You and Moments (real gameplay only, no cinematic trailer, no voice-over, no better-than-real graphics). Use this whenever a Roblox developer asks about their icon, thumbnail, game page images, trailer, gameplay video, Moments, click-through, play-through rate or bounce rate, or shares image or video files for a Roblox game, even if they only ask "does this look good?".
license: MIT
allowed-tools: Bash, Read, AskUserQuestion
metadata:
  version: "0.1.0"
  derived-from: "The new rules of the Roblox algorithm (youtube.com/watch?v=RC19PKdRt1Y), fact-checked against Roblox announcements, Oct 2026"
---

# Roblox icon, thumbnail and gameplay video review

Roblox replaced "qualified play-through rate" with two signals in 2026: **play-through rate** (did the impression become a play) and **first-play bounce rate** (did the player leave within 60 seconds, or within 61–180 seconds). The change exists because loud thumbnails were winning clicks for games that could not keep them. So the storefront is now judged twice: the icon must win the click, and the first 30 seconds must keep it. Gameplay video, which plays on the Recommended for You tile and in the Moments feed, is the one asset that shows the real thing before the click.

Read `references/media-rules.md` for the rules and sources. If the developer shares files, inspect them first.

## Steps

1. **Collect the set.** Icon (square), the first 16:9 thumbnail in the gallery, any gameplay video, and a description or recording of the first 30 seconds of play. Ask what the game is actually like for a new player; the review is a comparison between promise and delivery.
2. **Inspect files when given.** `SKILL_DIR` is the directory containing this file.

   ```bash
   python3 "${SKILL_DIR}/scripts/inspect_media.py" icon.png thumb_1.png gameplay.mp4
   ```

   It uses `ffprobe` to report dimensions, aspect ratio, duration, frame rate and whether a video has an audio track, then flags the obvious problems (non-square icon, non-16:9 thumbnail, video with narration-length speech is something you must judge by watching). View images and sample frames with the host's image tool before judging composition.
3. **Score five things** with the table below.
4. **Write the fix list and, if a video is missing or rejected, a shot list** the developer can record this week.

## Review table

| Asset | Question | Pass looks like |
|---|---|---|
| Icon | Does it promise exactly what happens in the first 30 seconds? | A new player can name the first thing they will do from the icon alone. |
| Icon | Does it stop the eye on a crowded front page at small size? | One subject, high contrast, readable at 150 px. |
| First 16:9 thumbnail | Does it hold up as the search-result image, not just a gallery slide? | Same promise as the icon, more context, no text that lies. |
| Gameplay video | Is it real, current gameplay with no narration, no cinematic cuts, no graphics the game cannot show? | Would be identical to a player's own Moments clip. |
| Gameplay video | Does it show the first fun moment inside the first few seconds? | Autoplay has no sound; the action must read silently and fast. |

Mark each row Pass / Fix / Missing, with one sentence of evidence and one concrete change.

## Shot list template for a compliant video

```markdown
# Gameplay video shot list: <game>
Target: 15–30 s of continuous or lightly cut real gameplay, no voice-over, no title cards, default graphics.
1. 0–3 s  The core verb, mid-action (the thing the icon promises).
2. 3–10 s Progress or payoff: a reward, a reveal, a near miss.
3. 10–20 s Social proof: a friend joining, a shared moment, a crowd.
4. 20–30 s Loop back to the core verb at a higher level so it reads as depth.
Record at the game's real settings on a mid-range device; capture, don't render.
Upload: Creator Hub → place settings → Videos tab; wait for approval before launch day.
```

## Judgement calls

- **The icon is a contract, not an ad.** When the icon is better than the game, fix the game's first 30 seconds or tone down the icon; do not pick the icon that tests best in isolation.
- **Trailers get rejected and would mislead anyway.** Cinematic footage raises the click and the bounce at the same time, which is the exact pair of signals the new system punishes.
- **Silence by default.** Autoplay on the tile is muted. If the clip needs sound to make sense, it needs a different first three seconds.
- **Numbers are case studies.** The often-quoted "+39% playtime" comes from one game (Notoriety) in Roblox's announcement, alongside +31% for another. Expect a lift, not that lift.
- **Test on the real page.** Compare the icon in a mock of the live front page against current top games at the size they appear. Third-party front-page tests exist; a screenshot and an honest eye work too.
