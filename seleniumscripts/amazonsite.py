import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Use scope='module' to create a single WebDriver instance for the entire module
@pytest.fixture(scope='module')
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_title_validation(setup):
    expected_title = "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
    assert setup.title == expected_title


def test_add_to_cart(setup):
    today_deal_link = setup.find_element(By.XPATH, "//div[@id='nav-xshop']/a[6]")
    today_deal_link.click()
    elementslist = setup.find_elements(By.XPATH, "//span[@class='a-truncate-cut']")
    for list in elementslist:
        itemsnames = setup.find_element(By.XPATH, "//span[@class='a-truncate-cut']").text
        print(itemsnames)


if __name__ == '__main__':
    pytest.main()
