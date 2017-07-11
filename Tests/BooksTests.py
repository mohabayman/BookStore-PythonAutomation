from selenium import webdriver
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from PageObjects.AdminPage import AdminPage
from PageObjects.BooksPage import BooksPage
from time import sleep


class BooksTests(object):

    @staticmethod
    def add_book():
        driver = webdriver.Edge(executable_path='../MicrosoftWebDriver.exe')
        driver.get('http://10.1.23.10/bookstore')
        sleep(1)
        home_page = HomePage(driver)
        home_page.click_on_admin_link()
        sleep(1)
        login_page = LoginPage(driver)
        login_page.login('admin', 'admin')
        sleep(1)
        admin_page = AdminPage(driver)
        admin_page.click_on_books_link()
        sleep(1)
        books_page = BooksPage(driver)
        books_page.click_on_add_new()
        sleep(2)
        driver.close()