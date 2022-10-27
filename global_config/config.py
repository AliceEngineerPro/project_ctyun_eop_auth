# coding: utf8
""" 
@File: global_config.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/25 18:15
"""
import os
from global_config import ReadYaml

BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
__YAML_FILE: str = os.path.join(BASE_DIR, 'config.yaml')
__SETTINGS = ReadYaml.ReadYamlConfig(file=__YAML_FILE)
# 认证
__AUTHOR: dict = __SETTINGS.get_config(keyword='auth')
AK = __AUTHOR['ak']
SK = __AUTHOR['sk']
# 项目
__PRODUCT: dict = __SETTINGS.get_config(keyword='pro')
EIP_CREATE = __PRODUCT['eip_create']
# 运行
__RUN: dict = __SETTINGS.get_config(keyword='run')
TIME = __RUN.get('time')
