# coding: utf8
"""
@File: main.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/24 13:05
"""

from src.ctyun.edge_cloud.eip import EIP
import time
from global_config import config

if __name__ == '__main__':
    # EIP.eip_query()
    while True:
        EIP.eip_create()
        time.sleep(config.TIME['interval'])
        
