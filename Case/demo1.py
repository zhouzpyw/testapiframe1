# -*- coding: utf-8 -*- 
# @Time : 2023/8/6 1:29 
# @Author : 远望
# @File : demo1.py 
# @desc:
# a = {'form':[['a','b','c','d','e','f'],[1,2,3,4,5,6],[7,8,9,10,11,12]],'data':[['q','w'],[11,12],[15,16]]}
# #1.dict1为：form 中abc为key,对应值为1，2，3，7，8，9，如[{'a':1,'b':2,'c':3},{'a':7,'b':8,'c':9}]
# #2.form 中def组合后作为key，如[{'d':4,'e':5,'f':6},{{'d':10,'e':11,'f':12}}]
# #3.data将其转换为[{'q':11,'w':12},{'q':15,'w':16}]
import pytest

# lista = {'form': [['number', 'title', 'exceptresult', 'grant_type', 'appid', 'secret'], [1, '正例，access_token不为空', 'access_token', 'client_credential', 'wxc2007f0b1387d1ea', 'e3a83fc0db6d79fb5900559bcdd324a4'], [2, '获取token失败', 'access_token', 'client_credential', 'wxc2007f0b1387d1ea2', 'e3a83fc0db6d79fb5900559bcdd324a4'], [3, '正例，成功获取到access_token,入参数据全部正确', 'id', '', '', ''], [4, '反例，标签名为空', 'id', '', '', '']], 'data': [['tag', 'name'], ['tag', '广东'], ['', '北京']]}
#
# params_form = []
# keys_form = lista['form'][0]
# for values in lista['form'][1:]:
#     params_dict = dict(zip(keys_form, values))
#     new_dict = params_dict.copy()
#     new_dict['form_params'] = {'grant_type': new_dict.pop('grant_type'),
#                                'appid': new_dict.pop('appid'),
#                                'secret': new_dict.pop('secret')}
#     params_form.append(new_dict)
#
# params_data = []
# keys_data = lista['data'][0]
# for values in lista['data'][1:]:
#     params_dict = dict(zip(keys_data, values))
#     params_data.append(params_dict)
#
# print(params_data)
#
# params = []
# for form in params_form:
#     for data in params_data:
#         param = form.copy()
#         param['data'] = data
#         params.append(param)
# print(params)
# @pytest.mark.parametrize('number,title,exceptresult,form_params,data', params)
# def test_func(number, title, exceptresult, form_params, data):
#     # your test function here
#     pass
# 原始数据
data = [(1, '正例，成功获取到access_token,入参数据全部正确', 'id', '', {'tag': {'name': '广东'}}), (2, '获取token失败', 'id', '', {'tag': {'name': '广东'}}), (3, '反例，标签名为空', 'id', '', {'': {'name': '广东'}})]

# 遍历数据
for i, item in enumerate(data):
  # 生成新的元组，替换'id'后的元素
  new_item = item[:3] + ('new value',) + item[4:]
  # 替换原来的元组
  data[i] = new_item

print(data)
