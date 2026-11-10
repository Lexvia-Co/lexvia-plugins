"""Exercise the real CLI as a relocated skill in a consumer project."""

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

SKILL = Path(__file__).resolve().parents[2]


def snapshot(directory):
    return {
        str(path.relative_to(directory)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in directory.rglob('*')
        if path.is_file() and '__pycache__' not in path.parts
    }


class TestInstalledSkill(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='lexvia-pro-max-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.consumer = self.root / 'Consumer Project'
        self.consumer.mkdir()
        self.installed = self.root / 'Plugin Cache With Spaces' / 'ui-ux-pro-max'
        shutil.copytree(SKILL, self.installed, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))

    def run_cli(self, *args, skill=None):
        completed = subprocess.run(
            [sys.executable, str((skill or self.installed) / 'scripts/search.py'), *args, '--json'],
            cwd=self.consumer,
            env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'},
            capture_output=True, text=True, check=True,
        )
        return json.loads(completed.stdout)

    def test_search_and_design_system_from_unrelated_working_directory(self):
        original = snapshot(self.installed)
        for skill in (SKILL, self.installed):
            with self.subTest(skill=str(skill)):
                result = self.run_cli('error summary validation', '--domain', 'ux', skill=skill)
                self.assertEqual(result['domain'], 'ux')
                self.assertGreater(result['count'], 0)
                result = self.run_cli('chip badge overflow nowrap', '--stack', 'html-tailwind', skill=skill)
                self.assertEqual(result['stack'], 'html-tailwind')
                self.assertEqual(result['results'][0]['Guideline'], 'Compact label layout')
                result = self.run_cli('internal analytics dashboard', '--design-system', skill=skill)
                self.assertTrue(result['design_system']['colors'])
                self.assertIsNone(result['persistence'])
        self.assertEqual(list(self.consumer.iterdir()), [])
        self.assertEqual(snapshot(self.installed), original)

    def test_persist_preserves_decisions_and_explicit_force_overwrites(self):
        original = snapshot(self.installed)
        args = (
            'internal analytics dashboard', '--design-system', '--persist',
            '-p', 'Consumer Project', '--output-dir', str(self.consumer),
        )
        result = self.run_cli(*args)
        self.assertEqual(result['persistence']['status'], 'success')
        master = self.consumer / 'design-system/consumer-project/MASTER.md'
        self.assertTrue(master.is_file())
        master.write_text('Existing approved master\n', encoding='utf-8')
        result = self.run_cli(*args)
        self.assertEqual(result['persistence']['status'], 'skipped_exists')
        self.assertEqual(master.read_text(encoding='utf-8'), 'Existing approved master\n')

        result = self.run_cli(*args, '--page', 'dashboard')
        page = master.parent / 'pages/dashboard.md'
        self.assertEqual(result['persistence']['status'], 'success')
        self.assertTrue(page.is_file())
        self.assertEqual(master.read_text(encoding='utf-8'), 'Existing approved master\n')
        page.write_text('Existing approved page\n', encoding='utf-8')
        result = self.run_cli(*args, '--page', 'dashboard')
        self.assertEqual(result['persistence']['status'], 'skipped_exists')
        self.assertEqual(page.read_text(encoding='utf-8'), 'Existing approved page\n')

        # This invocation represents an explicitly authorized overwrite.
        result = self.run_cli(*args, '--page', 'dashboard', '--force')
        self.assertEqual(result['persistence']['status'], 'success')
        self.assertNotEqual(master.read_text(encoding='utf-8'), 'Existing approved master\n')
        self.assertNotEqual(page.read_text(encoding='utf-8'), 'Existing approved page\n')
        self.assertEqual(snapshot(self.installed), original)


if __name__ == '__main__':
    unittest.main()
