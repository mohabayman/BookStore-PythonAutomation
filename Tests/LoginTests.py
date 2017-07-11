from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from time import sleep
from Utils.DriverFactory import DriverFactory


class LoginTests(object):

    @staticmethod
    def login_with_admin():
        driver = DriverFactory.get_driver('Edge')
        driver.get('http://10.1.23.10/bookstore/Login.aspx')
        login_page = LoginPage(driver)
        login_page.login('admin', 'admin')
        sleep(2)
        driver.close()

    @staticmethod
    def login_with_guest():
        driver = DriverFactory.get_driver('Edge')
        driver.get('http://10.1.23.10/bookstore/Login.aspx')
        login_page = LoginPage(driver)
        login_page.login('guest', 'guest')
        sleep(2)
        driver.close()
