from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from PageObjects.AdminPage import AdminPage
from PageObjects.MembersPage import MembersPage
from Utils.DriverFactory import DriverFactory
from time import sleep


class MembersTests(object):

    @staticmethod
    def members_insert():
        driver = DriverFactory.get_driver('Edge')
        driver.get('http://10.1.23.10/bookstore')
        sleep(1)
        home_page = HomePage(driver)
        home_page.click_on_admin_link()
        sleep(1)
        login_page = LoginPage(driver)
        login_page.login('admin', 'admin')
        sleep(1)
        admin_page = AdminPage(driver)
        admin_page.click_on_members_link()
        sleep(1)
        members_page = MembersPage(driver)
        members_page.click_on_insert_link()
        sleep(2)
        driver.close()
