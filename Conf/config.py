# -*- coding: utf-8 -*- 
# @Time : 2023/7/2 17:08 
# @Author : 远望灬Zhouzp
# @File : config.py

import os
from configparser import ConfigParser


def read_ini_file(sec, opt):
    '''
    获取指定节中指定配置项的值
    :param sec: config.ini文件中的section
    :param opt: config.ini文件中的option
    :return: 指定section下指定option的值
    '''
    # 使用相对目录确定文件位置
    conf_dir = os.path.dirname(__file__)  # 获取当前文件所在目录
    conf_file = os.path.join(conf_dir, 'config.ini')  # 获取配置文件所在位置
    # 实例化ConfigParser类，读取配置文件
    config = ConfigParser()
    config.read(conf_file, encoding='UTF-8')
    # 读取配置文件中所有配置
    # 获取所有节的列表
    sections = config.sections()
    int_result = {}  # 所有配置项以字典形式保存
    for section in sections:
        section_dict = {}
        options = config.options(section)
        for option in options:
            value = config.get(section, option, raw=True)
            section_dict[option] = value
        int_result[section] = section_dict
    try:
        inivalue = int_result.get(sec).get(opt)  # 节和option分别作为key
        return inivalue
    except AttributeError:
        # 处理字典中的键不存在或值为None的情况
        return None
    except Exception as e:
        # 处理其他异常
        print("发生了异常:", e)
        return None
