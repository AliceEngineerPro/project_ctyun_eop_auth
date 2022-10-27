# coding: utf8
""" 
@File: eip.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/25 19:22
"""

from src.ctyun.public.create_headers import CreateHeaders
from src.ctlogs.ctlogs import CtLogger
from global_config import config
import requests


class EIP(object):
    
    @staticmethod
    def eip_query():
        params = {
            'nodeCode': config.EIP_QUERY['nodeCode']
        }
        response = requests.request(
            method='GET',
            url=config.EIP_QUERY['url'],
            headers=CreateHeaders.headers(get_query=params),
            params=params
        )
        CtLogger.info(response.content.decode())
        
    @staticmethod
    def eip_create():
        data = {
            'nodeCode': config.EIP_CREATE['nodeCode'],
            'bandwidthSize': config.EIP_CREATE['bandwidthSize'],
            # 'isp': config.EIP_CREATE['isp'],
            'noBandwidthLimit': config.EIP_CREATE['noBandwidthLimit'],
            'isDualStack': config.EIP_CREATE['isDualStack'],
            'bandwidthPriceType': config.EIP_CREATE['bandwidthPriceType']
        }
        response = requests.request(
            method='POST',
            url=config.EIP_CREATE['url'],
            headers=CreateHeaders.headers(post_data=data),
            json=data,
            # verify=False
        )
        CtLogger.info(msg=response.content.decode())
        

