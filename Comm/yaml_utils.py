# -*- coding: utf-8 -*- 
# @Time : 2023/7/31 21:56 
# @Author : 远望
# @File : yaml_utils.py
# @desc: yaml文件操作方法
import os
import yaml

from Comm.Log import logger
from Conf.setting import YAM_INI


class YamlUtils:
    def __init__(self):
        # 获取配置文件中的yaml文件路径配置
        self.yamlpath = YAM_INI['YAML_PATH']

    def yaml_read(self, filename):
        '''
        读取yaml,读取全部yaml配置数据
        :param filename: 要加载的yaml文件名
        :return: yaml文件的所有数据列表
        '''
        try:
            with open(os.path.join(self.yamlpath, filename), encoding='GBK', mode='r') as f:
                value = yaml.load(f, yaml.FullLoader)
                logger.debug('读取yaml文件成功，获取到的数据：{}'.format(value))
        except Exception as e:
            logger.error('读取yaml文件异常', e)
        finally:
            f.close()
        return value

    def yaml_write_extractyaml(self, data):
        '''
        写入yaml
        :param filename: 要写入的yaml文件名
        :param data: 待写入数据
        :return:
        '''
        filename = YAM_INI['YAML_EXTRACT_PATH']
        try:
            with open(filename, encoding='GBK', mode='a+') as f:
                yaml.dump(data, stream=f, allow_unicode=True)
            logger.debug('写入extract.yaml文件成功，写入的数据：{}'.format(data))
        except Exception as e:
            logger.error('写入extract.yaml文件异常', e)
        finally:
            f.close()


# def yaml_clear(filename):
#     '''
#     清空yaml文件,以temp结尾则清空Temp下的临时yaml文件
#     :param filename:
#     :return:
#     '''
#     if filename.endswith('temp.yaml'):
#         with open(os.path.join(BaseHome, yamltemppath, filename), encoding='GBK', mode='w') as f:
#             f.truncate()
#     else:
#         with open(os.path.join(BaseHome,yamlpath,filename),encoding='GBK',mode='w') as f:
#             f.truncate()