import pytest
import subprocess
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from faker import Faker
import time

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd

def test_for_lection_6_task_2(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    driver.find_element_by_xpath("/html/body/div/div/div/table/tbody/tr/td[3]/div[1]/a[2]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/table/tbody/tr/td[3]/form/div/div/div[1]/table/tbody/tr[1]/td/label[1]/input").click()
    driver.find_element_by_name("name[en]").send_keys("Donald Duck")
    driver.find_element_by_name("code").send_keys("34567")
    driver.find_element_by_css_selector("input[data-name*=Rubber]").click()
    driver.find_elements_by_css_selector("input[name*=product_group]")[2].click()

    def superpower(driver, element, number):
        action = ActionChains(driver)
        action.click(element)
        action.send_keys_to_element(element, Keys.CONTROL+"a")
        action.send_keys_to_element(element, Keys.DELETE)
        action.send_keys_to_element(element, number)
        action.perform()

    quantity = driver.find_element_by_name("quantity")
    superpower(driver, quantity, "12345")

    driver.find_element_by_name("date_valid_from").send_keys("05052020")
    driver.find_element_by_name("date_valid_to").send_keys("12/12/2020")
    dir = subprocess.run(["pwd"], stdout=subprocess.PIPE, text=True)
    driver.find_element_by_css_selector("input[type=file]").send_keys(dir.stdout[0:-1]+"/5796097_0.png")

    driver.find_element_by_css_selector("a[href*=tab-information]").click()
    time.sleep(2)
    manufacturer = Select(driver.find_element_by_name("manufacturer_id"))
    manufacturer.select_by_visible_text("ACME Corp.")
    driver.find_element_by_name("keywords").send_keys("Duck")
    driver.find_element_by_name("short_description[en]").send_keys("Good duck")
    driver.find_element_by_class_name("trumbowyg-editor").send_keys("a:hgsdhfiehfasdfkja")

    driver.find_element_by_css_selector("a[href*=tab-prices]").click()
    time.sleep(2)
    price_currency = Select(driver.find_element_by_name("purchase_price_currency_code"))
    price_currency.select_by_visible_text("US Dollars")

    price = driver.find_element_by_name("purchase_price")
    superpower(driver, price, "5")

    price_u = driver.find_element_by_name("gross_prices[USD]")
    superpower(driver, price_u, "6")

    price_e = driver.find_element_by_name("gross_prices[EUR]")
    superpower(driver, price_e, "7")

    driver.find_element_by_name("save").click()
    time.sleep(2)

    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    donald_duck = driver.find_elements_by_xpath("//*[contains(text(), 'Donald Duck')]")

