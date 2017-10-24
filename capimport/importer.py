from __future__ import generators
from abc import ABCMeta, abstractmethod

from utils import parse_url


class Importer:
    __metaclass__ = ABCMeta

    @staticmethod
    def factory(url, token=None):
        host, user, repo = parse_url(url)
        repo_name = "/".join([user, repo])

        if "gitlab" in host:
            from gitlab_importer import GitlabImporter
            gli = GitlabImporter(repo_name, token=None)
            return gli

        if "github" in host:
            from github_importer import GithubImporter
            ghi = GithubImporter(repo_name, token=None)
            return ghi

    @abstractmethod
    def archive_repository(self):
        pass
