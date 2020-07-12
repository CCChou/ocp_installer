import sys
from ocp_installer.task.taskfactory import TaskFactory
from ocp_installer.config.parser.configparser import ConfigParser


class Main:
    def exec(self):
               
        parser = ConfigParser()
        config = parser.parse(self.__get_config_data)
        task_factory = TaskFactory()
        task = task_factory.create_task(config.tasks)
        task.exec(config)

    def __check_parameter(self):
        if len(sys.argv) < 2:
            raise Exception('Please provide the config file path')

    def __get_config_data(self, config_dir):
        with open(config_dir, 'r') as file:
            return file.read()


if __name__ == "__main__":
    Main().exec()
