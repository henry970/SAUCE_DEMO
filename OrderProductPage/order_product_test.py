import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

from OrderProductLocators.order_product_locator_test import OrderPageLocatorsBackPark, OrderPageLocatorsBikeLight, \
    OrderPageLocatorsBoltTshirt, OrderPageLocatorOneSie, OrderPageLocatorsJacket, OrderPageLocatorsBoltTshirtRed


class OrderPageLocators:
    def __init__(self, driver):
        self.driver = driver

    def click_back_park_button(self):
        click_back_park_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBackPark.ClICK_BACK_PARK))
        click_back_park_button.click()
        time.sleep(3)

    def click_continue_button(self):
        click_continue_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBackPark.ClICK_CONTINUE))
        click_continue_button.click()
        time.sleep(3)

    def click_checkout_button(self):
        click_checkout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBackPark.ClICK_CHECKOUT))
        click_checkout_button.click()
        time.sleep(3)

    def enter_firstName(self, first):
        enter_firstName = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBackPark.FIRSTNAME))
        enter_firstName.send_keys(first)
        time.sleep(3)

    def enter_LastName(self, last):
        enter_LastName = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBackPark.LASTNAME))
        enter_LastName.send_keys(last)
        time.sleep(3)

    def enter_Postal_Code(self, code):
        enter_Postal_Code = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBackPark.POSTAL_CODE))
        enter_Postal_Code.send_keys(code)
        time.sleep(3)

    def click_continue_button1(self):
        click_continue_button1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBackPark.ClICK_CONTINUE1))
        click_continue_button1.click()
        time.sleep(3)

    def click_finish_button(self):
        click_finish_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBackPark.ClICK_FINISH))
        click_finish_button.click()
        time.sleep(3)

    def click_back_button(self):
        click_back_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBackPark.CLICK_BACK_BUTTON))
        click_back_button.click()
        time.sleep(3)


class OrderPagesBikeLight:
    def __init__(self, driver):
        self.driver = driver

    def click_back_park_button(self):
        click_back_park_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBikeLight.ClICK_BIKE_LIGHT))
        click_back_park_button.click()
        time.sleep(3)

    def click_continue_button(self):
        click_continue_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBikeLight.ClICK_CONTINUE))
        click_continue_button.click()
        time.sleep(3)

    def click_checkout_button(self):
        click_checkout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBikeLight.ClICK_CHECKOUT))
        click_checkout_button.click()
        time.sleep(3)

    def enter_firstName(self, first):
        enter_firstName = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBikeLight.FIRSTNAME))
        enter_firstName.send_keys(first)
        time.sleep(3)

    def enter_LastName(self, last):
        enter_LastName = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBikeLight.LASTNAME))
        enter_LastName.send_keys(last)
        time.sleep(3)

    def enter_Postal_Code(self, code):
        enter_Postal_Code = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBikeLight.POSTAL_CODE))
        enter_Postal_Code.send_keys(code)
        time.sleep(3)

    def click_continue_button1(self):
        click_continue_button1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBikeLight.ClICK_CONTINUE1))
        click_continue_button1.click()
        time.sleep(3)

    def click_finish_button(self):
        click_finish_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBikeLight.ClICK_FINISH))
        click_finish_button.click()
        time.sleep(3)

    def click_back_button(self):
        click_back_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBikeLight.CLICK_BACK_BUTTON))
        click_back_button.click()
        time.sleep(3)


class OrderPageBoltTshirt:
    def __init__(self, driver):
        self.driver = driver

    def click_back_park_button(self):
        click_back_park_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBoltTshirt.ClICK_BOLT))
        click_back_park_button.click()
        time.sleep(3)

    def click_continue_button(self):
        click_continue_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBoltTshirt.ClICK_CONTINUE))
        click_continue_button.click()
        time.sleep(3)

    def click_checkout_button(self):
        click_checkout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBoltTshirt.ClICK_CHECKOUT))
        click_checkout_button.click()
        time.sleep(3)

    def enter_firstName(self, first):
        enter_firstName = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBoltTshirt.FIRSTNAME))
        enter_firstName.send_keys(first)
        time.sleep(3)

    def enter_LastName(self, last):
        enter_LastName = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBoltTshirt.LASTNAME))
        enter_LastName.send_keys(last)
        time.sleep(3)

    def enter_Postal_Code(self, code):
        enter_Postal_Code = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBoltTshirt.POSTAL_CODE))
        enter_Postal_Code.send_keys(code)
        time.sleep(3)

    def click_continue_button1(self):
        click_continue_button1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBoltTshirt.ClICK_CONTINUE1))
        click_continue_button1.click()
        time.sleep(3)

    def click_finish_button(self):
        click_finish_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBoltTshirt.ClICK_FINISH))
        click_finish_button.click()
        time.sleep(3)

    def click_back_button(self):
        click_back_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBoltTshirt.CLICK_BACK_BUTTON))
        click_back_button.click()
        time.sleep(3)


