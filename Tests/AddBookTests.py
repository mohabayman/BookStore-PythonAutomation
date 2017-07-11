from selenium import webdriver
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from PageObjects.AdminPage import AdminPage
from PageObjects.BooksPage import BooksPage
from PageObjects.AddBookPage import AddBookPage
from Utils.DriverFactory import DriverFactory
from time import sleep


class AddBookTests(object):

    @staticmethod
    def add_book():
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
        admin_page.click_on_books_link()
        sleep(1)
        books_page = BooksPage(driver)
        books_page.click_on_add_new()
        sleep(1)
        add_book = AddBookPage(driver)
        add_book.add_book('ahmed', 'ali', 'Sci-Fi', '1000')
        sleep(3)
        driver.close()

