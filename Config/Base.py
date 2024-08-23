from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from Function.LogUtils import logger
import subprocess
import configparser


class BaseElement:
    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, loc, timeout=10, poll_frequency=1):
        """
        定位单个元素
        定位到元素，返回元素对象，没定位到,超时异常

        :param loc: 定位器，元组类型，例如 ("id", "value1")
        :param timeout: 等待超时时间，默认10秒
        :param poll_frequency: 轮询频率，默认1秒
        :return: 定位到的元素对象
        :raises: NoSuchElementException: 如果元素未找到
        """
        if not isinstance(loc, tuple):
            logger.error('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
            raise TypeError('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            try:
                logger.info("正在定位元素信息：定位方式->%s, value值->%s" % (loc[0], loc[1]))
                ele = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
                    lambda x: x.find_element(*loc))
                return ele
            except NoSuchElementException as e:
                logger.error("定位元素出现问题,检查属性是否存在或者写错: %s" % str(e))
                raise


class Report:
    @staticmethod
    def allure_report(report_path, report_html):
        """
        生成Allure报告
        :param report_path: 测试结果路径
        :param report_html: 生成报告的路径
        :return: None
        """
        # 执行命令 allure generate...
        allure_cmd = "allure generate %s -o %s --clean" % (report_path, report_html)
        logger.info("报告生成命令：%s" % allure_cmd)
        try:
            subprocess.call(allure_cmd, shell=True)
            logger.info("Allure报告生成成功，报告地址：%s" % report_html)
        except subprocess.CalledProcessError as e:
            logger.error("生成Allure报告失败，请检查测试环境相关配置: %s" % str(e))
            raise

