import urllib
from github import Github
from base_importer import BaseImporter


class GithubImporter(BaseImporter):

    def __init__(self, repo, token=None):
        self.repo = repo
        self.token = token

    def archive_repository(self):
        """ download and archive repo via PyGithub """
        gh = Github(self.token)
        # self.repo format: username/repository
        repo = gh.get_repo(self.repo)
        link = repo.get_archive_link("tarball")
        return urllib.request.urlopen(link)
