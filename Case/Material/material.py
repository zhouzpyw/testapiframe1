# -*- coding: utf-8 -*- 
# @Time : 2023/8/7 5:43 
# @Author : 远望
# @File : material.py 
# @desc:


# '''新增素材'''
# def test_add_material(self):
#     method = 'POST'
#     url = TestWxGzh.baseurl + '/cgi-bin/media/uploadimg'
#     headers = {
#    'Content-type': 'multipart/form-Casedata;'}
#     data1 = {
#         'access_token':TestWxGzh.access_token,
#         'type':'image'
#     }
#     data2 = {
#         'media': open(r'D:\myname.jpg','rb')
#     }
#     response = requests.request(method=method, headers=headers, url=url,params=data1,files=data2)
#     if response.json().__contains__('url'):
#         TestWxGzh.logger.debug('请求新增素材接口，请求地址：{0}'.format(url))
#         TestWxGzh.logger.debug('请求新增素材接口，返回报文：{0}'.format(response.json()))
#         TestWxGzh.logger.info('请求新增素材接口成功！返回数据是：{0}'.format(response.json()))
#         return response.json()
#     else:
#         TestWxGzh.logger.error('请求新增素材接口异常，请求地址：{0}'.format(url))
#         TestWxGzh.logger.error('请求新增素材接口异常，返回报文：{0}'.format(response.json()))
#         return response.json()
#
# '''获取素材列表'''
# def test_get_add_material_list(self):
#     method = 'POST'
#     url = TestWxGzh.baseurl + '/cgi-bin/material/batchget_material'
#     headers = {'Content-Type': 'application/json;charset=utf8'}
#     data1 = {
#         'access_token': TestWxGzh.access_token
#     }
#     data2 = {
#         "type":'image',    #素材的类型，图片（image）、视频（video）、语音 （voice）、图文（news）
#         "offset":0,    #从全部素材的该偏移位置开始返回，0表示从第一个素材 返回
#         "count":20   #返回素材的数量，取值在1到20之间
#     }
#     response = requests.request(method=method,headers=headers,url=url,json=data2,params=data1)
#     if response.json().__contains__('total_count'):
#         TestWxGzh.logger.debug('请求获取素材列表接口，请求地址：{0}'.format(url))
#         TestWxGzh.logger.debug('请求获取素材列表接口，返回报文：{0}'.format(response.json()))
#         TestWxGzh.logger.info('请求获取素材列表接口成功！返回数据是：{0}'.format(response.json()))
#         return response.json()
#     else:
#         TestWxGzh.logger.error('请求获取素材列表接口异常，请求地址：{0}'.format(url))
#         TestWxGzh.logger.error('请求获取素材列表接口异常，返回报文：{0}'.format(response.json()))
#         return response.json()
#