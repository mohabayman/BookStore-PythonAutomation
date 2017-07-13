from selenium.webdriver.common.by import By
from Utils.EdgeSupport import EdgeSupport
from Page import Page


class AdminPage(Page):
    def __init__(self, driver):
        # Driver
        Page.__init__(self, driver)
        # Locator
        self.MembersLink_txt_loc = (By.ID, 'Form_Field1')
        self.BooksLink_txt_loc = (By.ID, 'Form_Field3')
        # Elements
        self.MembersLink_txt = driver.find_element(*self.MembersLink_txt_loc)
        self.BooksLink_txt = driver.find_element(*self.BooksLink_txt_loc)

    def click_on_members_link(self):
        EdgeSupport.click_element_by_id(self.driver, self.MembersLink_txt_loc[1])

    def click_on_books_link(self):
        EdgeSupport.click_element_by_id(self.driver, self.BooksLink_txt_loc[1])