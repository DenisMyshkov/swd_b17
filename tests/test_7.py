import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
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
        time.sleep(1)
        assert int(driver.find_element_by_class_name("quantity").text) == quantity
        quantity+=1

    driver.get("https://litecart.stqa.ru/en/checkout")
    number_of_product = len(driver.find_elements_by_xpath("//td[@class='tax']"))
    while number_of_product != 0:
        driver.get("https://litecart.stqa.ru/en/checkout")
        driver.find_element_by_name("remove_cart_item").click()
        number_of_product-=1

