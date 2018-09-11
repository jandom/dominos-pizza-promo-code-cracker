#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

POSTCODE = 'E15 1BL'

def get_elements_by_selector(selector, timeout = 10):
    condition = EC.visibility_of_any_elements_located((By.CSS_SELECTOR, selector))
    element = WebDriverWait(driver, timeout).until(condition)
    return element

def get_element_by_selector(selector, timeout = 10):
    condition = EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
    element = WebDriverWait(driver, timeout).until(condition)
    return element

def domino_postcode(url = 'https://www.dominos.co.uk/'):
    driver.get(url)
    driver.find_element_by_id('search-input').send_keys(POSTCODE)
    driver.find_element_by_id('btn-delivery').click()

def domino_close_popup(selector = '#arrival > div > i'):
    element = get_element_by_selector(selector)
    element.click()

def domino_menu(selector = '#accelerators > ul > li:nth-child(1) > a'):
    element = get_element_by_selector(selector)
    element.click()

def domino_add_to_basket(selector = '.product-order > button.btn-primary', number_of_clicks = 7):
    elements = get_elements_by_selector(selector)
    element = elements[0]
    for i in range(number_of_clicks):
        time.sleep(0.11 * i)
        element.click()
    time.sleep(2)

def domino_go_to_basket(selector = '.nav-item-wide > a', url = 'https://www.dominos.co.uk/basketdetails/show'):
    driver.get(url)
    # elements = get_elements_by_selector(selector)
    # element.click()

# def domino_add_basket_item(selector = '.basket-product-actions > button.btn-primary', number_of_clicks = 6):
#     for i in range(number_of_clicks):
#         elements = get_elements_by_selector(selector)
#         element = elements[0]
#         element.click()
#         time.sleep(1)
#     time.sleep(2)

def domino_enter_voucher_code(code, selector = '#voucher-code'):
    element = get_element_by_selector(selector)
    element.send_keys(code)
    element = get_element_by_selector('.new-voucher-button-box > button')
    element.click()
    time.sleep(1)

def check_element_by_selector(xpathSelector):
    element = None
    try:
        element = driver.find_elements_by_xpath(xpathSelector)
    except NoSuchElementException:
        return element
    return element

def domino_verify_success(selector = '//div[contains(@class, "voucher-eligibility-splash-action")]//a[contains(@class, "btn")]'):
    return check_element_by_selector(selector)

def domino_verify_error(selector = '//p[contains(@class, "new-voucher-help-block")]'):
    return check_element_by_selector(selector)

def domino_verify_voucher_code():
    successElements = domino_verify_success()
    errorElements = domino_verify_error()
    outcome = len(successElements) == 1 and len(errorElements) == 0
    # print("outcome", outcome, successElements, errorElements)
    if outcome:
        element = successElements[0]
        element.click()
        element = get_element_by_selector('button.basket-product-desktop-action-priceless')
        element.click()
    else:
        element = get_element_by_selector('#voucher-code')
        element.clear()

    return outcome

driver = webdriver.Chrome('./chromedriver')

domino_postcode()

domino_close_popup()

domino_menu()

domino_add_to_basket(number_of_clicks = 1)

domino_go_to_basket()

# domino_add_basket_item()

codes = [
    # u'FORTY40£',
    u'FORTY40£',
    u'FORTY40',
    u'FORTY40£',
]

for code in codes:
    domino_enter_voucher_code(code)
    outcome = domino_verify_voucher_code()
    print(code, outcome)

# driver.close()
