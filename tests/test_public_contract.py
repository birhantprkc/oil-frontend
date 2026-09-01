import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HERO_SOURCE = ROOT / "assets" / "readme" / "source" / "hero-layout.svg"
HERO_PNG = ROOT / "assets" / "readme" / "hero.png"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class PublicContractTest(unittest.TestCase):
    def test_trigger_policy_is_consistent(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        hero = HERO_SOURCE.read_text(encoding="utf-8")

        self.assertIn("仅在用户明确要求使用 oil-frontend 时触发", skill)
        self.assertIn("明确点名后启用", hero)
        self.assertIn("采用显式启用策略", readme)
        self.assertNotIn("前端改动自动启用", skill + readme + hero)

    def test_execution_evals_explicitly_enable_skill(self) -> None:
        data = json.loads((ROOT / "evals" / "evals.json").read_text(encoding="utf-8"))
        for case in data["evals"]:
            with self.subTest(case=case["name"]):
                self.assertIn("$oil-frontend", case["prompt"])

    def test_trigger_dataset_covers_both_boundaries(self) -> None:
        data = json.loads((ROOT / "evals" / "triggers.json").read_text(encoding="utf-8"))
        positives = [case for case in data["cases"] if case["should_trigger"]]
        negatives = [case for case in data["cases"] if not case["should_trigger"]]
        self.assertGreaterEqual(len(positives), 8)
        self.assertGreaterEqual(len(negatives), 8)

    def test_checked_in_hero_matches_reviewed_assets(self) -> None:
        self.assertEqual(
            sha256(HERO_SOURCE),
            "8fa1db7a1ca2351b0ab4694a1837f5a9a2d766c33d2521a7f7c84dd7cf38ddc7",
        )
        self.assertEqual(
            sha256(HERO_PNG),
            "99cb4eefa10e2e8cff2c93d8163706bbeeb33720eab48f1882252f16f55f4e5c",
        )


if __name__ == "__main__":
    unittest.main()
