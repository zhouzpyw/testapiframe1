# -*- coding: utf-8 -*- 
# @Time : 2023/8/6 0:15 
# @Author : 远望
# @File : judgment_needtoken.py 
# @desc:判断是否需要先获取token
from Comm.yaml_utils import yaml_read


def jn_token(filename):
    # 从yaml文件中获取是否需要的标志位
    data = yaml_read(filename)
    if data['needtoken'] == True:
        return True
    else:
        return False
# if __name__ == '__main__':
#     print(jn_token('test_wx_get_token.yaml'))
#     if jn_token('test_wx_get_token.yaml') == True:
#         print('ok')