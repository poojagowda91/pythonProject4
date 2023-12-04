import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_python_org_title(driver):
    site = "http://www.python.org"
    driver.get(site)
    driver.maximize_window()
    title = driver.title
    assert title == "Welcome to Python.org"


if __name__ == "__main__":
    pytest.main([__file__])
