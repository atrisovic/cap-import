import os
import urllib
import argparse

PROTOCOL = "https:/"
ARCHIVE = "repository/master/archive.tar.gz"


def verify_url(url):
    return '/'.join([PROTOCOL, url, ARCHIVE])


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


def main():
    args = parse_args()
    download_repo(args.url, args.token, args.destination)


if __name__ == '__main__':
    main()
