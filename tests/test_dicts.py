import unittest
from utils.dicts import get_val


class TestDicts(unittest.TestCase):
    def test_key(self):
        data = {"vcs": "mercurial"}
        self.assertEqual(get_val(data, "vcs"), 'mercurial')
        self.assertEqual(get_val(data, "vcs", "git"), 'mercurial')

    def test_default(self):
        data = {}
        self.assertEqual(get_val({}, "vcs", "git"), 'git')
        self.assertEqual(get_val({}, "vcs", "bazaar"), 'bazaar')
        self.assertEqual(get_val(data, "vcs", "git"), 'git')
        self.assertEqual(get_val(data, "vcs", "bazaar"), 'bazaar')

