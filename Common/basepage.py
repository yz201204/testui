# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/7/12 11:08 
@Auth : 杨哲
@File : basepage.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
import datetime
import os

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.handle_log import do_log
from Common.constants import SCREENSHOT_DIR
import time


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 等待元素可见
    def wait_element_visible(self, loc, img_doc, timeout=10, poll_frequency=0.5):
        do_log.info("在{}等待元素{}可见!".format(img_doc, loc))
        start_time = time.time()
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(loc))
        except:
            # 异常截图 - 通过截图名称，知道是哪个页面或者哪个模块出错了
            # 异常日志捕获
            do_log.error("等待元素{}可见失败!!!".format(loc))
            self.save_screenshot(img_doc)
            raise
        else:
            end_time = time.time()
            do_log.info('等待元素可见时长为：{:.5f}'.format(end_time - start_time))

    # 等待元素存在
    def wait_page_contains_element(self, loc, img_doc, timeout=10, poll_frequency=0.5):
        do_log.info("在{}等待元素{}存在!".format(img_doc, loc))
        start_time = time.time()
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(loc))
        except:
            # 异常截图 - 通过截图名称，知道是哪个页面或者哪个模块出错了
            # 异常日志捕获
            do_log.error("等待元素{}存在失败!!!".format(loc))
            self.save_screenshot(img_doc)
            raise
        else:
            end_time = time.time()
            do_log.info('等待元素存在时长为：{:.5f}'.format(end_time - start_time))

    # 查找元素
    def get_element(self, loc, img_doc, timeout=10, poll_frequency=0.5):
        self.wait_element_visible(loc, img_doc, timeout=timeout, poll_frequency=poll_frequency)
        do_log.info("在{}查找元素{}!".format(img_doc, loc))
        start_time = time.time()
        try:
            ele = self.driver.find_element(*loc)
        except:
            # 异常截图 - 通过截图名称，知道是哪个页面或者哪个模块出错了
            # 异常日志捕获
            do_log.error("查找元素{}失败!!!".format(loc))
            self.save_screenshot(img_doc)
            raise
        else:
            end_time = time.time()
            do_log.info('查找元素时长为：{:.5f}'.format(end_time - start_time))
            return ele

    # 查找多个元素
    def get_elements(self, loc, img_doc, timeout=10, poll_frequency=0.5):
        self.wait_element_visible(loc, img_doc, timeout=timeout, poll_frequency=poll_frequency)
        do_log.info("在{}查找多个元素{}!".format(img_doc, loc))
        start_time = time.time()
        try:
            eles = self.driver.find_elements(*loc)
        except:
            # 异常截图 - 通过截图名称，知道是哪个页面或者哪个模块出错了
            # 异常日志捕获
            do_log.error("查找多个元素{}失败!!!".format(loc))
            self.save_screenshot(img_doc)
            raise
        else:
            end_time = time.time()
            do_log.info('查找多个元素时长为：{:.5f}'.format(end_time - start_time))
            return eles

    # 点击元素
    def click_element(self, loc, img_doc, timeout=10, poll_frequency=0.5):
        # 元素可见、找到元素
        self.wait_element_visible(loc, img_doc, timeout=timeout, poll_frequency=poll_frequency)
        ele = self.get_element(loc, img_doc)
        do_log.info("在{}点击元素{}!".format(img_doc, loc))
        try:
            ele.click()
        except:
            # 异常截图 - 通过截图名称，知道是哪个页面或者哪个模块出错了
            # 异常日志捕获
            do_log.error("元素点击{}失败!!!".format(loc))
            self.save_screenshot(img_doc)
            raise

    # 输入文本
    def input_text(self, loc, text, img_doc, timeout=10, poll_frequency=0.5):
        self.wait_element_visible(loc, img_doc, timeout=timeout, poll_frequency=poll_frequency)
        ele = self.get_element(loc, img_doc)
        do_log.info("在{}元素{}中输入文本{}!".format(img_doc, loc, text))
        try:
            ele.send_keys(text)
        except:
            # 异常截图 - 通过截图名称，知道是哪个页面或者哪个模块出错了
            # 异常日志捕获
            do_log.error("在{}中,元素{}输入文本{}失败!!!".format(img_doc, loc, text))
            self.save_screenshot(img_doc)
            raise

    # 获取文本
    def get_element_text(self, loc, img_doc, timeout=10, poll_frequency=0.5):
        self.wait_page_contains_element(loc, img_doc, timeout=timeout, poll_frequency=poll_frequency)
        ele = self.get_element(loc, img_doc)
        do_log.info("在{}中获取元素{}的文本内容".format(img_doc, loc))
        try:
            text = ele.text
        except:
            do_log.error("在{}中获取元素{}的文本内容失败!!!".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise
        else:
            do_log.info("在{}中获取元素{}的文本内容为：{}".format(img_doc, loc, text))
            return text

    # 获取多个元素的文本值，返回列表
    def get_elements_text(self, loc, img_doc, timeout=10, poll_frequency=0.5):
        # 等待元素存在
        self.wait_page_contains_element(loc, img_doc, timeout=timeout, poll_frequency=poll_frequency)
        # 查找多个元素，返回元素为WebElement的列表
        eles = self.get_elements(loc, img_doc)
        do_log.info("在{}中获取多个元素{}的文本内容".format(img_doc, loc))
        try:
            # 创建空列表存储元素的文本值
            ele_text = []
            # 利用for循环将元素的文本值存入列表
            for ele in eles:
                text = ele.text
                ele_text.append(text)
        except:
            do_log.error("在{}中获取多个元素{}的文本内容失败!!!".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise
        else:
            do_log.info("在{}中获取多个元素{}的文本内容列表为：{}".format(img_doc, loc, ele_text))
        return ele_text

    # 获取属性
    def get_element_attr(self, loc, name, img_doc, timeout=10, poll_frequency=0.5):
        self.wait_page_contains_element(loc, img_doc, timeout=timeout, poll_frequency=poll_frequency)
        ele = self.get_element(loc, img_doc)
        do_log.info("在{}中获取元素{}的{}属性".format(img_doc, loc, name))
        try:
            attr = ele.get_attribute(name)
        except:
            do_log.error("在{}中获取元素{}的属性{}失败!!!".format(img_doc, loc, name))
            self.save_screenshot(img_doc)
            raise
        else:
            do_log.info("在{}中获取元素{}的{}属性的值为：{}".format(img_doc, loc, name, attr))
            return attr

    def save_screenshot(self, img_doc):
        time_str = datetime.datetime.now().strftime('%Y-%m-%d %H%M%S')
        filename = "{}_{}.png".format(time_str, img_doc)
        filepath = os.path.join(SCREENSHOT_DIR, filename)
        self.driver.save_screenshot(filepath)
        do_log.info("失败截图已保存，请查看文件：{}".format(filepath))

    def get_window_url(self, img_doc):
        do_log.info("获取当前窗口url")
        try:
            url = self.driver.current_url
        except:
            do_log.error("获取当前窗口url失败!!!".format(img_doc))
            self.save_screenshot(img_doc)
            raise
        else:
            return url

    # 访问url
    def visit_url(self, url, img_doc):
        do_log.info("访问{}".format(url))
        try:
            self.driver.get(url)
        except:
            do_log.info("访问{}失败，请检查url".format(url))
            self.save_screenshot(img_doc)
            raise

    def quit(self):
        do_log.info("退出浏览器!!!")
        self.driver.quit()

    def window_refresh(self):
        do_log.info("刷新页面!!!")
        self.driver.refresh()

    # 判断元素不存在
    def wait_element_invisible(self, loc, img_doc, timeout=10, poll_frequency=0.5):
        do_log.info("判断元素是否消失!!!")
        try:
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency)
            wait.until(EC.invisibility_of_element_located(loc))
        except:
            do_log.error("元素{}仍存在!!!".format(loc))
            self.save_screenshot(img_doc)
            return True
        return False


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.maximize_window()
    a = BasePage(driver)
    a.visit_url("http://www.baidu.com", "aa")
    # x = a.get_elements_text((By.XPATH, "//div[@id='lm-new']//a"), "首页")
    # print(x)
    # a.get_elements_text("1", "首页", timeout=2)
    # print(a.get_current_url("url获取"))
    a.quit()
