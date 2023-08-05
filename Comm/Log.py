# -*- coding: utf-8 -*- 
# @Time : 2023/7/2 19:30 
# @Author : 远望灬Zhouzp
# @File : Log.py
import os
import logging
from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler
from Comm.filename_init import log_filename_init, ishav_dir
from Conf.config import read_ini_file


BaseHome = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) #获取当前目录所在的文件根目录
log_level = eval(read_ini_file('log','log_level'))  #从配置文件中读取日志级别配置
log_path = read_ini_file('log','log_path') #从配置文件读取日志存放目录
log_format = read_ini_file('log','log_format') #从配置文件读取日志书写格式
log_filedir = log_filename_init() #日志文件存放目录
log_filedir = ishav_dir(os.path.join(BaseHome,log_path),log_filedir) #日志文件存放目录不存在则创建
log_file = os.path.join(BaseHome,log_path,log_filedir,'log.txt') #定义日志文件名



def log_init():
    logger = logging.getLogger('main')
    logger.setLevel(level=log_level) #日志级别
    formatter = logging.Formatter(log_format) #日志格式

    handler = TimedRotatingFileHandler(filename=log_file, when="D", interval=1, backupCount=7)
    handler = RotatingFileHandler(filename=log_file, maxBytes=10240, backupCount=3)

    handler.setLevel(log_level)
    handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(handler)

    console = logging.StreamHandler()
    console.setLevel(log_level)
    console.setFormatter(formatter)
    logger.addHandler(console)
    #logger.removeHandler(handler)
# # 这个日志里面，加了两个输出，handler用于向日志文件打印日志，console 用于向终端打印日志，两个的定义方式不同。
# #
# # TimedRotatingFileHandler的参数简介：
# #
# # 参数	意义	说明
# # filename	日志文件	没啥好说的
# # when	切割条件	按周(W)、天(D)、时(H)、分(M)、秒(S)切割
# # interval	间隔	就是几个when切割一次。when是W，interval是3的话就代表3周切割一次
# # backupCount	数量	就是保留几个日志文件，起过这个数量，就把最早的删除掉，从而滚动删除
# # 我这里配置的是每天生成1个日志文件，保留7天的日志。

#
# log_init()
# logger = logging.getLogger('main')
# logger.info('log test----------')
