import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture(scope='module')
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_title_validation(setup):
    expected_title = "Practice Page"
    assert setup.title == expected_title


def test_radio_button_example(setup):
    radion_btn_list = setup.find_elements(By.XPATH, "//div[@id='radio-btn-example']/fieldset/label/input")
    radio_dict = {}

    for index, radio_btn in enumerate(radion_btn_list):
        radio_id = f"{index}"
        radio_dict[radio_btn.get_attribute("value")] = radio_id

    print(radio_dict)

    for value, radio_id in radio_dict.items():
        radio_element = setup.find_element(By.XPATH, f"//label[@for='{value}']/input")

        # Check if radio button is displayed, enabled, and selected
        assert radio_element.is_displayed()
        assert radio_element.is_enabled()
        assert not radio_element.is_selected()  # Assuming you want to check it's not selected

        # Click on the radio button
        radio_element.click()

        # Now, you can check if the radio button is selected after clicking
        assert radio_element.is_selected()


if __name__ == '__main__':
    pytest.main()
