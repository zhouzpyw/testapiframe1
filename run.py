# -*- coding: utf-8 -*- 
# @Time : 2023/8/3 3:05 
# @Author : 远望
# @File : run.py 
# @desc:
import os
import pytest


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--clean-alluredir', '--alluredir=./Report/xml'])
    os.system(r"copy .\environment.properties .\Report\xml\environment.properties")
    os.system(r"allure generate --clean ./Report/xml -o ./Report/html")
    os.system(r"allure open -h 127.0.0.1 -p 8088 ./Report/html")
