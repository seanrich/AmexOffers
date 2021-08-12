#!/usr/bin/python
"""
Created on Thu Aug 12 15:10:51 2021

@author: MitchellCaywood
"""

from selenium import webdriver

PATH = "msedgedriver.exe"
driver = webdriver.Edge(PATH)

driver.get("https://www.americanexpress.com/en-us/account/login?DestPage=https%3A%2F%2Fglobal.americanexpress.com%2Foffers%2Feligible")

user_id = driver.find_element_by_id("eliloUserID")
user_id.send_keys(input("\n\nWhat is your Amex USER ID? "))

password = driver.find_element_by_id("eliloPassword")
password.send_keys(input("\n\nWhat is your Amex PASSWORD? "))

driver.find_element_by_id("loginSubmit").click()

accept_offer_buttons = []

while not accept_offer_buttons:
    accept_offer_buttons = driver.find_elements_by_class_name("pad-0-l")

accepted_offers = 0
for offer in accept_offer_buttons:
    if offer.text == "Add to Card":
        offer.click()
        accepted_offers += 1

print(f'\n\nAccepted {accepted_offers} offers\n')