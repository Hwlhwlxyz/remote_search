import toml
import os
import sys
from pathlib import Path

root_path = os.path.dirname(sys.modules['__main__'].__file__)

def find_config_file_path():
    root_path = os.path.dirname(sys.modules['__main__'].__file__)
    home_path = str(Path.home())
    possible_path = [os.path.join(root_path, 'remote_search.toml'),
                     os.path.join(root_path, 'config.toml'),
                     os.path.join(home_path, 'remote_search.toml')]
    for p in possible_path:
        if os.path.isfile(p):
            return p

def read_toml(toml_file_name):
    config_value = None
    with open(toml_file_name) as f:
        toml_config = toml.load(f)
        config_value = toml_config.get('server')
        return toml_config

def get_toml_value():
    return read_toml(find_config_file_path())
