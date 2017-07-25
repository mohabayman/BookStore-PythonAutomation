import os
from PageObjects.PageParts import Header
from DriverFactory import DriverFactory
from Utils.LocatorParser import LocatorParser


class BasePage(object):

    def __init__(self, browser, locator_file):
        # self.driver = driver
        locator_file_path = os.path.join(os.path.driname(__file__), '..', 'Locators', locator_file)
        self.driver = DriverFactory.get_driver(browser)
        self.header = Header(self.driver)
        self.page_locators = LocatorParser.get_Locators(locator_file_path)

    # Get element by element name
    def get_element(self, elem_name):
        elem_locator = self.page_locators[elem_name]
        element = self.driver.find_element(elem_locator[0], elem_locator[1])
        return element

    def close_web_browser(self):
        self.driver.close()