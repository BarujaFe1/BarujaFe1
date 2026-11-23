import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import profile_assets as assets


def response():
    return {"data": {"user": {"login": "BarujaFe1", "contributionsCollection": {
        "startedAt": "2025-11-23T00:00:00Z", "endedAt": "2026-11-23T00:00:00Z",
        "totalCommitContributions": 100, "totalPullRequestContributions": 12,
        "totalIssueContributions": 2, "totalPullRequestReviewContributions": 5,
        "contributionCalendar": {"totalContributions": 125},
    }}}}


class ProfileAssetsTests(unittest.TestCase):
    def test_real_shape_and_deterministic_safe_svg(self):
        activity = assets.parse_activity(response(), "barujafe1")
        self.assertEqual(activity["commits"], 100)
        self.assertEqual(activity["total"], 125)
        activity["login"] = 'A<&"'
        svg = assets.stats_svg(activity)
        self.assertEqual(svg, assets.stats_svg(activity))
        root = ET.fromstring(svg)
        self.assertIn('A<&"', "".join(root.itertext()))
        self.assertNotIn("<script", svg)
        ET.fromstring(assets.featured_svg())

    def test_rejects_partial_errors_wrong_user_and_bad_counts(self):
        invalid = [None, {}, {"errors": [{"message": "failure"}]},
                   {"data": {"user": None}}]
        for key, value in [("totalCommitContributions", -1),
                           ("totalPullRequestContributions", True),
                           ("totalIssueContributions", "0"),
                           ("startedAt", "bad-date"),
                           ("endedAt", "2025-11-24T00:00:00Z")]:
            payload = response()
            payload["data"]["user"]["contributionsCollection"][key] = value
            invalid.append(payload)
        wrong_user = response()
        wrong_user["data"]["user"]["login"] = "someone-else"
        invalid.append(wrong_user)
        partial = response()
        del partial["data"]["user"]["contributionsCollection"]["totalCommitContributions"]
        invalid.append(partial)
        for payload in invalid:
            with self.subTest(payload=payload), self.assertRaises(ValueError):
                assets.parse_activity(payload, "BarujaFe1")

    def test_failed_input_keeps_both_previous_assets(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            for name in ["stats.svg", "featured-dataflow.svg"]:
                (target / name).write_text("previous valid asset")
            source = target / "input.json"
            for body in ['{"errors":[{"message":"failure"}]}', '{broken', 'null']:
                source.write_text(body)
                with contextlib.redirect_stderr(io.StringIO()):
                    self.assertEqual(assets.main(["--input", str(source), "--output-dir", directory]), 1)
                for name in ["stats.svg", "featured-dataflow.svg"]:
                    self.assertEqual((target / name).read_text(), "previous valid asset")

    def test_input_generates_cards_and_featured_only_keeps_stats(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "input.json"
            source.write_text(json.dumps(response()))
            args = ["--input", str(source), "--output-dir", directory]
            self.assertEqual(assets.main(args), 0)
            stats = Path(directory, "stats.svg").read_bytes()
            self.assertEqual(assets.main(args), 0)
            self.assertEqual(Path(directory, "stats.svg").read_bytes(), stats)
            self.assertEqual(assets.main(["--featured-only", "--output-dir", directory]), 0)
            self.assertEqual(Path(directory, "stats.svg").read_bytes(), stats)

    def test_api_failures_do_not_leak_response_body(self):
        for error in [HTTPError("https://api.github.com/graphql", 403, "sensitive", {}, None),
                      URLError("sensitive"), TimeoutError("sensitive")]:
            with patch.dict("os.environ", {"GH_TOKEN": "synthetic-test-token"}), \
                    patch.object(assets, "urlopen", side_effect=error):
                with self.assertRaises(ValueError) as caught:
                    assets.fetch_activity("BarujaFe1")
                self.assertNotIn("sensitive", str(caught.exception))
                self.assertNotIn("synthetic-test-token", str(caught.exception))


if __name__ == "__main__":
    unittest.main()
