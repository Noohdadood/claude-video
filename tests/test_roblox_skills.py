"""The Roblox discovery skills are self-contained folders that install beside watch."""
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SKILLS = sorted(p for p in (ROOT / 'skills').glob('roblox-*') if p.is_dir())
ALLOWED = {'name', 'description', 'license', 'allowed-tools', 'metadata', 'compatibility'}


def test_four_roblox_skills_exist():
    assert [p.name for p in SKILLS] == ['roblox-discovery-audit', 'roblox-gameplay-video', 'roblox-kids-eligibility', 'roblox-launch-plan']


@pytest.mark.parametrize('skill', SKILLS, ids=lambda p: p.name)
def test_frontmatter_is_agent_skills_compatible(skill):
    text = (skill / 'SKILL.md').read_text(encoding='utf-8')
    assert text.startswith('---\n')
    frontmatter = text.split('---\n')[1]
    keys = {line.split(':')[0] for line in frontmatter.splitlines() if line and not line.startswith(' ')}
    assert keys <= ALLOWED, keys - ALLOWED
    assert re.search(r'^name: ' + re.escape(skill.name) + '$', frontmatter, re.M)
    assert 'CLAUDE_SKILL_DIR' not in text
    # Every eval case has the files `claude plugin eval` needs.
    for case in (skill / 'evals').iterdir():
        assert (case / 'prompt.md').is_file() and (case / 'case.yaml').is_file()
        assert list((case / 'graders').glob('*.md')), case


def run(script, *args):
    result = subprocess.run([sys.executable, str(script), *args], capture_output=True, encoding='utf-8')
    assert result.returncode == 0, result.stderr
    return result.stdout


def test_launch_calendar_windows_follow_the_launch_date():
    script = ROOT / 'skills/roblox-launch-plan/scripts/launch_calendar.py'
    plan = json.loads(run(script, '--launch', '2026-12-05', '--name', 'Siege Garden', '--json'))
    windows = [(w['start'], w['end']) for w in plan['windows']]
    assert windows == [('2026-12-05', '2026-12-05'), ('2026-12-06', '2026-12-11'), ('2026-12-12', '2027-01-01')]
    days = {b['day']: b['date'] for b in plan['beats']}
    assert days[8] == '2026-12-12' and days[28] == '2027-01-01'
    markdown = run(script, '--launch', '2026-12-05', '--weekly-day', 'Saturday')
    assert '| 8 | Sat 12 Dec 2026 |' in markdown and 'Days 8–28' in markdown


def test_eligibility_thresholds_track_the_2026_schedule():
    script = ROOT / 'skills/roblox-kids-eligibility/scripts/eligibility.py'
    before = json.loads(run(script, '--hep', '80', '--date', '2026-10-20', '--daily-hep', '2', '--json'))
    assert (before['entry_threshold'], before['maintenance_threshold'], before['gap']) == (250, 25, 170)
    assert before['projection']['days_to_cross'] == 85 and before['next_change']['entry_threshold'] == 100
    assert before['next_change']['already_meets_it'] is False
    later = json.loads(run(script, '--hep', '120', '--date', '2026-12-01', '--json'))
    assert later['entry_threshold'] == 100 and later['meets_threshold'] is True
    maintained = json.loads(run(script, '--hep', '30', '--status', 'in', '--date', '2026-09-01', '--json'))
    assert maintained['applicable_threshold'] == 25 and maintained['meets_threshold'] is True
    early = json.loads(run(script, '--hep', '30', '--status', 'in', '--date', '2026-07-01', '--json'))
    assert early['applicable_threshold'] == 100 and early['gap'] == 70


def test_inspect_media_flags_shape_problems(tmp_path):
    import shutil
    if not shutil.which('ffmpeg') or not shutil.which('ffprobe'):
        pytest.skip('ffmpeg required')
    icon = tmp_path / 'icon.png'
    thumb = tmp_path / 'thumb_1.png'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', 'color=c=red:s=1280x720', '-frames:v', '1', str(icon)], check=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', 'color=c=blue:s=1920x1080', '-frames:v', '1', str(thumb)], check=True)
    rows = json.loads(run(ROOT / 'skills/roblox-gameplay-video/scripts/inspect_media.py', str(icon), str(thumb), '--json'))
    by_name = {Path(r['file']).name: r for r in rows}
    assert any('square' in f for f in by_name['icon.png']['flags'])
    assert by_name['thumb_1.png']['aspect'] == '16:9' and by_name['thumb_1.png']['flags'] == ['no technical issues; judge the promise and the first 3 seconds by viewing it']
