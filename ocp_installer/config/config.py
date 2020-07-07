class Config:
    def __init__(self, tasks, env, nodes):
        self.__tasks = tasks
        self.__env = env
        self.__nodes = nodes

    @property 
    def tasks(self):
        return self.__tasks

    @property
    def env(self):
        return self.__env
        
    @property
    def nodes(self):
        return self.__nodes
