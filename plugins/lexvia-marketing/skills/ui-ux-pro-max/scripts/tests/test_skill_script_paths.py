"""Lexvia's installed skill must resolve documented tools without a repo anchor.

Adapted from upstream's script-path regression test for the single Codex skill
layout. The upstream test walked duplicate CLI and Claude packages instead.
"""

import re
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[2]
INVOCATION = re.compile(r'(?<![\w/.-])(?:python3?|node|bash)\s+"([^"\n]+\.(?:py|cjs|js|mjs|sh))"')


class SkillScriptPathsTest(unittest.TestCase):
    def test_documented_tools_are_quoted_skill_paths_and_ship(self):
        seen = 0
        for md in (SKILL / 'SKILL.md', SKILL / 'README.md', *sorted((SKILL / 'references').glob('*.md'))):
            text = md.read_text(encoding='utf-8')
            with self.subTest(file=md.name):
                self.assertNotIn('${CLAUDE_PLUGIN_ROOT}', text)
                for path in INVOCATION.findall(text):
                    seen += 1
                    self.assertTrue(path.startswith('<skill>/'), path)
                    self.assertTrue((SKILL / path.removeprefix('<skill>/')).is_file(), path)
                # Reject unquoted, relative and host-specific script invocations too.
                for line in text.splitlines():
                    if re.match(r'^(?:python3?|node|bash)\s+(?!-m\b)', line):
                        self.assertRegex(line, r'^\w+\s+"<skill>/scripts/[^"\n]+"')
        self.assertGreater(seen, 10, 'script-path extractor found too few commands')

    def test_packaged_references_resolve(self):
        text = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
        references = set(re.findall(r'`(references/[^`]+\.md)`', text))
        self.assertTrue(references)
        for reference in references:
            self.assertTrue((SKILL / reference).is_file(), reference)
        # The optional sibling workflow is part of this plugin, not the upstream repo.
        self.assertTrue((SKILL.parent / 'taste-skill/SKILL.md').is_file())


if __name__ == '__main__':
    unittest.main()
