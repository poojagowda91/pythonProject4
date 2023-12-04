from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://timesofindia.indiatimes.com/"
driver = webdriver.Chrome()


def test_setup(url):
    driver.maximize_window()
    driver.get(url)
    # header = driver.find_element(By.XPATH, "//a[@aria-label='TOI Logo']").text
    # print(header)
    # assert header == "THE TIMES OF INDIA"

    driver.find_element(By.XPATH, "//a[@aria-label='Sports']").click()
    print(driver.window_handles)


test_setup(url)

driver.quit()
