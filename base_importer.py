from abc import ABCMeta, abstractmethod


class BaseImporter:
    __metaclass__ = ABCMeta

    @abstractmethod
    def archive_repository(self):
        pass
