# -*- coding: utf-8 -*- 
# @Time : 2023/8/7 5:47 
# @Author : 远望
# @File : sendrequest.py 
# @desc:封装请求方法
import requests
from Conf import setting


class SendRequest:

    def send_request(self, **kwargs):
        '''
        发起请求
        :param kwargs:
        :return: res
        '''
        session = requests.session()
        res = session.request(**kwargs)
        return res

    def run_apimain(self, name, url, case_name, method, header, cookies=None, file=None, **kwargs):
        """
        接口请求
        :param name: 接口名
        :param url: 接口地址
        :param case_name: 测试用例名称
        :param casenum: 测试用例编号
        :param header:请求头
        :param method:请求方法
        :param cookies：默认为空
        :param file: 上传文件接口
        :param kwargs: 请求参数，根据yaml文件的参数类型
        :return:
        """
        response = self.send_request(method=method,
                                     url=url,
                                     headers=header,
                                     cookies=cookies,
                                     files=file,
                                     timeout=setting.API_TIMEOUT,
                                     # verify=False,
                                     **kwargs)
        return response
