Importer Module Repository
========================

Example:

>>> from importer import get_importer

>>> im = get_importer("https://gitlab.cern.ch/atrisovi/root-examples")

>>> im.archive_repository()

>>> with open("archive.tar.gz", "w") as f:

>>>    f.write(a)


