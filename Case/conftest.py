# -*- coding: utf-8 -*- 
# @Time : 2023/8/1 2:55 
# @Author : 远望
# @File : conftest.py 
# @desc:定义pytest.fixture装饰器
import logging
import pytest as pytest
from Comm.Log import log_init


'''实例化日志类'''
@pytest.fixture(scope='class',autouse=True)
def loggers():
    print('实例化初始化日志类开始.......')
    log_init()
    logger = logging.getLogger('main.testapis')
    print('实例化初始化日志类结束.......')
    yield logger

