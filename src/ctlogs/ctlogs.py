# coding: utf8
""" 
@File: ctlogs.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/25 18:14
"""

import logging
from typing import Any

class CtLogger(object):
    def __ctlog_config(self):
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s %(levelname)s %(message)s',
            datefmt='%a %d %b %Y %H:%M:%S',
        )
        return logging
    
    @classmethod
    def info(cls, msg: Any):
        return cls().__ctlog_config().info(msg=msg)
    
    @classmethod
    def debug(cls, msg: Any):
        return cls().__ctlog_config().debug(msg=msg)
    
    @classmethod
    def warn(cls, msg: Any):
        return cls().__ctlog_config().warning(msg=msg)
    
    @classmethod
    def error(cls, msg: Any):
        return cls().__ctlog_config().error(msg=msg)