import pickle
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pathlib import Path

from constants import helper_constants, tech_constants
from page import sign_in_form, registration_form, test_page


def wait_for_element(element, driver, time=tech_constants.TIMEOUT):
    wait = WebDriverWait(driver, time)
    wait.until(expected_conditions.visibility_of(element))


def save_cookie(driver):
    os.makedirs(tech_constants.COOKIES_FOLDER, exist_ok=True)
    with open(tech_constants.COOKIES_FILE_NAME, 'wb') as f:
        pickle.dump(driver.get_cookies(), f)


def login_with_cookie(driver):
    with open(tech_constants.COOKIES_FILE_NAME, 'rb') as f:
        cookies = pickle.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()


def is_cookie_file_exist():
    return Path(tech_constants.COOKIES_FILE_NAME).exists()


def sign_in_click(driver):
    wait_for_element(registration_form.get_sign_in_button(driver), driver)
    registration_form.get_sign_in_button(driver).click()


def enter_username(driver):
    wait_for_element(sign_in_form.get_username_input(driver), driver)
    sign_in_form.get_username_input(driver).send_keys(helper_constants.LOGIN)


def enter_password(driver):
    sign_in_form.get_password_input(driver).send_keys(helper_constants.PASSWORD)


def press_submit(driver):
    sign_in_form.get_submit_button(driver).click()


def login(driver):
    if is_cookie_file_exist():
        login_with_cookie(driver)
    else:
        sign_in_click(driver)
        enter_username(driver)
        enter_password(driver)
        press_submit(driver)
        save_cookie(driver)


def switch_to_frame(driver):
    driver.switch_to.frame(test_page.get_frame(driver))


def drag_and_drop_object(driver):
    ActionChains(driver). \
        move_to_element(test_page.get_object_for_target(driver)). \
        drag_and_drop(
        test_page.get_object_for_target(driver), test_page.get_target(driver)). \
        perform()


def get_target_text(driver):
    return test_page.get_target_text(driver).text
