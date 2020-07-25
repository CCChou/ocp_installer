import jinja2
import os
import shutil
import re
from distutils.dir_util import copy_tree
from ocp_installer.task.task import Task
from ocp_installer.config.config import Config
import ocp_installer.task.utils as utils


class OCPTask(Task):
    def __init__(self):
        self.__install_dir = '~/ocp4'

    def exec(self, config: Config):
        utils.exec_command("ssh-keygen -q -t rsa -N '' -f ~/.ssh/id_rsa <<<y 2>&1 >/dev/null")
        utils.exec_command(f'tar zxvf {config.env} -C /usr/local/bin/')
        utils.exec_command(f'tar zxvf {config.env} -C /usr/local/bin/')
        self.__generate_config(config)
        self.__create_new_install_dir()
        utils.exec_command('openshift-installer create manifests --dir=~/ocp4')
        self.__modify_manifests_config()
        utils.exec_command('openshift-installer create ignition-configs --dir=~/ocp4')
        self.__move_resources_to_httpd()
        utils.exec_command('chmod 644 /var/www/html/*')
    
    def __generate_config(self, config):
        pull_secret_dir = config.env.pull_secret_dir
        pull_secret = self.__get_pull_secret(pull_secret_dir)
        sshkey = self.__get_sshkey()
        master_count = self.__get_master_count(config)

        with open('./templates/install_config.j2', 'r') as stream:
            template = jinja2.Template(stream.read())

        with open(f'{self.__install_dir}/install_config.yaml', 'w') as file:
            file.write(template.render(env = config.env, pull_secret = pull_secret, sshkey = sshkey, master_count = master_count))

    def __get_pull_secret(self, pull_secret_dir):
        with open(pull_secret_dir, 'r') as file:
            return file.read()

    def __get_sshkey(self):
        with open('~/.ssh/id_rsa.pub', 'r') as file:
            return file.read()
        
    def __get_master_count(self, config):
        count = 0
        for node in config.nodes:
            if node.role == 'master':
                count += 1
        return count

    def __create_new_install_dir(self):
        dirpath = '~/ocp4'
        if os.path.exists(dirpath) and os.path.isdir(dirpath):
            shutil.rmtree(dirpath)
        os.mkdir(dirpath)
    
    def __modify_manifests_config(self):
        manifests_dir = ''
        content = ''
        regex = '^[\\s]*mastersSchedulable:'
        with open(manifests_dir, 'r') as file:
            line = file.readline()
            if re.match(regex, line):
                line.replace('true', 'false')
            content += line
            
        with open(manifests_dir, 'w') as file:
            file.write(content)

    def __move_resources_to_httpd(self):
        from_dir = self.__install_dir
        to_dir = '/var/html/www'
        copy_tree(from_dir, to_dir)
