from selenium.webdriver.common.by import By

__USERNAME_INPUT = (By.XPATH, '//form[@class="ajaxlogin"]//input[@name="username"]')
__PASSWORD_INPUT = (By.XPATH, '//form[@class="ajaxlogin"]//input[@name="password"]')
__SUBMIT_BUTTON = (By.XPATH, '//form[@class="ajaxlogin"]//input[@type="submit"]')


def get_username_input(driver):
    return driver.find_element(*__USERNAME_INPUT)


def get_password_input(driver):
    return driver.find_element(*__PASSWORD_INPUT)


def get_submit_button(driver):
    return driver.find_element(*__SUBMIT_BUTTON)
