import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from faker import Faker
import time

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd

def test_for_lection_6_task_2(driver):
    fake = Faker()
    valid_password = "Uber2020"
    valid_email = fake.email()
    driver.get("https://litecart.stqa.ru/en/create_account")
    driver.find_element_by_name("tax_id").send_keys(fake.ssn())
    driver.find_element_by_name("company").send_keys(fake.company())
    driver.find_element_by_name("firstname").send_keys(fake.first_name())
    driver.find_element_by_name("lastname").send_keys(fake.last_name())
    driver.find_element_by_name("address1").send_keys(fake.street_address())
    driver.find_element_by_name("postcode").send_keys(fake.postcode())
    driver.find_element_by_name("city").send_keys(fake.city())
    driver.find_element_by_name("email").send_keys(valid_email)
    driver.find_element_by_name("phone").clear()
    driver.find_element_by_name("phone").send_keys("+1"+fake.pystr_format(string_format='######{{random_int}}'))
    driver.find_element_by_name("password").send_keys(valid_password)
    driver.find_element_by_name("confirmed_password").send_keys(valid_password)
    country = Select(driver.find_element_by_name("country_code"))
    country.select_by_visible_text("United States")
    zone_code = Select(driver.find_element_by_css_selector("select[name=zone_code]"))
    zone_code.select_by_visible_text("Texas")
    driver.find_element_by_name("create_account").click()
    driver.get("https://litecart.stqa.ru/en/logout")
    driver.find_element_by_name("email").send_keys(valid_email)
    driver.find_element_by_name("password").send_keys(valid_password)
    driver.find_element_by_name("login").click()

