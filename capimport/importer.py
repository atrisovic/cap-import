import os
import re
import urllib
import argparse
import gitlab


PROTOCOL = "https:/"
ARCHIVE_GLAB = "repository/master/archive.tar.gz"
ARCHIVE_GHUB = "archive/master.tar.gz"


def verify_url(url):
    """ verify url to find host, username and repository """
    pattern = r"(?P<host>github\.com|gitlab\.cern\.ch)\/(?P<user>[a-zA-Z][\w.-]+)\/(?P<repo>[\w.-]+)"
    match = re.search(pattern, url, re.IGNORECASE)
    if not match:
        raise ValueError("The URL cannot be parsed, please provide valid URL.")
    p = match.groupdict()
    archive = ARCHIVE_GLAB if "gitlab" in p['host'] else ARCHIVE_GHUB
    if p['repo'].endswith(".git"): p['repo'] = p['repo'][:-4]
    p_list = [PROTOCOL, p['host'], p['user'], p['repo'], archive]
    return '/'.join(p_list)


def download_repo(url, token, path):
    """ download via urllib """
    if not os.path.exists(path):
        os.makedirs(path)
    location = os.path.join(path, "archive.tar.gz")
    pt = "?private_token=" + token
    urllib.urlretrieve(verify_url(url) + pt, location)


def parse_args():
    """ parse arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="The Gitlab URL")
    parser.add_argument("token", help="The Gitlab API Token")
    parser.add_argument("-d", "--destination", default=os.getcwd(), help="The destination directory.")
    return parser.parse_args()


def archive_gitlab(token, repo):
    """ download and archive repo via python-gitlab """
    gl = gitlab.Gitlab('https://gitlab.cern.ch', token, api_version=4)
    repo = gl.projects.get(repo)
    tgz = repo.repository_archive()
    with open("archive.tar.gz", "w") as f:
        f.write(tgz)

    # Labels
    # labels = project.labels.list()
    # label = project.labels.get(label_name)
    # label = project.labels.create({'name': 'foo', 'color': '#8899aa'})


def main():
    args = parse_args()
    # download_repo(args.url, args.token, args.destination)
    archive_gitlab(args.token, args.url)


if __name__ == '__main__':
    main()
