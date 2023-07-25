import os
import configparser

repo_path = os.getcwd()


class Config:

    def __init__(self):
        self.config_path = repo_path.replace('src','config/config.ini')
        pass

    def parse_config(self):
        config = configparser.ConfigParser()
        config.read(self.config_path)
        return config['general']


