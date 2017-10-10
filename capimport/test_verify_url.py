from unittest import TestCase


class TestVerifyUrl(TestCase):

    def test_verify_url(self):
        from importer import verify_url
        self.assertTrue(verify_url("https://GitHub.com/enaVerse/enaVerse.github.io.git"))
        self.assertTrue(verify_url("https://gitlab.cern.ch/atrisovi/root-examples"))
        self.assertTrue(verify_url("gitlab.cern.ch/atrisovi/root-examples"))
        with self.assertRaises(ValueError):
            verify_url("ssh://git@gitlab.cern.ch:7999/atrisovi/root-examples.git")
            verify_url("https://github.com/")
            verify_url("gitgub.com/enaVerse")
