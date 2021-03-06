from unittest import TestCase
from ..utils import parse_url


class TestParseUrl(TestCase):

    def test_parse_url_success(self):

        self.assertTrue(parse_url("https://gitlab.cern.ch/atrisovi/my-internal-project.git"))
        self.assertTrue(parse_url("https://gitlab.cern.ch/atrisovi/root-examples"))
        self.assertTrue(parse_url("gitlab.cern.ch/atrisovi/root-examples"))
        self.assertTrue(parse_url("https://GitHub.com/enaVerse/enaVerse.github.io.git"))
        self.assertTrue(parse_url("https://github.com/tiborsimko/myrepo"))
        self.assertTrue(parse_url("git@github.com:tiborsimko/myrepo"))
        self.assertTrue(parse_url("https://github.com/atrisovic/cap-import.git"))

    def test_parse_url_failed(self):

        with self.assertRaises(ValueError):
            parse_url("ssh://git@gitlab.cern.ch:7999/atrisovi/root-examples.git")
            parse_url("https://github.com/")
            parse_url("gitgub.com/enaVerse")
