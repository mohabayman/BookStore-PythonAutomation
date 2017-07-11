from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from time import sleep


class LoginTests(object):

    @staticmethod
    def login_with_admin():
        driver = webdriver.Edge(executable_path='../MicrosoftWebDriver.exe')
        driver.get('http://10.1.23.10/bookstore/Login.aspx')
        login_page = LoginPage(driver)
        login_page.login('admin', 'admin')
        sleep(2)
        driver.close()

    @staticmethod
    def login_with_guest():
        driver = webdriver.Edge(executable_path='../MicrosoftWebDriver.exe')
        driver.get('http://10.1.23.10/bookstore/Login.aspx')
        login_page = LoginPage(driver)
        login_page.login('guest', 'guest')
        sleep(2)
        driver.close()
