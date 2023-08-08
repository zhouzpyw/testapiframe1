# -*- coding: utf-8 -*- 
# @Time : 2023/8/7 6:18 
# @Author : 远望
# @File : setting.py 
# @desc:项目环境变量设置
import os
import sys
from Conf.config import read_ini_file

# 项目根路径
DIR_BASE = os.path.dirname(os.path.dirname(__file__))
sys.path.append(DIR_BASE)

# 接口超时时间，单位/s
API_TIMEOUT = 60

# 项目系统相关
SYS_INI = {
    'URL': read_ini_file('sys', 'base_url')
}

# 日志配置
LOG_INI = {
    'LOG_LEVEL': read_ini_file('log', 'log_level'),
    'LOG_FOMAT': read_ini_file('log', 'log_format'),
    'LOG_PATH': os.path.join(DIR_BASE, read_ini_file('log', 'log_path')),
}

# yaml配置
YAM_INI = {
    'YAML_PATH': os.path.join(DIR_BASE, read_ini_file('yaml', 'yaml_path')),
    'YAML_EXTRACT_PATH': os.path.join(DIR_BASE, read_ini_file('yaml', 'yaml_extract_path'))
}

# 默认请求头信息
LOGIN_HEADER = {
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive'
}
