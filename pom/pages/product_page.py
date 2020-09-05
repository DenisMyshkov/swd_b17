from selenium.webdriver.support.wait import WebDriverWait


class Product_page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://litecart.stqa.ru/en/checkout")
        return self

    @property
    def number_of_product(self):
        return len(self.driver.find_elements_by_xpath("//td[@class='tax']"))

    @property
    def remove_button(self):
        return self.driver.find_element_by_name("remove_cart_item")

    @property
    def product_in_sheet(self):
        return self.driver.find_elements_by_xpath(".//td[@class='tax']")
