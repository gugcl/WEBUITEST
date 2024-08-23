from Config.Base import BaseElement
from element_locators import Login_Locator


class Login(BaseElement):

    def enter_username(self, name):
        ele = self.base_find_element(Login_Locator.username_loc)
        # ele.clear()
        ele.send_keys(name)  # 输入用户名

    def enter_password(self, password):
        ele = self.base_find_element(Login_Locator.password_loc)
        ele.send_keys(password)  # 输入密码

    def click_login_button(self):
        ele = self.base_find_element(Login_Locator.login_button)
        ele.click()  # 点击登录按钮

    def Login_action(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()



