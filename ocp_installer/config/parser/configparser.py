from ocp_installer.config.config import Config
from ocp_installer.config.task import Task
from ocp_installer.config.env import Env
from ocp_installer.config.node import Node


class ConfigParser:
    def parse(self, yaml_config: dict):
        print('start parse')
        tasks = self.parse_tasks(yaml_config)
        env_vars = self.parse_env(yaml_config)
        nodes = self.parse_nodes(yaml_config)
        return Config(tasks, env_vars, nodes)

    def parse_tasks(self, yaml_config: dict):
        return [Task(t['name']) for t in yaml_config['tasks']]

    def parse_env(self, yaml_config: dict):
        env = yaml_config['env']
        return Env(env['dns'], env['pull-secret-dir'], env['image-file-dir'], env['cluster-name'], env['base-domain'], env['ocp-client-dir'], env['ocp-installer-dir'])

    def parse_nodes(self, yaml_config: dict):
        nodes = []
        nodes.extend([Node('master', n['ip'], n['name']) for n in yaml_config['nodes']['master']])
        nodes.extend([Node('worker', n['ip'], n['name']) for n in yaml_config['nodes']['worker']])
        nodes.extend([Node('bootstrap', n['ip'], n['name']) for n in yaml_config['nodes']['bootstrap']])
        nodes.extend([Node('bastion', n['ip'], n['name']) for n in yaml_config['nodes']['bastion']])
        return nodes
