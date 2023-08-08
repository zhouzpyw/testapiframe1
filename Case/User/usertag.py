# -*- coding: utf-8 -*- 
# @Time : 2023/8/7 5:42 
# @Author : 远望
# @File : usertag.py 
# @desc:


def test_create_tag(self, method, url, dataform, data):
    '''用户标签管理-创建标签接口'''
    headers = {'Content-Type': 'application/json;charset=utf8'}
    response = requests.request(method=method, headers=headers, url=url, params=dataform, json=data)
    return response
# '''获取公众号已创建的标签'''
# def test_select_tag(self):
#     method = 'GET'
#     url = TestWxGzh.baseurl + '/cgi-bin/tags/get'
#     headers = {'Content-Type': 'application/json;charset=utf8'}
#     data = {
#         'access_token': TestWxGzh.access_token
#     }
#     response = requests.request(method=method, headers=headers, url=url,params=data)
#     if response.json().__contains__('tags'):
#         TestWxGzh.logger.debug('请求获取公众号已创建的标签接口，请求地址：{0}'.format(url))
#         TestWxGzh.logger.debug('请求获取公众号已创建的标签接口，返回报文：{0}'.format(response.json()))
#         return response.json()
#     else:
#         TestWxGzh.logger.error('请求获取公众号已创建的标签接口异常，请求地址：{0}'.format(url))
#         TestWxGzh.logger.error('请求获取公众号已创建的标签接口异常，返回报文：{0}'.format(response.json()))
#         return response.json()
#