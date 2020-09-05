from selenium.webdriver.support.wait import WebDriverWait


class Main_page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://litecart.stqa.ru/en/")
        return self

    @property
    def product_button(self):
        return self.driver.find_element_by_xpath("//li[@class='product column shadow hover-light']")

    @property
    def add_product_button(self):
        return self.driver.find_element_by_xpath("//button[@name='add_cart_product']")
