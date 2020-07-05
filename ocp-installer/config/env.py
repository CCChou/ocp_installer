class Env:
    def __init__(self, dns, pull_secret, image_file, cluster_name, base_domain):
        self.__dns = dns
        self.__pull_secret = pull_secret
        self.__image_file = image_file
        self.__cluster_name = cluster_name
        self.__base_domain = base_domain

    @property
    def dns(self):
        return self.__dns

    @property 
    def image_file(self):
        return self.__image_file
        
    @property
    def pull_secret(self):
        return self.__pull_secret
        
    @property 
    def cluster_name(self):
        return self.__cluster_name
        
    @property
    def base_domain(self):
        return self.__base_domain
