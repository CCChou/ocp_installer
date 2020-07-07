from ocp_installer.task.task import Task
import ocp_installer.task.utils as utils


class HttpServerTask(Task):
    def exec(self):
        service_name = 'httpd'
        utils.install_pkg(service_name)
        self.__change_listen_port()
        utils.enable_service(service_name)
        utils.restart_service(service_name)

    def __change_listen_port(self):
        dir = '/etc/httpd/conf/httpd.conf'
        with open(dir, 'r') as file:
            data = file.read()
        
        data.replace('Listen 80', 'Listen 8080')
        with open(dir, 'w') as file:
            file.write(data)
        