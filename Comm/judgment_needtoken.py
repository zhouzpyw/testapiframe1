# -*- coding: utf-8 -*- 
# @Time : 2023/8/6 0:15 
# @Author : 远望
# @File : judgment_needtoken.py 
# @desc:判断是否需要先获取token
from Comm.yaml_utils import yaml_read


def jn_token(filename):
    '''
    # 从yaml文件中获取是否需要获取token的标志位
    :param filename: yaml文件地址
    :return: True or False
    '''
    data = yaml_read(filename)
    if data['needtoken'] == True:
        return True
    else:
        return False