import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (you can specify the Chrome executable path if needed)
driver = webdriver.Chrome()


def test_setup(url):
    driver.maximize_window()
    driver.get(url)
    title = driver.title
    assert title == "ProtoCommerce"


def test_broken_links(url):
    links = driver.find_elements(By.TAG_NAME, 'a')
    print(links)

    # Initialize an empty list to store broken links
    broken_links = []

    for link in links:
        href = link.get_attribute('href')
        if href:
            # Send a HEAD request to the link to check its status
            response = requests.head(href)
            if response.status_code != 200:
                broken_links.append(href)

    return broken_links


url = 'https://rahulshettyacademy.com/angularpractice/'  # Replace with the URL of the webpage you want to check
test_setup(url)
broken_links = test_broken_links(url)

if not broken_links:
    print("No broken links found on", url)
else:
    print("Broken links on", url)
    for link in broken_links:
        print(link)

# Close the WebDriver when done
driver.quit()


#driver.execute_script("window.scrollTo(0,document.body.scrollheight)") -- For scrolling
