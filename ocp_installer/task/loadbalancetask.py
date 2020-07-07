import jinja2
import yaml
import os
from ocp_installer.config.config import Config
from ocp_installer.task.task import Task
import ocp_installer.task.utils as utils


class LoadBalancerTask(Task):
    def exec(self, config: Config):
        service_name = 'haproxy'
        utils.install_pkg(service_name)
        self.__generate_config(config)
        utils.enable_service(service_name)
        utils.restart_service(service_name)
    
    def __generate_config(self, config):
        with open('./templates/haproxy.j2', 'r') as stream:
            template = jinja2.Template(stream.read())

        with open('/etc/haproxy/haproxy.cfg', 'a') as file:
            file.write(template.render(nodes = config.nodes))