class OrderPageBoltOneSie:
    def __init__(self, driver):
        self.driver = driver

    def click_back_park_button(self):
        click_back_park_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorOneSie.ClICK_ONESIE))
        click_back_park_button.click()
        time.sleep(3)

    def click_continue_button(self):
        click_continue_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorOneSie.ClICK_CONTINUE))
        click_continue_button.click()
        time.sleep(3)

    def click_checkout_button(self):
        click_checkout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorOneSie.ClICK_CHECKOUT))
        click_checkout_button.click()
        time.sleep(3)

    def enter_firstName(self, first):
        enter_firstName = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorOneSie.FIRSTNAME))
        enter_firstName.send_keys(first)
        time.sleep(3)

    def enter_LastName(self, last):
        enter_LastName = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorOneSie.LASTNAME))
        enter_LastName.send_keys(last)
        time.sleep(3)

    def enter_Postal_Code(self, code):
        enter_Postal_Code = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorOneSie.POSTAL_CODE))
        enter_Postal_Code.send_keys(code)
        time.sleep(3)

    def click_continue_button1(self):
        click_continue_button1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorOneSie.ClICK_CONTINUE1))
        click_continue_button1.click()
        time.sleep(3)

    def click_finish_button(self):
        click_finish_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorOneSie.ClICK_FINISH))
        click_finish_button.click()
        time.sleep(3)

    def click_back_button(self):
        click_back_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorOneSie.CLICK_BACK_BUTTON))
        click_back_button.click()
        time.sleep(3)


class OrderPageBoltJacket:
    def __init__(self, driver):
        self.driver = driver

    def click_back_park_button(self):
        click_back_park_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsJacket.ClICK_JACKET))
        click_back_park_button.click()
        time.sleep(3)

    def click_continue_button(self):
        click_continue_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsJacket.ClICK_CONTINUE))
        click_continue_button.click()
        time.sleep(3)

    def click_checkout_button(self):
        click_checkout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsJacket.ClICK_CHECKOUT))
        click_checkout_button.click()
        time.sleep(3)

    def enter_firstName(self, first):
        enter_firstName = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsJacket.FIRSTNAME))
        enter_firstName.send_keys(first)
        time.sleep(3)

    def enter_LastName(self, last):
        enter_LastName = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsJacket.LASTNAME))
        enter_LastName.send_keys(last)
        time.sleep(3)

    def enter_Postal_Code(self, code):
        enter_Postal_Code = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsJacket.POSTAL_CODE))
        enter_Postal_Code.send_keys(code)
        time.sleep(3)

    def click_continue_button1(self):
        click_continue_button1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsJacket.ClICK_CONTINUE1))
        click_continue_button1.click()
        time.sleep(3)

    def click_finish_button(self):
        click_finish_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsJacket.ClICK_FINISH))
        click_finish_button.click()
        time.sleep(3)

    def click_back_button(self):
        click_back_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsJacket.CLICK_BACK_BUTTON))
        click_back_button.click()
        time.sleep(3)


class OrderPageBoltTshirtRed:
    def __init__(self, driver):
        self.driver = driver

    def click_back_park_button(self):
        click_back_park_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBoltTshirtRed.ClICK_BOLT_RED))
        click_back_park_button.click()
        time.sleep(3)

    def click_continue_button(self):
        click_continue_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBoltTshirtRed.ClICK_CONTINUE))
        click_continue_button.click()
        time.sleep(3)

    def click_checkout_button(self):
        click_checkout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBoltTshirtRed.ClICK_CHECKOUT))
        click_checkout_button.click()
        time.sleep(3)

    def enter_firstName(self, first):
        enter_firstName = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBoltTshirtRed.FIRSTNAME))
        enter_firstName.send_keys(first)
        time.sleep(3)

    def enter_LastName(self, last):
        enter_LastName = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBoltTshirt.LASTNAME))
        enter_LastName.send_keys(last)
        time.sleep(3)

    def enter_Postal_Code(self, code):
        enter_Postal_Code = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBoltTshirtRed.POSTAL_CODE))
        enter_Postal_Code.send_keys(code)
        time.sleep(3)

    def click_continue_button1(self):
        click_continue_button1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBoltTshirtRed.ClICK_CONTINUE1))
        click_continue_button1.click()
        time.sleep(3)

    def click_finish_button(self):
        click_finish_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBoltTshirtRed.ClICK_FINISH))
        click_finish_button.click()
        time.sleep(3)

    def click_back_button(self):
        click_back_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocatorsBoltTshirtRed.CLICK_BACK_BUTTON))
        click_back_button.click()
        time.sleep(3)
