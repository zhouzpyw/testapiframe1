# -*- coding: utf-8 -*- 
# @Time : 2023/7/2 19:30 
# @Author : 远望灬Zhouzp
# @File : Logs.py
import datetime
import os
import logging
import time
from logging.handlers import RotatingFileHandler
from Conf.setting import DIR_BASE, LOG_INI

BaseHome = DIR_BASE  # 获取当前项目根目录
log_level = LOG_INI['LOG_LEVEL']  # 获取日志级别配置
log_format = LOG_INI['LOG_FOMAT']  # 获取日志书写格式
log_formatdir = time.strftime("%Y-%m-%d")
log_path = os.path.join(BaseHome, LOG_INI['LOG_PATH'], log_formatdir)  # 获取日志存放根目录
if not os.path.exists(log_path): os.mkdir(log_path)
logfile_name = log_path + r"\test_log.txt"


class RecordLog:
    """日志模块"""

    def __init__(self):
        self.handle_overdue_log()

    def handle_overdue_log(self):
        """处理过期日志文件"""
        # 获取系统的当前时间
        now_time = datetime.datetime.now()
        # 日期偏移30天，最多保留30的日志文件，超过自动清理
        offset_date = datetime.timedelta(days=-30)
        # 获取前一天时间戳
        before_date = (now_time + offset_date).timestamp()
        # 找到目录下的文件
        files = os.listdir(log_path)
        for file in files:
            if os.path.splitext(file)[1]:
                filepath = log_path + "\\" + file
                file_create_time = os.path.getctime(filepath)  # 获取文件创建时间,返回时间戳
                if file_create_time < before_date:
                    os.remove(filepath)
                else:
                    continue

    def output_logging(self):
        """获取logger对象"""
        logger = logging.getLogger(__name__)
        # 防止重复打印日志
        if not logger.handlers:
            logger.setLevel(log_level)
            log_format = logging.Formatter(
                '%(levelname)s - %(asctime)s - %(filename)s:%(lineno)d -[%(module)s:%(funcName)s] - %(message)s')
            # 日志输出到指定文件，滚动备份日志
            fh = RotatingFileHandler(filename=logfile_name, mode='a', maxBytes=524288,
                                     backupCount=7,
                                     encoding='utf-8')  # maxBytes:控制单个日志文件的大小，单位是字节,backupCount:用于控制日志文件的数量

            fh.setLevel(log_level)
            fh.setFormatter(log_format)
            # 将相应的handler添加在logger对象中
            logger.addHandler(fh)

            # 输出到控制台
            sh = logging.StreamHandler()
            sh.setLevel(log_level)
            sh.setFormatter(log_format)
            logger.addHandler(sh)
        return logger


apilog = RecordLog()
logger = apilog.output_logging()
