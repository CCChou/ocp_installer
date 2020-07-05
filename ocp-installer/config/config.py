class Config:
    def __init__(self, tasks, env_vars, nodes):
        self.__tasks = tasks
        self.__env_vars = env_vars
        self.__nodes = nodes

    @property 
    def tasks(self):
        return self.__tasks

    @property
    def env_vars(self):
        return self.__env_vars
        
    @property
    def nodes(self):
        return self.__nodes
