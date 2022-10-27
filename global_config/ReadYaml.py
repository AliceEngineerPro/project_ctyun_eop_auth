# coding: utf8
""" 
@File: ReadYaml.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/24 15:35
"""

import yaml

class ReadYamlConfig(object):
    
    def __init__(self, file: str):
        self.file = file
    
    def get_config(self, keyword: str):
        with open(file=self.file, mode='r', encoding='utf-8') as config_yaml_file:
            yaml_config = yaml.load(config_yaml_file, Loader=yaml.FullLoader)
            # return yaml_config
            try:
                return yaml_config[keyword]
            except Exception as error:
                return error
    
