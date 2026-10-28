"""Offline tests: installer preflight must not perform installation."""

import pathlib
import subprocess
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "jarvis-master-install.sh"


class InstallPreflightTests(unittest.TestCase):
    def invoke(self, *args):
        return subprocess.run(
            ["bash", str(SCRIPT), *map(str, args)],
            text=True, capture_output=True, timeout=15, check=False,
        )

    def test_shell_syntax(self):
        subprocess.run(["bash", "-n", str(SCRIPT)], check=True)

    def test_no_arguments_refuses_installation(self):
        result = self.invoke()
        self.assertEqual(result.returncode, 2)
        self.assertIn("No packages", result.stderr)

    def test_relative_path_rejected(self):
        self.assertEqual(self.invoke("relative-checkout").returncode, 2)

    def test_missing_source_preserves_existing_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            sentinel = root / "existing-service.txt"
            sentinel.write_text("unchanged")
            result = self.invoke(root)
            self.assertEqual(result.returncode, 1)
            self.assertIn("Missing required", result.stderr)
            self.assertEqual(sentinel.read_text(), "unchanged")
            self.assertEqual(list(root.iterdir()), [sentinel])

    def test_complete_source_is_checked_but_never_executed(self):
        with tempfile.TemporaryDirectory(prefix="jarvis source ") as directory:
            root = pathlib.Path(directory)
            (root / "runtime" / "src").mkdir(parents=True)
            (root / "config").mkdir()
            (root / "runtime" / "package.json").write_text('{"private":true}')
            (root / "config" / "prompt-11-profile.json").write_text("{}")
            (root / "runtime" / "src" / "server.mjs").write_text(
                'throw new Error("Preflight must never execute this module");\n'
            )
            result = self.invoke(root)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Source preflight passed", result.stdout)
            self.assertNotIn("Preflight must never execute", result.stderr)
            self.assertFalse((root / "runtime" / "node_modules").exists())
            self.assertFalse((root / "runtime" / ".env").exists())

    def test_invalid_server_syntax_fails_before_success(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            (root / "runtime" / "src").mkdir(parents=True)
            (root / "config").mkdir()
            (root / "runtime" / "package.json").write_text("{}")
            (root / "config" / "prompt-11-profile.json").write_text("{}")
            (root / "runtime" / "src" / "server.mjs").write_text("function {")
            result = self.invoke(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertNotIn("Source preflight passed", result.stdout)


if __name__ == "__main__":
    unittest.main()
