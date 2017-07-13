from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from PageObjects.AdminPage import AdminPage
from Utils.DriverFactory import DriverFactory
from time import sleep


class AdminTests(object):

    @staticmethod
    def admin_members():
        driver = DriverFactory.get_driver('Edge')
        driver.get(HomePage.get_home_url())
        sleep(1)
        home_page = HomePage(driver)
        home_page.header.click_admin_link()
        sleep(1)
        login_page = LoginPage(driver)
        login_page.login('admin', 'admin')
        sleep(1)
        admin_page = AdminPage(driver)
        admin_page.click_on_members_link()
        sleep(2)
        driver.close()
