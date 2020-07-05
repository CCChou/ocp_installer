from ocp_installer.config.config import Config
from ocp_installer.config.task import Task
from ocp_installer.config.env import Env
from ocp_installer.config.node import Node


class ConfigParser:
    def parse(self, yaml_config: dict):
        tasks = self.parse_tasks(yaml_config)
        env_vars = self.parse_env_vars(yaml_config)
        nodes = self.parse_nodes(yaml_config)
        return Config(tasks, env_vars, nodes)

    def parse_tasks(self, yaml_config: dict):
        return [Task(t['name']) for t in yaml_config['tasks']]

    def parse_env_vars(self, yaml_config: dict):
        env_vars = yaml_config['env']
        return Env(env_vars['dns'], env_vars['pull-secret-dir'], env_vars['image-file-dir'], env_vars['cluster-name'], env_vars['base-domain'])

    def parse_nodes(self, yaml_config: dict):
        nodes = []
        nodes.append([Node('master', n['ip'], n['name']) for n in yaml_config['nodes']['master']])
        nodes.append([Node('worker', n['ip'], n['name']) for n in yaml_config['nodes']['worker']])
        nodes.append([Node('bootstrap', n['ip'], n['name']) for n in yaml_config['nodes']['bootstrap']])
        nodes.append([Node('bastion', n['ip'], n['name']) for n in yaml_config['nodes']['bastion']])
        return nodes
