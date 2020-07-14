# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/5/10 7:50 
@Auth : 杨哲
@File : handle_config.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
from configparser import ConfigParser
from Common.constants import LOG_CONFIG_PATH, REPORT_CONFIG_PATH


class HandleConfig:
    """

    """

    def __init__(self, filename):
        self.filename = filename
        self.config = ConfigParser()
        self.config.read(self.filename, encoding="utf-8")

    def get_value(self, section, option):
        return self.config.get(section, option)

    def get_int(self, section, option):
        return self.config.getint(section, option)

    def get_float(self, section, option):
        return self.config.getfloat(section, option)

    def get_boolean(self, section, option):
        return self.config.getboolean(section, option)

    def get_eval_data(self, section, option):
        return eval(self.get_value(section, option))

    @staticmethod
    def write_config(datas, filename):
        if isinstance(datas, dict):
            for value in datas.values():
                if not isinstance(value, dict):
                    return "数据不合法，应为嵌套字典的字典"
            # 这里要循环完了才证明数据合法
            config = ConfigParser()
            for key in datas:
                config[key] = datas[key]
            with open(filename, "w") as file:
                config.write(file)


log_config_filename = LOG_CONFIG_PATH
log_config = HandleConfig(log_config_filename)
report_config_filename = REPORT_CONFIG_PATH
report_config = HandleConfig(report_config_filename)

if __name__ == '__main__':
    result = log_config.get_value("log", "log_filename")
    print(result)
