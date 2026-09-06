import importlib.util
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_security_boundaries.py"
POLICY = ROOT / "security" / "policy.json"

spec = importlib.util.spec_from_file_location("security_validator", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class SecurityBoundaryTests(unittest.TestCase):
    def test_protected_exact_path(self):
        self.assertTrue(module.path_is_protected("PRINCIPLES.md", ["PRINCIPLES.md"]))

    def test_protected_directory(self):
        self.assertTrue(module.path_is_protected(".github/workflows/validate.yml", [".github/workflows/"]))

    def test_unprotected_data_path(self):
        self.assertFalse(module.path_is_protected("data/evidence.json", ["PRINCIPLES.md", "security/"]))

    def run_validator(self, **env_overrides):
        env = os.environ.copy()
        env.update(env_overrides)
        return subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, env=env, text=True, capture_output=True)

    def test_external_pr_requires_human_review(self):
        result = self.run_validator(
            GITHUB_EVENT_NAME="pull_request",
            BASE_REPO="Nate27624/HumanityAI",
            HEAD_REPO="outside/HumanityAI",
            CHANGED_FILES="data/evidence.json\n",
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("HUMAN_REVIEW_REQUIRED", result.stdout)
        self.assertIn("external_pull_request", result.stdout)

    def test_internal_protected_change_requires_human_review(self):
        result = self.run_validator(
            GITHUB_EVENT_NAME="pull_request",
            BASE_REPO="Nate27624/HumanityAI",
            HEAD_REPO="Nate27624/HumanityAI",
            CHANGED_FILES="SECURITY.md\n",
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("protected_path_change", result.stdout)

    def test_internal_unprotected_change_passes(self):
        result = self.run_validator(
            GITHUB_EVENT_NAME="pull_request",
            BASE_REPO="Nate27624/HumanityAI",
            HEAD_REPO="Nate27624/HumanityAI",
            CHANGED_FILES="data/evidence.json\n",
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_policy_requires_email_notification(self):
        policy = json.loads(POLICY.read_text(encoding="utf-8"))
        self.assertIs(policy["email_on_human_review_required"], True)


if __name__ == "__main__":
    unittest.main()
