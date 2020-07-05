class Env:
    def __init__(self, dns, pull_secret_dir, image_file_dir, cluster_name, base_domain):
        self.__dns = dns
        self.__pull_secret_dir = pull_secret_dir
        self.__image_file_dir = image_file_dir
        self.__cluster_name = cluster_name
        self.__base_domain = base_domain

    @property
    def dns(self):
        return self.__dns

    @property 
    def image_file_dir(self):
        return self.__image_file_dir
        
    @property
    def pull_secret_dir(self):
        return self.__pull_secret_dir
        
    @property 
    def cluster_name(self):
        return self.__cluster_name
        
    @property
    def base_domain(self):
        return self.__base_domain
