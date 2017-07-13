from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from Utils.DriverFactory import DriverFactory
from time import sleep



class LoginTests(object):

    @staticmethod
    def login_with_admin():
        driver = DriverFactory.get_driver('Edge')
        driver.get(HomePage.get_home_url())
        sleep(1)
        home_page = HomePage(driver)
        home_page.header.click_sign_in_link()
        sleep(1)
        login_page = LoginPage(driver)
        login_page.login('admin', 'admin')
        sleep(1)
        driver.close()

    @staticmethod
    def login_with_guest():
        driver = DriverFactory.get_driver('Edge')
        driver.get(HomePage.get_home_url())
        sleep(1)
        home_page = HomePage(driver)
        home_page.header.click_sign_in_link()
        sleep(1)
        login_page = LoginPage(driver)
        login_page.login('guest', 'guest')
        sleep(1)
        driver.close()
