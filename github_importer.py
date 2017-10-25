from urllib2 import urlopen
from github import Github
from base_importer import BaseImporter


class GithubImporter(BaseImporter):

    def __init__(self, repo, ref=None, token=None):
        self.repo = repo
        self.token = token
        self.ref = ref

    def archive_repository(self):
        """ download and archive repo via PyGithub """
        gh = Github(self.token)
        # self.repo format: username/repository
        repo = gh.get_repo(self.repo)
        link = repo.get_archive_link("tarball", ref=self.ref)
        return urlopen(link).read()
