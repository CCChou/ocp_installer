class Node:
    def __init__(self, role, ip, name, domain):
        self.__role = role
        self.__ip = ip
        self.__name = name
        self.__domain = domain

    @property
    def role(self):
        return self.__role

    @property
    def ip(self):
        return self.__ip

    @property
    def name(self):
        return self.__name

    @property 
    def domain(self):
        return self.__domain
