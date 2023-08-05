# -*- coding: utf-8 -*- 
# @Time : 2023/7/31 21:56 
# @Author : 远望
# @File : yaml_utils.py
# @desc: yaml工具



#定义yaml工具类
import os
import yaml

from Conf.config import read_ini_file

yamlpath = read_ini_file('yaml','yaml_path')
# 获取配置文件中的yaml文件路径配置
yamltemppath = read_ini_file('yaml','yaml_temp_path')
# 获取配置文件中的yaml临时文件路径配置
yaml_api_yaml = read_ini_file('yaml','yaml_api_yaml')
# 获取配置文件中接口与yaml文件对应的记录文件
BaseHome = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# 获取当前目录所在的文件根目录

def yaml_write(filename,data):
    '''写入yaml，以temp结尾则视为临时变量存储'''
    if filename.endswith('temp.yaml'):
        with open(os.path.join(BaseHome, yamltemppath, filename), encoding='GBK', mode='a+') as f:
            yaml.dump(data, stream=f, allow_unicode=True)
    else:
        with open(os.path.join(BaseHome,yamlpath,filename),encoding='GBK',mode='a+') as f:
            yaml.dump(data,stream=f,allow_unicode=True)


def yaml_read(filename):
    '''读取yaml,读取全部yaml配置数据,以temp结尾则读取Temp下的临时yaml文件'''
    if filename.endswith('temp.yaml'):
        with open(os.path.join(BaseHome, yamltemppath, filename), encoding='GBK', mode='r') as f:
            value = yaml.load(f, yaml.FullLoader)
    else:
        with open(os.path.join(BaseHome,yamlpath,filename),encoding='GBK',mode='r') as f:
            value = yaml.load(f,yaml.FullLoader)
    return value


def yaml_case_info(filename):
    '''读取yaml,配置数据驱动参数，这里主要获取parametrize的数据'''
    lista = yaml_read(filename)['parametrize']
    # 提取参数名(这里取parametrize列表中第一个列表元素作为参数)
    # 提取并处理对应的参数值
    return lista[0]

def yaml_case_data(filename):
    '''读取yaml,配置数据驱动的数据，这里主要获取parametrize的数据'''
    lista  = yaml_read(filename)['parametrize']
    values = []
    for item in lista[1:]:
        values.append(dict(zip(lista[0], item)))
    headers = yaml_case_info(filename)
    test_data = []
    for value in values:
        test_data.append(tuple(value[header] for header in headers))
    return test_data
# def yaml_case_updatedata(filename,newvalue):
#     '''修改token'''
#     data = yaml_case_data(filename)
#     for i, item in enumerate(data):
#         # 生成新的元组，替换'id'后的元素
#         new_item = item[:3] + (newvalue,) + item[4:]
#         # 替换原来的元组
#         data[i] = new_item
#     return data

def yaml_elseinfo(filename):
    '''读取yaml中除数据驱动外的其他数据,返回一个字典'''
    elseinfo = yaml_read(filename)
    dictinfo = {
    'feature':elseinfo['feature'],
    'story':elseinfo['story'],
    'description': elseinfo['description'],
    'title':elseinfo['title'],
    'requst':elseinfo['requst'],
    'extract':elseinfo['extract'],
    'needif':elseinfo['extract']['needif'],
    'filename':elseinfo['extract']['filename'],
    'datakey':elseinfo['extract']['datakey'],
    'datavalue':elseinfo['extract']['datavalue'],
    'validate':elseinfo['validate'],
    'asserttype':elseinfo['validate']['asserttype'],
    'exceptresult':elseinfo['validate']['exceptresult']
    }
    return dictinfo

def yaml_apiload(apiname):
    '''获取接口对应的yaml文件，以字典形式返回'''
    yamlfilename = yaml_read(yaml_api_yaml)[apiname]['yamlfilename']
    apidescription = yaml_read(yaml_api_yaml)[apiname]['apidescription']
    dictyaml = {'apiname':apiname,'yamlfilename':yamlfilename,'apidescription':apidescription}
    return dictyaml

def yaml_clear(filename):
    '''清空yaml文件,以temp结尾则读取Temp下的临时yaml文件'''
    if filename.endswith('temp.yaml'):
        with open(os.path.join(BaseHome, yamltemppath, filename), encoding='GBK', mode='w') as f:
            f.truncate()
    else:
        with open(os.path.join(BaseHome,yamlpath,filename),encoding='GBK',mode='w') as f:
            f.truncate()

# if __name__ == '__main__':
#     #print(yaml_read('test_wx_get_token.yaml')['parametrize'])
# #     print(yaml_case_info('test_wx_get_token.yaml'))
# # #     print(yaml_case_data('test_wx_get_token.yaml'))
# #     print(yaml_case_info('test_wx_get_token.yaml'))
#     print(yaml_case_data('test_wx_create_tag.yaml'))
#     print(yaml_case_updatedata('test_wx_create_tag.yaml','a'))
# #     yamlfilename = yaml_read(yaml_api_yaml)['test_create_tag']['yamlfilename']