# -*- coding: utf-8 -*- 
# @Time : 2023/7/29 1:15 
# @Author : 远望
# @File : filename_init.py
# @desc:定义日志目录生成格式
import os
import time


def log_filename_init(): #定义日志文件存放目录
    log_filename = time.strftime("%Y-%m-%d")
    return log_filename

def ishav_dir(dirpath,dirname): #判断目标路径下是否存在指定目录，不存在则创建，存在则返回指定目录
    filedir = os.path.join(dirpath,dirname)
    if os.path.exists(filedir) == True:
        return filedir
    else:
        os.mkdir(filedir)