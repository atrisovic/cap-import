Importer Module Repository
========================

Example:

>>> from capimport import get_importer
>>> im = get_importer("https://gitlab.cern.ch/atrisovi/root-examples")
>>> a = im.archive_repository()
>>> with open("archive.tar.gz", "w") as f:
>>>    f.write(a)
