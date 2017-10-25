import gitlab
from base_importer import BaseImporter


class GitlabImporter(BaseImporter):

    def __init__(self, repo, ref=None, token=None):
        self.repo = repo
        self.token = token
        self.ref = ref  # branch/tag/commit

    def archive_repository(self):
        """ download and archive repo via python-gitlab """
        gl = gitlab.Gitlab('https://gitlab.cern.ch', self.token, api_version=4)
        repo = gl.projects.get(self.repo)
        tgz = repo.repository_archive(self.ref)
        return tgz
