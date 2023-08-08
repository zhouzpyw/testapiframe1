# -*- coding: utf-8 -*- 
# @Time : 2023/8/7 7:34 
# @Author : 远望
# @File : apiutils.py 
# @desc: 处理测试用例数据
import json
import re

import allure
import jsonpath as jsonpath

from Base.debugutils import DeBugUtils
from Base.sendrequest import SendRequest
from Comm.Log import logger
from Comm.yaml_utils import YamlUtils
from Conf.setting import SYS_INI


class RequestBase:
    def __init__(self):
        self.send = SendRequest()
        self.yamlutil = YamlUtils()

    def yaml_replace_load(self, data):
        '''
        yaml数据解析替换
        :param data: 待解析替换数据
        :return: 解析替换后的数据
        '''
        str_data = data
        if not isinstance(str_data, str):
            str_data = json.dumps(data, ensure_ascii=False)
        try:
            logger.debug('-------------开始解析yaml文件里的函数调用-------------')
            for i in range(str_data.count('${')):
                if '${' in str_data and '}' in str_data:
                    start_index = str_data.index('${')
                    end_index = str_data.index('}', start_index)
                    result_all = str_data[start_index:end_index + 1]  # 获取到要处理得到字符串
                    result_fuc = str_data[start_index + 2:end_index]  # 获取到待解析数据中的函数名和参数完整表达式
                    result_fucname = result_fuc[:result_fuc.index('(')]  # 获取到待解析数据中的函数的参数
                    result_fucparams = result_fuc[result_fuc.index('(') + 1:result_fuc.index(')')]  # 将待解析数据中的函数的参数
                    # 调用getattr类反射方法调用函数，参数名以','分割
                    res = getattr(DeBugUtils(), result_fucname)(
                        *result_fucparams.split(',') if result_fucparams else "")
                    # 将结果强制转换为字符串替换回原始字符串中对应位置
                    str_data = str_data.replace(result_all, str(res))
            logger.debug('-------------解析yaml文件里的函数调用结束-------------')
        except Exception as e:
            logger.error('解析异常，请检查yaml文件格式是否正确', e)
        # 返回处理后的数据
        data = json.loads(str_data)
        return data

    def specification_yaml(self, caseinfo):
        '''
        规范测试用例数据
        :param case_info:list类型,调试取case_info[0]-->dict
        :return:
        '''
        apiname = caseinfo['baseinfo']['apiname']
        allure.attach(apiname, f'接口名称：{apiname}')
        method = caseinfo['baseinfo']['requst']['method']
        allure.attach(method, f'接口请求方式：{method}')
        url = SYS_INI['URL'] + caseinfo['baseinfo']['requst']['url']
        allure.attach(url, f'接口请求URL：{url}')
        header = caseinfo["baseinfo"]["header"]
        allure.attach(header, f'接口请求头信息：{header}')
        for i in caseinfo['testcase']:
            casename = i.pop('case_name')
            allure.attach(casename, f'用例名称：{casename}')
            validation = i.pop('validation')
            extract = i.pop('extract')
            reqdata = caseinfo['testcase']
            allure.attach(reqdata, f'接口请求数据：{reqdata}')
            response = self.send.run_apimain(case_name=casename, name=apiname, method=method, url=url,
                                             header=header, **reqdata)
            # 获取响应
            res = response.text
            # 提取响应信息

            # 提取断言数据
            # 处理断言

    def extract_data(self, testcase_extract, response):
        """
        提取接口的返回参数，支持正则表达式和json提取，提取单个或多个参数
        :param testcase_extract: testcase文件yaml中的extract值,list列表
        :param response: 接口的实际返回值,str类型
        :return:extract_data
        """
        try:
            for j in testcase_extract:
                for k, v in j.items():
                    # 处理json
                    if v.startswith('$.'):
                        extract_json = jsonpath.jsonpath(json.loads(response), v)
                        if extract_json:
                            extract_data = {k: extract_json[0]}
                            logger.info('json提取到的数据为{}'.format(extract_data))
                            self.yamlutil.yaml_write_extractyaml(extract_data)
                        else:
                            extract_data = {k: 'json未提取到数据，该接口返回结果可能为空,或yaml文件extract的json表达式错误'}
                            self.yamlutil.yaml_write_extractyaml(extract_data)
                            logger.error('json未提取到数据，该接口返回结果可能为空,或yaml文件extract的json表达式错误')
                    # 处理正则
                    else:
                        extract_data_list = re.search(v, response)
                        if extract_data_list is not None:
                            if r'(\d+)' in v or r'(\d*)' in v:
                                extract_data = {k: int(extract_data_list.group(1))}
                                logger.info('正则提取到的数据为：{}'.format(extract_data))
                                self.yamlutil.yaml_write_extractyaml(extract_data)
                            elif '(.+?)' in v or '(.*?)' in v or r'(\w+)' in v :
                                extract_data = {k: extract_data_list.group(1)}
                                logger.info('正则提取到的数据为：{}'.format(extract_data))
                                self.yamlutil.yaml_write_extractyaml(extract_data)
                        else:
                            extract_data = {k: '未提取到数据，正则提取方式不支持或错误！'}
                            logger.error('未提取到数据，该接口返回结果可能为空或正则提取方式不支持！')
                            self.yamlutil.yaml_write_extractyaml(extract_data)
        except Exception as e:
            print('接口返回值提取异常，请检查yaml文件extract表达式是否正确！',e)

    def load_header(self,type):
        '''
        返回对应请求头信息
        :param type: form,data,json
        :return: 对应的Content-Type:
        '''
        if type == 'form':
            return {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
        elif type == 'data':
            return {"Content-Type":'multipart/form-data'}
        elif type == 'json':
            return {'Content-Type': 'application/json'}
        else:
            logger.error('不支持的请求头信息')
# if __name__ == '__main__':
# # print(yaml_read('test_wx_get_token.yaml')[0]['testcase'])
# # RequestBase().specification_yaml(yaml_read('test_wx_get_token.yaml')[0])
# # print(RequestBase().yaml_replace_load(yaml_read('test_wx_get_token.yaml')[0]))
#     a = {
#     "info":
#     {
#         "time": 2018433021,
#         "token":"xiaoluo"
#     },
#     "data":
#     {
#         "year":1999,
#         "month":9,
#         "day":2
#     }
# }
#     #a = str(a)
#     a = json.dumps(a)
#     #RequestBase().extract_data([{"token":"'token': '(\w+)2'"},{"time":"'time': (\d+)"}],a)
#     RequestBase().extract_data([{"token":"$.info.token"},{"time":"$.info.time"}],a)
#     # s = [{"token":"$.info.token"},]
#     #
#     # for j in s:
#     #     for k, v in j.items():
#     #         if '$' in v:
#     #             extract_json = jsonpath.jsonpath(json.loads(a), v)
#     #             if extract_json:
#     #                 extract_json = {k:extract_json[0]}
#     #                 print(extract_json)
#     #             else:
#     #                 print('ok')