from selenium.webdriver.common.by import By
from Utils.EdgeSupport import EdgeSupport


class LoginPage(object):
    def __init__(self, driver):
        # Driver
        self.driver = driver
        # Locators
        self.username_txt_loc = (By.ID, 'Login_name')
        self.password_txt_loc = (By.ID, 'Login_password')
        self.login_btn_loc = (By.ID, 'Login_login')
        # Elements
        self.username_txt = driver.find_element(*self.username_txt_loc)
        self.password_txt = driver.find_element(*self.password_txt_loc)
        self.login_btn = driver.find_element(*self.login_btn_loc)

    def login(self, username, password):
        self.username_txt.send_keys(username)
        self.password_txt.send_keys(password)

        EdgeSupport.click_element_by_id(self.driver, self.login_btn_loc[1])
