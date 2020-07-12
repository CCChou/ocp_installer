import os
from ocp_installer.config.config import Config
from ocp_installer.task.task import Task

class CompositeTask(Task):
    def __init__(self):
        self.__tasks = []

    def add_task(self, task: Task):
        self.__tasks.append(task)

    def remove_task(self, task: Task):
        self.__tasks.remove(task)

    def exec(self, config: Config):
        for task in self.__tasks:
            task.exec(config)