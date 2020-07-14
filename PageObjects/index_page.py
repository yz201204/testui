# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/7/11 13:21 
@Auth : 杨哲
@File : index_page.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from TestDatas import common_datas as cd
from Common.basepage import BasePage
from PageLocators.index_page_locs import IndexLocators as loc


class IndexPage(BasePage):

    # def __init__(self, driver: WebDriver):
    #     self.driver = driver
    #     self.wait = WebDriverWait(self.driver, 20)

    def if_user_is_exist(self):
        """
        用户元素是否存在，存在返回true，不存在返回false
        :return:
        """
        try:
            self.wait_element_visible(loc.user_logo, "首页_等待用户logo元素存在")
        except:
            return False
        else:
            return True

    def if_course_is_exsits(self, course_id):
        course_link = (loc.course_id[0], loc.course_id[1].format(course_id))
        try:
            self.wait_element_visible(course_link, "登陆页面_判断加入的课程存在")
        except:
            return False
        else:
            return True

    def if_course_is_not_exsits(self, course_id):
        course_link = (loc.course_id[0], loc.course_id[1].format(course_id))
        try:
            # 元素不可见返回False，可见返回True，并抛出异常
            bool_1 = self.wait_element_invisible(course_link, "登陆页面_判断加入的课程不存在")
        except:
            pass
        else:
            return bool_1

    def get_current_url(self):
        return self.get_window_url("获取首页url信息")

    # 重新访问首页
    def get_url(self):
        return self.visit_url(cd.index_url, "重新访问首页")

    def add_in_course(self, code):
        # try:
        #     self.wait.until(EC.visibility_of_element_located(loc.add_in_course))
        #     self.driver.find_element(*loc.add_in_course).click()
        #     self.wait.until(EC.visibility_of_element_located(loc.add_course_code))
        #     self.driver.find_element(*loc.add_course_code).send_keys(code)
        #     self.driver.find_element(*loc.add_course_button).click()
        # except TimeoutError:
        #     return False
        # else:
        #     return True
        self.click_element(loc.add_in_course, "首页_点击加入课程")
        self.input_text(loc.add_course_code, code, "首页_输入加课码")
        self.click_element(loc.add_course_button, "首页_点击加课按钮")

    def enter_class(self, course_id):
        # 课程名称loc格式化
        loc1 = (loc.course_name_link[0], loc.course_name_link[1].format(course_id))
        # self.wait.until(EC.visibility_of_element_located(loc1))
        # self.driver.find_element(*loc1).click()
        self.click_element(loc1, "首页_点击课程名称链接进入课程")

    def quit_class(self, course_id):
        # 更多按钮loc格式化
        loc_more_button = (loc.more_button[0], loc.more_button[1].format(course_id))
        # 退课按钮loc格式化
        loc_quit_button = (loc.quit_button[0], loc.quit_button[1].format(course_id))
        # self.wait.until(EC.visibility_of_element_located(loc_more_button))
        # self.driver.find_element(*loc_more_button).click()
        # self.wait.until(EC.visibility_of_element_located(loc_quit_button))
        # self.driver.find_element(*loc_quit_button).click()
        # self.wait.until(EC.visibility_of_element_located(loc.password_text))
        # self.driver.find_element(*loc.password_text).send_keys(cd.student_user[1])
        # self.wait.until(EC.visibility_of_element_located(loc.quit_confirm_button))
        # self.driver.find_element(*loc.quit_confirm_button).click()
        self.click_element(loc_more_button, "首页_点击更多按钮")
        self.click_element(loc_quit_button, "首页_点击退课按钮")
        self.input_text(loc.password_text, cd.student_user[1], "首页_退课弹框输入密码")
        self.click_element(loc.quit_confirm_button, "首页_退课弹框点击退课确认按钮")

    def refresh(self):
        self.window_refresh()

    # 查找置顶课程
    def stu_top_courses(self):
        return self.get_elements(loc.stu_top_courses, "首页_查找置顶课程")

    # 查找其他课程
    def stu_other_courses(self):
        return self.get_elements(loc.stu_other_courses, "首页_查找其他课程")
