from __future__ import generators

from utils import parse_url
from gitlab_importer import GitlabImporter
from github_importer import GithubImporter


class Importer:

    @staticmethod
    def factory(url, ref=None, token=None):
        host, user, repo = parse_url(url)
        repo_name = "/".join([user, repo])

        if "gitlab" in host:
            gli = GitlabImporter(repo_name, ref, token)
            return gli

        if "github" in host:
            ghi = GithubImporter(repo_name, ref, token)
            return ghi
