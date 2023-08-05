# -*- coding: utf-8 -*- 
# @Time : 2023/8/3 0:53 
# @Author : 远望
# @File : base_assert.py 
# @desc:封装断言方法


class AssertAll:
    def inner_assert(self, exceptstr, resultstr):
        '''定义断言方法（包含断言）'''
        assert exceptstr in resultstr


    def assert_choice(self,asserttype,exceptstr, resultstr):
        if asserttype == 'inner':
            return self.inner_assert(exceptstr, resultstr)
        elif asserttype == 'equal':
            pass
        else:
            pass

# a = AssertAll()
# try:
#     a.inner_assert('a','vs')
#     print('ok')
# except AssertionError as e:
#     print('erro')
#     raise e