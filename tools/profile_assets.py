#!/usr/bin/env python3
"""Generate standalone profile SVGs using Python's standard library."""

import argparse
from datetime import datetime
from html import escape
import json
import os
from pathlib import Path
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
QUERY = """query($login: String!) {
  user(login: $login) {
    login
    contributionsCollection {
      startedAt endedAt
      totalCommitContributions totalPullRequestContributions
      totalIssueContributions totalPullRequestReviewContributions
      contributionCalendar { totalContributions }
    }
  }
}"""


def fetch_activity(login):
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        raise ValueError("Set GH_TOKEN or GITHUB_TOKEN, or supply --input JSON.")
    request = Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": login}}).encode(),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json",
                 "User-Agent": "profile-assets"},
    )
    try:
        with urlopen(request, timeout=30) as response:
            return json.load(response)
    except HTTPError as error:
        raise ValueError(f"GitHub API returned HTTP {error.code}.") from None
    except (URLError, TimeoutError):
        raise ValueError("GitHub API unavailable.") from None


def parse_activity(payload, login):
    """Reject partial responses instead of publishing plausible but false zeroes."""
    try:
        if payload.get("errors"):
            raise ValueError("GitHub GraphQL reported errors.")
        user = payload["data"]["user"]
        if user["login"].casefold() != login.casefold():
            raise ValueError("Activity belongs to a different GitHub account.")
        data = user["contributionsCollection"]
        start = datetime.fromisoformat(data["startedAt"].replace("Z", "+00:00"))
        end = datetime.fromisoformat(data["endedAt"].replace("Z", "+00:00"))
        if not 330 <= (end - start).days <= 367:
            raise ValueError("Expected an annual contribution window.")
        metrics = {
            "total": data["contributionCalendar"]["totalContributions"],
            "commits": data["totalCommitContributions"],
            "pull_requests": data["totalPullRequestContributions"],
            "issues": data["totalIssueContributions"],
            "reviews": data["totalPullRequestReviewContributions"],
        }
        if any(type(value) is not int or value < 0 for value in metrics.values()):
            raise ValueError("Contribution counts must be non-negative integers.")
        return {**metrics, "login": user["login"], "start": start.date().isoformat(),
                "end": end.date().isoformat()}
    except (KeyError, TypeError, AttributeError, OverflowError):
        raise ValueError("Incomplete or malformed GitHub activity response.") from None


def text(x, y, value, size=18, color="#c8cce8", extra=""):
    return (f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" '
            f'{extra}>{escape(str(value))}</text>')


def frame(title, description, body, height):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{height}" viewBox="0 0 960 {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">{escape(description)}</desc>
<defs><pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="#282348" stroke-width="1"/></pattern></defs>
<rect width="960" height="{height}" rx="16" fill="#101126"/>
<rect x="1" y="1" width="958" height="{height - 2}" rx="16" fill="url(#grid)" stroke="#6550a4"/>
<path d="M24 2H220M740 {height - 2}H936" stroke="#b85aff" stroke-width="3"/>
<g font-family="ui-monospace, SFMono-Regular, Consolas, monospace">
{body}
</g></svg>
'''


def stats_svg(activity):
    a = activity
    body = text(32, 44, "GITHUB / ACTIVITY", 17, "#55dcff")
    body += text(32, 78, f'@{a["login"]} · last year', 24, "#f0eeff")
    body += '<path d="M32 98H928" stroke="#393158"/>'
    for x, key, label, color in [
        (32, "total", "Contributions", "#55dcff"),
        (350, "commits", "Commit contributions", "#c48bff"),
        (668, "pull_requests", "Pull requests", "#74efd3"),
    ]:
        body += f'<rect x="{x}" y="121" width="8" height="8" fill="{color}"/>'
        body += text(x, 189, f'{a[key]:,}', 54, "#f0eeff", 'font-weight="700"')
        body += text(x, 222, label, 21)
    body += text(32, 267, f'Reviews {a["reviews"]:,}  /  Issues {a["issues"]:,}', 18, "#b49adf")
    body += text(32, 301, f'{a["start"]} → {a["end"]} UTC · API snapshot', 17, "#a6a8c6")
    return frame("Felipe Baruja — GitHub activity",
                 f'{a["total"]} contributions, {a["commits"]} commit contributions and '
                 f'{a["pull_requests"]} pull requests from {a["start"]} to {a["end"]}.', body, 328)


def featured_svg():
    body = text(32, 44, "FEATURED PROJECT / DATA QUALITY LAB", 17, "#55dcff")
    body += '<path d="M34 83l30-17 30 17-30 17zM34 101l30 17 30-17M34 119l30 17 30-17" fill="none" stroke="#55dcff" stroke-width="7"/>'
    body += text(116, 123, "DataFlow", 55, "#f0eeff", 'font-weight="700"')
    body += text(32, 177, "Understand your data.", 28, "#f0eeff")
    body += text(32, 214, "Explain the signals behind the score.", 23)
    body += text(32, 268, "PROFILE  /  INVESTIGATE  /  CLEAN", 18, "#c48bff")
    body += text(32, 306, "Local-first · Explainable · Privacy-conscious", 17, "#a6a8c6")
    # Decorative interface, deliberately without invented metrics.
    body += '<rect x="645" y="70" width="281" height="214" rx="8" fill="#181a38" stroke="#6550a4"/>'
    body += text(665, 100, "QUALITY EXPLORER", 16, "#55dcff")
    for x, h, color in [(669, 36, "#6550a4"), (705, 58, "#9363da"), (741, 48, "#b85aff"), (777, 90, "#55dcff"), (813, 70, "#36b6d5"), (849, 110, "#74efd3")]:
        body += f'<rect x="{x}" y="{236-h}" width="24" height="{h}" fill="{color}"/>'
    body += text(665, 265, "ILLUSTRATIVE UI", 13, "#a6a8c6")
    return frame("DataFlow — featured data quality lab",
                 "Local-first data profiling, explainable quality signals and auditable cleaning. Lab/demo project.", body, 340)


def write_asset(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--login", default="BarujaFe1")
    parser.add_argument("--input", help="GitHub GraphQL JSON file, or - for stdin")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "assets")
    parser.add_argument("--featured-only", action="store_true")
    args = parser.parse_args(argv)
    try:
        if not args.featured_only:
            if args.input == "-":
                payload = json.load(sys.stdin)
            elif args.input:
                payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
            else:
                payload = fetch_activity(args.login)
            stats = stats_svg(parse_activity(payload, args.login))
        featured = featured_svg()
        # Validate the full response before replacing any checked-in asset.
        if not args.featured_only:
            write_asset(args.output_dir / "stats.svg", stats)
        write_asset(args.output_dir / "featured-dataflow.svg", featured)
    except (ValueError, OSError):
        print("Asset generation failed: invalid input, API unavailable, or output unwritable. Previous valid cards are retained on API/input failures.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
