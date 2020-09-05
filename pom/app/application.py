from selenium import webdriver
from pom.pages.main_page import Main_page
from pom.pages.product_page import Product_page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = Main_page(self.driver)
        self.product_page = Product_page(self.driver)
        self.wait = WebDriverWait(self.driver, 10)
        self.EC = EC
        self.By = By

    def quit(self):
        self.driver.quit()

    def add_3_duck_in_cart(self):
        quantity = 1
        while quantity < 4:
            self.main_page.open()
            self.main_page.product_button.click()
            self.main_page.add_product_button.click()
            self.wait.until(self.EC.presence_of_element_located((self.By.XPATH, f".//span[contains(@class, 'quantity') and contains(., '{quantity}')]")))
            quantity+=1

    def remove_all_products_from_cart(self):
        self.product_page.open()
        number_of_product = self.product_page.number_of_product
        while number_of_product != 0:
            self.product_page.open()
            self.element = self.product_page.product_in_sheet[number_of_product-1]
            self.product_page.remove_button.click()
            self.EC.staleness_of(self.element)
            number_of_product -= 1

