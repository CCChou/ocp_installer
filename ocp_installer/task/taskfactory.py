from ocp_installer.task.dnstask import DNSTask
from ocp_installer.task.loadbalancetask import LoadBalanceTask
from ocp_installer.task.httpservertask import HttpServerTask
from ocp_installer.task.ocptask import OCPTask
from ocp_installer.task.compositetask import CompositeTask


class TaskFactory:
    def create_task(self, tasks):
        composite_task = CompositeTask()
        for task in tasks:
            composite_task.add_task(self.__get_instance(task.name))
        return composite_task

    def __get_instance(self, class_name):
        class_obj = globals()[class_name + 'Task']
        return class_obj()

