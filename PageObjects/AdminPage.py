from selenium.webdriver.common.by import By
from Utils.EdgeSupport import EdgeSupport
from Utils.BasePage import BasePage


class AdminPage(BasePage):
    def __init__(self, driver):
        # Driver
        BasePage.__init__(self, driver)
        # Locator
        # self.MembersLink_txt_loc = (By.ID, 'Form_Field1')
        # self.BooksLink_txt_loc = (By.ID, 'Form_Field3')
        # Elements
        # self.MembersLink_txt = driver.find_element(*self.MembersLink_txt_loc)
        # self.BooksLink_txt = driver.find_element(*self.BooksLink_txt_loc)

    def click_on_members_link(self):
        member_element = self.get_element('MembersLink_txt_loc')
        EdgeSupport.click_element(member_element)

    def click_on_books_link(self):
        member_element = self.get_element('BooksLink_txt_loc')
        EdgeSupport.click_element(member_element)