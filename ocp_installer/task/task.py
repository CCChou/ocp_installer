from abc import ABCMeta, abstractmethod
from ocp_installer.config.config import Config


class Task(metaclass=ABCMeta):
    @abstractmethod
    def exec(self, config: Config):
        pass