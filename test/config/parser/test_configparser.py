import unittest
import yaml
from ocp_installer.config.parser.configparser import ConfigParser


class ConfigParserTest(unittest.TestCase):
    def setUp(self):
        self.__parser = ConfigParser()
        self.__data = self.load_config()
    
    def load_config(self):
        with open('./config.yml', 'r') as stream:
            data = yaml.load(stream)
        return data
    
    def test_parse_tasks(self):
        tasks = self.__parser.parse_tasks(self.__data)
        assert tasks[0].name == 'dns'
        assert tasks[1].name == 'load-balance'
        assert tasks[2].name == 'http-server'
        assert tasks[3].name == 'ocp-prepare'

    def test_parse_env(self):
        env = self.__parser.parse_env(self.__data)
        assert env.dns == '8.8.8.8'
        assert env.pull_secret_dir == '/root/pull-secret'
        assert env.image_file_dir == '/root/rhcos.raw.gz'
        assert env.cluster_name == 'ibm'
        assert env.base_domain == 'cp.example'
        
    def test_parse_nodes(self):
        nodes = self.__parser.parse_nodes(self.__data)
        assert nodes is not None


if __name__ == '__main__':
    unittest.main()