#!/usr/bin/python
"""
Created on Thu Aug 12 15:10:51 2021

@author: MitchellCaywood
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located as present
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

PATH = "msedgedriver.exe"
driver = webdriver.Edge(PATH)
wait = WebDriverWait(driver, timeout=15)

driver.get("https://www.americanexpress.com/en-us/account/login?DestPage=https%3A%2F%2Fglobal.americanexpress.com%2Foffers%2Feligible")

user_id = driver.find_element_by_id("eliloUserID")
user_id.send_keys(input("\n\nWhat is your Amex USER ID? "))

password = driver.find_element_by_id("eliloPassword")
password.send_keys(input("\n\nWhat is your Amex PASSWORD? "))

driver.find_element_by_id("loginSubmit").click()

wait.until(present((By.CLASS_NAME, "pad-0-l")))
accept_offer_buttons = driver.find_elements_by_class_name("pad-0-l")
accepted_offers = 0
while len(accept_offer_buttons):
    try:
        offer = accept_offer_buttons.pop(0)
        if offer.text == "Add to Card":
            offer.click()
            accepted_offers += 1
            wait.until(present((By.CLASS_NAME, "offer-added-notification")))
            accept_offer_buttons = driver.find_elements_by_class_name("pad-0-l")
    except TimeoutException:
        break
    except StaleElementReferenceException:
        accept_offer_buttons = driver.find_elements_by_class_name("pad-0-l")
        continue

print(f'\n\nAccepted {accepted_offers} offers\n')
