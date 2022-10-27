# coding: utf8
""" 
@File: create_headers.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/25 18:16
"""
from typing import Union

from global_config import config
from datetime import datetime
import uuid, random, base64, hmac, json
from hashlib import sha256


class CreateHeaders(object):

    def __init__(self):
        self.__ymd: str = datetime.now().strftime('%Y%m%d')
        self.__hms: str = datetime.now().strftime('%H%M%S')
        self.__uuid: str = str(uuid.uuid4())
        self.__random_id: str = ''.join(str(random.choice(range(10))) for _ in range(10))
        self.__ak: str = config.AK
        self.__sk: str = config.SK
        self.__host: str = 'ecx-global.ctapi.ctyun.cn'
        self.eop_date: str = f'{self.__ymd}T{self.__hms}Z'
    
    @staticmethod
    def __base64_of_hmac(data: bytes):
        return base64.b64encode(data)
    
    def __format_get_params_to_str(self, params: dict):
        sorted_data = sorted(params.items(), key=lambda x: x[0])
        str_list = map(lambda x, y: f'{x}={y}', (key[0] for key in sorted_data), (value[1] for value in sorted_data))
        return '&'.join(str_list)
    
    def __build_sign(self, get_query: dict, post_data: dict):
        query_str = self.__format_get_params_to_str(params=get_query)
        data_str = json.dumps(post_data) if post_data else ''
        hash_data = sha256(data_str.encode()).hexdigest()
        eop_auth_must_str = f'ctyun-eop-request-id:{self.__uuid}\neop-date:{self.eop_date}\n'
        eop_auth_str = f'{eop_auth_must_str}\n{query_str}\n{hash_data}'
        k_time = hmac.new(self.__sk.encode(), self.eop_date.encode(), digestmod=sha256).digest()
        k_ak = hmac.new(k_time, self.__ak.encode(), digestmod=sha256).digest()
        k_data = hmac.new(k_ak, self.__ymd.encode(), digestmod=sha256).digest()
        signature_base64 = self.__base64_of_hmac(data=hmac.new(k_data, eop_auth_str.encode(), digestmod=sha256).digest()).decode()
        eop_auth = f'{self.__ak} Headers=ctyun-eop-request-id;eop-date Signature={signature_base64}'
        return eop_auth

    def __get_headers(self, get_query: dict, post_data: dict) -> dict:
        headers = {
            'Content-Type': 'application/json',
            'ctyun-eop-request-id': self.__uuid,
            'Eop-Authorization': self.__build_sign(get_query=get_query, post_data=post_data),
            'eop-date': self.eop_date,
            'host': 'ecx-global.ctapi.ctyun.cn',
            'x-alogic-externalId': self.__random_id,
        }
        return headers

    @classmethod
    def headers(cls, get_query=None, post_data: dict=None):
        if get_query is None:
            get_query = {}
        return cls().__get_headers(get_query=get_query, post_data=post_data)
