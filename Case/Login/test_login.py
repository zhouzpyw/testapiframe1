# -*- coding: utf-8 -*-
# @Time : 2023/7/31 21:55
# @Author : 远望
# @File : test_login.py
# @desc:测试获取access_token
import pytest

from Base.apiutils import RequestBase
from Comm.yaml_utils import YamlUtils


class TestLogin:
    @pytest.mark.parametrize('caseinfo', YamlUtils().yaml_read('test_wx_get_token.yaml'))
    def test_get_access_token(self, caseinfo):
        """
        获取access_token接口
        """
        return RequestBase().specification_yaml(caseinfo)
