import yaml

with open('./config.yml', 'r') as stream:
    data = yaml.load(stream)

print(data)
print(type(data))