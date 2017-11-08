from selenium.webdriver.common.by import By

__OBJECT_FOR_TARGET = (By.ID, 'draggable')
__TARGET = (By.ID, 'droppable')
__FRAME = (By.XPATH, '//div[@id = "example-1-tab-1"]//iframe')
__TARGET_TEXT = (By.CSS_SELECTOR, '#droppable>p')

def get_object_for_target(driver):
    return driver.find_element(*__OBJECT_FOR_TARGET)


def get_target(driver):
    return driver.find_element(*__TARGET)


def get_target_text(driver):
    return driver.find_element(*__TARGET_TEXT)


def get_frame(driver):
    return driver.find_element(*__FRAME)