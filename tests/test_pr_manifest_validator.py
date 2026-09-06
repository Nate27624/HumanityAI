import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_pr_manifest.py"

CHECKS = [
    "This contribution does not treat AI-generated text as independent evidence.",
    "Consequential factual claims are traceable to verifiable sources where reasonably possible.",
    "Credible disagreement, limitations, and uncertainty are preserved.",
    "This does not weaken tests/provenance merely to obtain green CI.",
    "This does not expand autonomous authority over consequential real-world actions.",
    "This does not silently modify foundational human-agency, rights, consent, pluralism, peaceful-cooperation, or governance protections.",
    "I checked for materially duplicate work.",
    "I have the right to submit my contribution under the repository's Apache-2.0 license and have not silently relicensed third-party source material.",
]


def valid_body():
    checklist = "\n".join(f"- [x] {item}" for item in CHECKS)
    return f"""## HumanityAI contribution summary

A reviewable external contribution that improves source validation without changing governance.

### Contribution manifest
- **Task ID:** AT0001
- **Agent/model/system:** test-agent
- **Human reviewed before submission:** no
- **Coordination check:** issue checked and open PRs checked

### Evidence and epistemics
- **Primary/authoritative sources consulted:** HTTP specifications and repository policy
- **Important contradictory, negative, or qualifying evidence:** transient failures can mimic dead links
- **Key uncertainty / unresolved question:** network conditions vary across CI environments

### Evaluation
- **Validators/tests run:** unittest plus repository validators
- **Expected benefit:** reduce stale citations without false evidence deletion
- **Plausible failure modes / ways this could be misleading:** false positives from rate limits
- **Reversibility:** easy; validator can be reverted

### Files changed
scripts and tests

### Governance and safety checklist
{checklist}
"""


class ManifestValidatorTests(unittest.TestCase):
    def run_validator(self, *, head_repo, body):
        env = os.environ.copy()
        env.update({
            "GITHUB_EVENT_NAME": "pull_request",
            "BASE_REPO": "Nate27624/HumanityAI",
            "HEAD_REPO": head_repo,
            "PR_BODY": body,
        })
        return subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=ROOT,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_same_repo_pr_bypasses_external_gate(self):
        result = self.run_validator(head_repo="Nate27624/HumanityAI", body="short")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_valid_external_manifest_passes(self):
        result = self.run_validator(head_repo="someone/HumanityAI", body=valid_body())
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_external_manifest_missing_governance_fails(self):
        body = valid_body().replace(f"- [x] {CHECKS[0]}\n", "")
        result = self.run_validator(head_repo="someone/HumanityAI", body=body)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("must affirm governance checklist item", result.stdout)

    def test_unfilled_task_field_fails(self):
        body = valid_body().replace("- **Task ID:** AT0001", "- **Task ID:** <!-- AT0001, etc. -->")
        result = self.run_validator(head_repo="someone/HumanityAI", body=body)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unfilled manifest field", result.stdout)


if __name__ == "__main__":
    unittest.main()
