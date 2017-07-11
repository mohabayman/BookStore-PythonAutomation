from selenium import webdriver
from time import sleep


class DriverFactory(object):
    @staticmethod
    def get_driver(browser_name):
        if browser_name.lower() == 'edge':
            driver = webdriver.Edge(executable_path='../Tools/MicrosoftWebDriver.exe')
            sleep(2)
            return driver
        else:
            raise Exception('Wrong browser name provided !!')
