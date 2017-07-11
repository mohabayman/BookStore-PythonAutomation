from selenium.webdriver.common.by import By
from Utils.EdgeSupport import EdgeSupport


class HomePage(object):
    def __init__(self, driver):
        # Driver
        self.driver = driver
        # Locator
        self.Admin_btn_loc = (By.ID, 'Header_Menu_Admin')
        # Elements
        self.Admin_btn = driver.find_element(*self.Admin_btn_loc)

    def click_on_admin_link(self):
        EdgeSupport.click_element_by_id(self.driver, self.Admin_btn_loc[1])
