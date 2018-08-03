import yaml
from dotmap import DotMap


with open('../config.yaml', 'r') as f:
    config = DotMap(yaml.load(f))
