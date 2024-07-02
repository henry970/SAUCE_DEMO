import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

from LogOutPageLocators.Login_page_locators import LogOutPageLocators


class LogOutPage:
    def __init__(self, driver):
        self.driver = driver

    def click_profile_tab(self):
        click_profile_tab = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LogOutPageLocators.CLICK_PROFILE_TAB))
        click_profile_tab.click()
        time.sleep(3)

    def click_log_out_button(self):
        click_log_out_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LogOutPageLocators.CLICK_lOG_OUT_BUTTON))
        click_log_out_button.click()
        time.sleep(3)
