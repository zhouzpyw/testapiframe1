# -*- coding: utf-8 -*- 
# @Time : 2023/8/5 17:00 
# @Author : 远望
# @File : driverallfuc.py 
# @desc:封装方法，调用某一个类下所有函数，并返回对应结果。

import importlib
import json
import os

from Comm.judgment_needtoken import jn_token
from Comm.yaml_utils import yaml_read


def is_allowed(module_name, class_name):
    '''#校验类名和模块名是否合法'''
    BaseHome = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  # 获取当前目录所在的文件根目录
    filename = BaseHome + r'\configmodule.json'
    with open(filename, "r") as file:
        config = json.load(file)
    if module_name not in config["allowed_modules"]:
        print(f"ERROR: module {module_name} is not allowed.")
        return False
    if class_name not in config["allowed_classes"]:
        print(f"ERROR: class {class_name} is not allowed.")
        return False
    return True

def import_and_instantiate(module_name, class_name):
    '''导入相关模块和类名'''
    if not is_allowed(module_name, class_name):
        return None
    module = importlib.import_module(module_name)
    cls = getattr(module, class_name)
    instance = cls()
    return instance


def driveallfuc(yamlfilename,module,classname,method,url,form,data):
    # 使用
    instance = import_and_instantiate(module,classname)
    if instance is not None:
        baseclass = instance
    ##获取类中所有的自定义方法,并调用
        for method_name in dir(baseclass):
            if callable(getattr(baseclass, method_name)) and not method_name.startswith("__"):
                if jn_token(yamlfilename) == False:
                    # 使用getattr()调用方法
                    basefuc = getattr(baseclass, method_name)(method,url,form,data)
                    return basefuc
                else:
                    form = {'access_token':yaml_read('access_token_temp.yaml')['access_token']}
                    basefuc = getattr(baseclass, method_name)(method, url, form,data)
                    return basefuc
def sendfucname(module,classname):
        '''获取类中所有的自定义方法名,返回方法名列表'''
        # 使用
        list_fucname = []
        instance = import_and_instantiate(module, classname)
        if instance is not None:
            baseclass = instance
            for method_name in dir(baseclass):
                if callable(getattr(baseclass, method_name)) and not method_name.startswith("__"):
                    list_fucname.append(method_name)
        return list_fucname
if __name__ == '__main__':
    basefucname = sendfucname('Case.wxgzh','WxGzh')
    for i in basefucname:
        print(i)