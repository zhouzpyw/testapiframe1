# -*- coding: utf-8 -*- 
# @Time : 2023/7/31 22:35 
# @Author : 远望
# @File : test_baseapi.py
# @desc:封装方法统一接口,所有请求从这里调用
import allure
import pytest
from Comm.base_assert import AssertAll
from Comm.driverallfuc import sendfucname, driveallfuc
from Comm.yaml_utils import yaml_apiload, yaml_elseinfo, yaml_clear, yaml_write, yaml_case_info, yaml_case_data
from Conf.config import read_ini_file

@pytest.mark.usefixtures('loggers')  #实例初始化日志类
class TestBaseApi(AssertAll):
    ##获取要测试的类中所有的自定义方法名并遍历
    for basefucname in sendfucname('Case.wxgzh','WxGzh'):
        # 根据函数名加载接口对应yaml文件名
        yamlfilename = yaml_apiload(basefucname)['yamlfilename']
        # 获取接口描述
        apidescription = yaml_apiload(basefucname)['apidescription']
        # 加载yaml配置文件中数据驱动外其他配置
        loadyamlconfig = yaml_elseinfo(yamlfilename)
        # 读取yaml配置文件中的模块名
        modulename = loadyamlconfig['feature']
        # 读取yaml配置文件的story
        yamlstory = loadyamlconfig['story']
        # 读取yaml配置文件的description
        yamldescription = loadyamlconfig['description']
        # 读取yaml配置文件中请求方式
        apimethod = loadyamlconfig['requst']['method']
        # 读取yaml配置文件中URL
        apiurltemp = loadyamlconfig['requst']['url']
        # 获取系统中基础url
        baseurl = read_ini_file('sys','base_url')
        # 拼接url得到最终的url
        apiurl = baseurl+apiurltemp
        # 读取断言相关配置
        getvalidate = loadyamlconfig['validate']
        # 读取提取数据相关配置
        getextract = loadyamlconfig['extract']
        @allure.feature(modulename)
        @allure.story(yamlstory)
        @allure.title('{title}')
        @allure.description(yamldescription)
        @pytest.mark.parametrize(yaml_case_info(yamlfilename),yaml_case_data(yamlfilename))
        def test_base_api(self,loggers, number, title, exceptresult, form,data):
            # 调用函数
            basefuc = driveallfuc(self.yamlfilename,'Case.wxgzh', 'WxGzh', method=self.apimethod, url=self.apiurl,form=form,data=data)
            loggers.info('测试接口{0}......'.format(self.basefucname))
            loggers.info('开始执行第{0}条用例，用例标题为：{1}'.format(number, title))
            # 调用方法结果赋值给response
            response = basefuc
            try:
                # 根据yaml文件中相关配置，调用断言方法断言
                self.assert_choice(self.getvalidate['asserttype'], exceptresult, str(response.json().keys()))
                # 断言成功，进行下面的步骤
                loggers.debug('请求{0}，请求报文：{1}'.format(self.apidescription, response.url))
                loggers.debug('请求{0}，返回报文：{1}'.format(self.apidescription, response.json()))
                loggers.info('请求{0}成功！测试通过!'.format(self.apidescription))
                # 判断是否有中间变量需要写入yaml文件，有则写入
                if self.getextract['needif'] == True:
                    yaml_clear(self.getextract['filename'])
                    writedata = {self.getextract['datakey']: response.json()[self.getextract['datavalue']]}
                    yaml_write(self.getextract['filename'], data=writedata)
                    loggers.info('写入{0}文件成功!'.format(self.getextract['filename']))
                    loggers.info('写入的数据为{0}'.format(writedata))
            # 断言失败记录日志，抛出异常。
            except AssertionError as e:
                loggers.error('测试不通过！！！')
                loggers.error('请求{0}异常，{1}，请求报文：{2}'.format(self.apidescription, e, response.url))
                loggers.error('请求{0}异常，返回报文：{1}'.format(self.apidescription, response.json()))
                raise