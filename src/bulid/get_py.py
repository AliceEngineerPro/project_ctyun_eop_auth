# coding: utf8
""" 
@File: get_py.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/27 2:18
"""
import os
import pathlib
from global_config import config

path = pathlib.Path(rf'{config.BASE_DIR}')
files_path = path.glob('**/*')
count_file = []
for file in files_path:
    if os.path.isdir(file):
        pass
    elif os.path.isfile(file):
        filename, extension = os.path.splitext(file)
        if extension == '.py':
            try:
                count_file.append(str(file))
            except Exception as error:
                print(error)
                break
print(count_file)