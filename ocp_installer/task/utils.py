import os

def install_pkg(pkg_name):
    exec_command(f'yum install -y {pkg_name}')

def enable_service(service_name):
    exec_command(f'systemctl enable {service_name}')

def restart_service(service_name):
    exec_command(f'systemctl restart {service_name}')

def exec_command(command):
    rv = os.system(command)
    if rv is not 0:
        raise RuntimeError()