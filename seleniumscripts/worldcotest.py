from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from utilties.basefile import setup
import pytest


# The test function that uses the 'setup' fixture
def test_popup_close(setup):
    driver = setup
    try:
        closebtn = driver.find_element(By.XPATH, "//div[@class='fc-ab-dialog fc-dialog']/button/div")
        if closebtn.is_displayed():
            closebtn.click()
        else:
            print("No close button displayed")
    except NoSuchElementException:
        print("Close button not found")


# Use the pytest.mark.parametrize decorator to indicate test functions
@pytest.mark.parametrize("scroll_to_bottom", [True, False])
def test_listallcountries(setup, scroll_to_bottom):
    driver = setup
    countrieslist = driver.find_elements(By.XPATH,
                                         "//table[@id='main_table_countries_today']/tbody/tr[@class='even' or @class='odd']/td[2]")
    print(f"Number of countries: {len(countrieslist)}")

    if scroll_to_bottom:
        # Scroll to the bottom of the page to see all countries (you can customize the scroll action)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    for i in countrieslist:
        print(i.text)


if __name__ == "__main__":
    pytest.main()
