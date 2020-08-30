import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd

def test_for_lection_7(driver):
    quantity = 1
    while quantity < 4:
        driver.get("https://litecart.stqa.ru/en/")
        driver.find_element_by_xpath("//li[@class='product column shadow hover-light']").click()
        driver.find_element_by_xpath("//button[@name='add_cart_product']").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f".//span[contains(@class, 'quantity') and contains(., '{quantity}')]")))
        quantity+=1 

    driver.get("https://litecart.stqa.ru/en/checkout")
    number_of_product = len(driver.find_elements_by_xpath("//td[@class='tax']"))
    while number_of_product != 0:
        driver.get("https://litecart.stqa.ru/en/checkout")
        element = driver.find_elements_by_xpath(".//td[@class='tax']")[number_of_product-1] 
        driver.find_element_by_name("remove_cart_item").click()
        EC.staleness_of(element)
        number_of_product-=1

