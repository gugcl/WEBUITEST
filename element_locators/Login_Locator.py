from selenium.webdriver.common.by import By

# 用户登录页面
username_loc = (By.XPATH, "//input[@placeholder='请输入用户名']")
password_loc = (By.XPATH, "//input[@placeholder='请输入密码']")
login_button = (By.XPATH, "//button[contains(@class, 'login-btn')]")



