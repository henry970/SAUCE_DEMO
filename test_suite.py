import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from LogOutPagge.LogOut_page_test import LogOutPage
from OrderProductPage.order_product_test import OrderPageLocators, OrderPagesBikeLight, OrderPageBoltTshirt, \
    OrderPageBoltOneSie, OrderPageBoltJacket, OrderPageBoltTshirtRed
from loginPage.login_page_test import LoginPage


@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (to avoid errors in headless mode)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


# @pytest.fixture(scope="module")
# def driver_setup():
#     driver = webdriver.Edge()
#     driver.implicitly_wait(20)
#     driver.maximize_window()
#     yield driver
#     driver.quit()


@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login_url("https://www.saucedemo.com")
    return login_page


def test_login_page_on_sauce_demo_website(login):
    login.enter_username("performance_glitch_user")
    login.enter_password("secret_sauce")
    login.click_login_button()


def test_order_product_on_sauce_demo_website(login):
    test_login_page_on_sauce_demo = OrderPageLocators(login.driver)
    test_login_page_on_sauce_demo.click_back_park_button()
    test_login_page_on_sauce_demo.click_continue_button()
    test_login_page_on_sauce_demo.click_checkout_button()
    test_login_page_on_sauce_demo.enter_firstName("henry")
    test_login_page_on_sauce_demo.enter_LastName("okolie")
    test_login_page_on_sauce_demo.enter_Postal_Code("323")
    test_login_page_on_sauce_demo.click_continue_button1()
    test_login_page_on_sauce_demo.click_finish_button()
    test_login_page_on_sauce_demo.click_back_button()


def test_order_product_on_sauce_demo_website1(login):
    test_login_page_on_sauce_demo = OrderPagesBikeLight(login.driver)
    test_login_page_on_sauce_demo.click_back_park_button()
    test_login_page_on_sauce_demo.click_continue_button()
    test_login_page_on_sauce_demo.click_checkout_button()
    test_login_page_on_sauce_demo.enter_firstName("henry")
    test_login_page_on_sauce_demo.enter_LastName("okolie")
    test_login_page_on_sauce_demo.enter_Postal_Code("323")
    test_login_page_on_sauce_demo.click_continue_button1()
    test_login_page_on_sauce_demo.click_finish_button()
    test_login_page_on_sauce_demo.click_back_button()


def test_order_product_on_sauce_demo_website2(login):
    test_login_page_on_sauce_demo = OrderPageBoltTshirt(login.driver)
    test_login_page_on_sauce_demo.click_back_park_button()
    test_login_page_on_sauce_demo.click_continue_button()
    test_login_page_on_sauce_demo.click_checkout_button()
    test_login_page_on_sauce_demo.enter_firstName("henry")
    test_login_page_on_sauce_demo.enter_LastName("okolie")
    test_login_page_on_sauce_demo.enter_Postal_Code("323")
    test_login_page_on_sauce_demo.click_continue_button1()
    test_login_page_on_sauce_demo.click_finish_button()
    test_login_page_on_sauce_demo.click_back_button()


def test_order_product_on_sauce_demo_website3(login):
    test_login_page_on_sauce_demo = OrderPageBoltOneSie(login.driver)
    test_login_page_on_sauce_demo.click_back_park_button()
    test_login_page_on_sauce_demo.click_continue_button()
    test_login_page_on_sauce_demo.click_checkout_button()
    test_login_page_on_sauce_demo.enter_firstName("henry")
    test_login_page_on_sauce_demo.enter_LastName("okolie")
    test_login_page_on_sauce_demo.enter_Postal_Code("323")
    test_login_page_on_sauce_demo.click_continue_button1()
    test_login_page_on_sauce_demo.click_finish_button()
    test_login_page_on_sauce_demo.click_back_button()


def test_order_product_on_sauce_demo_website5(login):
    test_order_product_on_sauce_demo = OrderPageBoltJacket(login.driver)
    test_order_product_on_sauce_demo.click_back_park_button()
    test_order_product_on_sauce_demo.click_continue_button()
    test_order_product_on_sauce_demo.click_checkout_button()
    test_order_product_on_sauce_demo.enter_firstName("henry")
    test_order_product_on_sauce_demo.enter_LastName("okolie")
    test_order_product_on_sauce_demo.enter_Postal_Code("323")
    test_order_product_on_sauce_demo.click_continue_button1()
    test_order_product_on_sauce_demo.click_finish_button()
    test_order_product_on_sauce_demo.click_back_button()


def test_order_product_on_sauce_demo_website6(login):
    test_login_page_on_sauce_demo = OrderPageBoltTshirtRed(login.driver)
    test_login_page_on_sauce_demo.click_back_park_button()
    test_login_page_on_sauce_demo.click_continue_button()
    test_login_page_on_sauce_demo.click_checkout_button()
    test_login_page_on_sauce_demo.enter_firstName("henry")
    test_login_page_on_sauce_demo.enter_LastName("okolie")
    test_login_page_on_sauce_demo.enter_Postal_Code("323")
    test_login_page_on_sauce_demo.click_continue_button1()
    test_login_page_on_sauce_demo.click_finish_button()
    test_login_page_on_sauce_demo.click_back_button()


def test_log_out_page_on_sauce_demo_website(login):
    test_log_out_page_on_sauce_demo = LogOutPage(login.driver)
    test_log_out_page_on_sauce_demo.click_profile_tab()
    test_log_out_page_on_sauce_demo.click_log_out_button()
