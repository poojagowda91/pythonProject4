from selenium import webdriver
from selenium.webdriver.common.by import By


class Practice:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def start(self):
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        self.driver.implicitly_wait(5)

    def title_validation(self):
        title = self.driver.title
        assert title == "GreenKart - veg and fruits kart"

    def products_onpage(self):
        products = self.driver.find_elements(By.XPATH, "//div[@class='products']/div/h4")
        for product in products:
            print(product.text)

        # screenshot = self.driver.get_screenshot_as_png()
        # desktop_path = "/Users/poojagn/Desktop/products_screenshot.png"  # Replace 'YourUsername' with your actual username
        #
        # with open(desktop_path, "wb") as file:
        #     file.write(screenshot)

    def switch_case(self):
        self.driver.find_element(By.XPATH, "//a[@href='#/offers']").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        newtitle = self.driver.title
        print(newtitle)
    

    def quit(self):
        self.driver.quit()


# Create an instance of the Practice class
practice = Practice()

# Call the methods on the instance
practice.start()
practice.title_validation()
practice.products_onpage()
practice.switch_case()

# Quit the driver at the end
practice.quit()
