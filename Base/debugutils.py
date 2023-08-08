# -*- coding: utf-8 -*- 
# @Time : 2023/8/8 8:46 
# @Author : 远望
# @File : debugutils.py 
# @desc:解析yaml文件所需要的方法类
import base64
import datetime
import hashlib
import time
from _sha1 import sha1


class DeBugUtils:
    def __init__(self):
        pass

    def md5_encryption(self, params):
        """参数MD5加密"""
        enc_data = hashlib.md5()
        enc_data.update(params.encode(encoding="utf-8"))
        return enc_data.hexdigest()

    def sha1_encryption(self, params):
        """参数sha1加密"""
        enc_data = sha1()
        enc_data.update(params.encode(encoding="utf-8"))
        return enc_data.hexdigest()

    def base64_encryption(self, params):
        """base64加密"""
        base_params = params.encode("utf-8")
        encr = base64.b64encode(base_params)
        return encr

    def timestamp(self):
        """获取当前时间戳，10位"""
        t = int(time.time())
        return t

    def timestamp_thirteen(self):
        """获取当前的时间戳，13位"""
        t = int(time.time()) * 1000
        return t

    def end_time(self):
        """获取当前时间标准时间格式"""
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return now_time

    def end_year_time(self):
        """获取当前时间标准时间格式，年月日"""
        now_time = datetime.datetime.now().strftime("%Y-%m-%d")
        return now_time

    def today_zero_tenstamp(self):
        """获取当天00:00:00时间戳，10位时间戳"""
        time_stamp = int(time.mktime(datetime.date.today().timetuple()))
        return time_stamp

    def today_zero_stamp(self):
        """获取当天00:00:00时间戳，13位时间戳"""
        time_stamp = int(time.mktime(datetime.date.today().timetuple())) * 1000
        return time_stamp

    def specified_zero_tamp(self, days):
        """获取当前日期指定日期的00:00:00时间戳，days：往前为负数，往后为整数"""
        tom = datetime.date.today() + datetime.timedelta(days=int(days))
        date_tamp = int(time.mktime(time.strptime(str(tom), '%Y-%m-%d'))) * 1000
        return date_tamp

    def specified_end_tamp(self, days):
        """获取当前日期指定日期的23:59:59时间戳，days：往前为负数，往后为整数"""
        tom = datetime.date.today() + datetime.timedelta(days=int(days) + 1)
        date_tamp = int(time.mktime(time.strptime(str(tom), '%Y-%m-%d'))) - 1
        return date_tamp * 1000

    def today_end_stamp(self):
        """获取当天23:59:59时间戳"""
        # 今天日期
        today = datetime.date.today()
        # 明天日期
        tomorrow = today + datetime.timedelta(days=1)
        today_end_time = int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d'))) - 1
        return today_end_time * 1000

    def month_start_time(self):
        """获取本月第一天标准时间，年月日"""
        # 今天日期
        now = datetime.datetime.now()
        this_month_start = datetime.datetime(now.year, now.month, 1).strftime("%Y-%m-%d")
        return this_month_start

    def month_first_time(self):
        """本月1号00:00:00时间戳，13位"""
        # 今天日期
        now = datetime.datetime.now()
        # 本月第一天日期
        this_month_start = datetime.datetime(now.year, now.month, 1)
        first_time_stamp = int(time.mktime(this_month_start.timetuple())) * 1000
        return first_time_stamp

    def testa(self, a, b, c):
        return [a, b, c]
