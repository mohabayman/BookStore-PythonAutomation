from selenium import webdriver
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from PageObjects.AdminPage import AdminPage
from PageObjects.MembersPage import MembersPage
from PageObjects.AddMemberPage import AddMemberPage
from Utils.DriverFactory import DriverFactory
from time import sleep


class AddMemberTests (object):

    @staticmethod
    def add_member():
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
        sleep(1)
        add_member = AddMemberPage(driver)
        add_member.insert_member('admin', 'admin', 'Memeber', 'Ahmed', 'Ali', 'ahmedali@yahoo.com')
        sleep(3)
        driver.close()

