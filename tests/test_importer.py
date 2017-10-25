from unittest import TestCase
from ..github_importer import GithubImporter
from ..gitlab_importer import GitlabImporter
from ..importer import Importer


class TestImporter(TestCase):

    def test_importer_factory_github(self):
        gh = Importer.factory("https://GitHub.com/enaVerse/enaVerse.github.io.git")
        assert isinstance(GithubImporter, gh)

    def test_importer_factory_gitlab(self):
        gh = Importer.factory("https://gitlab.cern.ch/atrisovi/root-examples")
        assert isinstance(GitlabImporter, gh)

    def test_archive_repository_github(self):
        gh = Importer.factory("https://GitHub.com/enaVerse/enaVerse.github.io.git")
        self.assertTrue(gh.archive_repository())

    def test_archive_repository_gitlab(self):
        gh = Importer.factory("https://gitlab.cern.ch/atrisovi/root-examples")
        self.assertTrue(gh.archive_repository())
