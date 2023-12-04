import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.worldometers.info/coronavirus/")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def teardown():
    yield
    # Additional cleanup code (if needed) goes here
