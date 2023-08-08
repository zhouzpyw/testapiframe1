# -*- coding: utf-8 -*- 
# @Time : 2023/8/3 0:53 
# @Author : 远望
# @File : base_assert.py 
# @desc:封装断言方法
import allure

from Comm.Log import logger
from Comm.yaml_utils import YamlUtils


class Assertions:
    """"
    接口断言模式，支持
    1）响应文本字符串包含模式断言
    2）响应结果相等断言

    """
    def contains_assert(self, exceptresult, response):
        """
        字符串包含断言模式，断言预期结果的字符串是否包含在接口的响应信息中
        :param exceptresult: 预期结果，yaml文件的预期结果值,list
        :param response: 接口实际响应结果text格式
        :return: 返回结果的状态标识
        """
        # 断言状态标识，0成功，其他失败
        flag = 0
        temp = 0
        for i in exceptresult:
            if i in response:
                temp = 1
            else:
                temp = 2
        if temp == 1:
            allure.attach(f"预期结果应该包含的字符串有：{exceptresult}\n实际结果：{response}", '包含断言结果:成功',
                          attachment_type=allure.attachment_type.TEXT)
            logger.info("contains断言成功：预期结果应该包含的字符串有【%s】实际结果【%s】" % (exceptresult, response))
        else:
            flag += 1
            allure.attach(f"预期结果应该包含的字符串有：{exceptresult}\n实际结果：{response}", '响应代码断言结果:失败',
                          attachment_type=allure.attachment_type.TEXT)
            logger.error("contains断言失败：预期结果应该包含的字符串有【%s】实际结果【%s】" % (exceptresult, response))
        return flag

    def equal_assert(self, expected_results, actual_results, statuc_code=None):
        """
        相等断言模式
        :param expected_results: 预期结果，yaml文件validation值
        :param actual_results: 接口实际响应结果
        :return:
        """


if __name__ == '__main__':
    print(YamlUtils().yaml_read('test_wx_get_token.yaml')[0]['testcase'][0]['validation'][0]['contains'])
    a = YamlUtils().yaml_read('test_wx_get_token.yaml')[0]['testcase'][0]['validation'][0]['contains']
        #     if assert_key == "status_code":
        #         if assert_value != status_code:
        #             flag += 1
        #             allure.attach(f"预期结果：{assert_value}\n实际结果：{status_code}", '响应代码断言结果:失败',
        #                           attachment_type=allure.attachment_type.TEXT)
        #             logs.error("contains断言失败：接口返回码【%s】不等于【%s】" % (status_code, assert_value))
        #     else:
        #         resp_list = jsonpath.jsonpath(response, "$..%s" % assert_key)
        #         if isinstance(resp_list[0], str):
        #             resp_list = ''.join(resp_list)
        #         if resp_list:
        #             assert_value = None if assert_value.upper() == 'NONE' else assert_value
        #             if assert_value in resp_list:
        #                 logs.info("字符串包含断言成功：预期结果【%s】,实际结果【%s】" % (assert_value, resp_list))
        #             else:
        #                 flag = flag + 1
        #                 allure.attach(f"预期结果：{assert_value}\n实际结果：{resp_list}", '响应文本断言结果：失败',
        #                               attachment_type=allure.attachment_type.TEXT)
        #                 logs.error("响应文本断言失败：预期结果为【%s】,实际结果为【%s】" % (assert_value, resp_list))
        # return flag
    Assertions().contains_assert(a,'asssss{"access_token":"ACCESS_TOKEN","expires_in":7200}sssssssssssssss')