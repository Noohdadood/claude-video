#!/usr/bin/env python3
"""Inspect Roblox storefront media (icons, thumbnails, gameplay videos) with ffprobe.

Pure standard library plus the ffprobe binary. Usage:
    python3 inspect_media.py icon.png thumb.png gameplay.mp4 [--json]
Reports dimensions, aspect ratio, duration, frame rate and audio presence, and flags common problems.
"""
from __future__ import annotations

import argparse
import json
import math
import shutil
import subprocess
import sys
from pathlib import Path

IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif"}
VIDEO_EXT = {".mp4", ".mov", ".webm", ".mkv", ".m4v"}


def probe(path: Path) -> dict:
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type,codec_name,width,height,r_frame_rate,sample_rate",
           "-of", "json", str(path)]
    out = subprocess.run(cmd, capture_output=True, encoding="utf-8")
    if out.returncode != 0:
        raise RuntimeError(out.stderr.strip() or "ffprobe failed")
    return json.loads(out.stdout or "{}")


def ratio_label(w: int, h: int) -> str:
    if not w or not h:
        return "?"
    g = math.gcd(w, h)
    simple = f"{w // g}:{h // g}"
    r = w / h
    for name, val in (("1:1", 1.0), ("16:9", 16 / 9), ("9:16", 9 / 16), ("4:3", 4 / 3)):
        if abs(r - val) < 0.02:
            return name
    return simple


def inspect(path: Path) -> dict:
    info = {"file": str(path), "kind": "video" if path.suffix.lower() in VIDEO_EXT else "image" if path.suffix.lower() in IMAGE_EXT else "unknown",
            "width": None, "height": None, "aspect": None, "duration_s": None, "fps": None, "has_audio": False, "flags": []}
    try:
        data = probe(path)
    except Exception as exc:  # noqa: BLE001
        info["flags"].append(f"could not probe: {exc}")
        return info
    for s in data.get("streams", []):
        if s.get("codec_type") == "video" and info["width"] is None:
            info["width"], info["height"] = s.get("width"), s.get("height")
            fr = s.get("r_frame_rate", "0/1")
            try:
                n, d = fr.split("/")
                info["fps"] = round(int(n) / int(d), 2) if int(d) else None
            except (ValueError, ZeroDivisionError):
                info["fps"] = None
        elif s.get("codec_type") == "audio":
            info["has_audio"] = True
    dur = data.get("format", {}).get("duration")
    info["duration_s"] = round(float(dur), 2) if dur else None
    if info["width"] and info["height"]:
        info["aspect"] = ratio_label(info["width"], info["height"])
    if info["kind"] == "image":
        info["fps"] = None
    flags = info["flags"]
    name = path.stem.lower()
    if info["kind"] == "image":
        if "icon" in name and info["aspect"] != "1:1":
            flags.append("icon should be square (1:1)")
        if "icon" in name and info["width"] and info["width"] < 512:
            flags.append("icon is under 512 px; upload at least 512×512")
        if "icon" not in name and info["aspect"] not in ("16:9",):
            flags.append("thumbnail should be 16:9 (1920×1080 recommended)")
        if "icon" not in name and info["width"] and info["width"] < 1920:
            flags.append("thumbnail is under 1920 px wide")
    elif info["kind"] == "video":
        if info["aspect"] != "16:9":
            flags.append("gameplay video should be 16:9 landscape")
        if info["duration_s"] and info["duration_s"] > 60:
            flags.append("longer than 60 s; the tile autoplays silently, lead with the core verb and keep it short")
        if info["duration_s"] and info["duration_s"] < 10:
            flags.append("shorter than 10 s; may not show a complete fun moment")
        if info["has_audio"]:
            flags.append("has an audio track: confirm there is no voice-over or narration (autoplay is muted anyway)")
        if info["fps"] and info["fps"] < 24:
            flags.append("frame rate under 24 fps; capture again at the game's real frame rate")
    if not flags:
        flags.append("no technical issues; judge the promise and the first 3 seconds by viewing it")
    return info


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("files", nargs="+")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    if not shutil.which("ffprobe"):
        print("ffprobe not found; install ffmpeg (brew install ffmpeg / apt install ffmpeg / winget install Gyan.FFmpeg)", file=sys.stderr)
        return 2
    results = [inspect(Path(f)) for f in args.files]
    if args.json:
        json.dump(results, sys.stdout, indent=1)
        print()
        return 0
    print("| File | Kind | Size | Aspect | Duration | FPS | Audio | Flags |")
    print("|---|---|---|---|---|---|---|---|")
    for r in results:
        size = f"{r['width']}×{r['height']}" if r["width"] else "?"
        dur = f"{r['duration_s']} s" if r["duration_s"] else "-"
        print(f"| {Path(r['file']).name} | {r['kind']} | {size} | {r['aspect'] or '?'} | {dur} | {r['fps'] or '-'} | {'yes' if r['has_audio'] else 'no'} | {'; '.join(r['flags'])} |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
