import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from test_results_collector import send_test_result

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
title = driver.title
assert title == "ProtoCommerce"
driver.quit()

test_name = "Test: Verify Page Title"
status = "PASSED" if title == "ProtoCommerce" else "FAILED"
send_test_result(test_name, status)