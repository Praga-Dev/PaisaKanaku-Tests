from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click_element(self, locator):
        self.wait_for_element_clickable(locator).click()

    def input_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def select_dropdown_option_by_text(self, locator, option_text):
        from selenium.webdriver.support.select import Select
        select = Select(self.wait_for_element(locator))
        select.select_by_visible_text(option_text)
    def select_drop_option_by_index(self, locator, index):
        from selenium.webdriver.support.select import Select
        select= Select(self.wait_for_element(locator))
        select.select_by_index(index)


    def get_text(self, locator):
        return self.wait_for_element(locator).text

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False