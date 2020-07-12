from ocp_installer.task.dnstask import DNSTask
from ocp_installer.task.loadbalancetask import LoadBalanceTask
from ocp_installer.task.httpservertask import HttpServerTask
from ocp_installer.task.ocptask import OCPTask
from ocp_installer.task.compositetask import CompositeTask


class TaskFactory:
    def create_task(self, task_names):
        task = CompositeTask()
        for task_name in task_names:
            task.add_task(self.__get_instance(task_name))
        return task

    def __get_instance(self, class_name):
        class_obj = globals()[class_name]
        return class_obj()