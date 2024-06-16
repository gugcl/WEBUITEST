import os
from Function.YamlUtils import YamlReader


# 1、获取项目基本目录
# 获取当前项目的绝对路径
current = os.path.abspath(__file__)
# print(current)
BASE_DIR = os.path.dirname(os.path.dirname(current))
# print(BASE_DIR)

# 定义config目录的路径
_config_path = BASE_DIR + os.sep + "Config"

# 定义conf.yml文件的路径
_config_file = _config_path + os.sep + "conf.yml"

# 定义log文件路径
_log_path = BASE_DIR + os.sep + "Log"

# 定义report目录的路径
_report_path = BASE_DIR + os.sep + "Report"

# 定义data目录的路径
_data_path = BASE_DIR + os.sep + "data"


def get_report_path():
    """
    获取report绝对路径
    :return:
    """
    return _report_path


def get_data_path():
    return _data_path


def get_config_path():
    return _config_path


def get_config_file():
    return _config_file


def get_log_path():
    """
    获取Log文件路径
    :return:
    """
    return _log_path


# 2、读取配置文件
# 创建类
class ConfigYaml:

    # 初始yaml读取配置文件
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()

    # 定义方法获取需要信息

    def get_conf_url(self):
        return self.config["BASE"]["test"]["url"]

    def get_conf_log(self):
        """
        获取日志级别
        :return:
        """
        return self.config["BASE"]["log_level"]

    def get_conf_log_extension(self):
        """
        获取文件扩展名
        :return:
        """
        return self.config["BASE"]["log_extension"]

    def get_email_info(self):
        """
        获取邮件配置相关信息
        :return:
        """
        return self.config["email"]



