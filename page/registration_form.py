from selenium.webdriver.common.by import By

__SIGN_IN_BUTTON = (By.XPATH, '//a[@href="#login"]')


def get_sign_in_button(driver):
    return driver.find_element(*__SIGN_IN_BUTTON)




