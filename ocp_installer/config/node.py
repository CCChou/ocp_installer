class Node:
    def __init__(self, role, ip, name):
        self.__role = role
        self.__ip = ip
        self.__name = name

    @property
    def role(self):
        return self.__role

    @property
    def ip(self):
        return self.__ip

    @property
    def name(self):
        return self.__name
