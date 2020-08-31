import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(desired_capabilities={'loggingPrefs': {'performance': 'ALL'}})
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd

def test_for_lection_10(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    x = 0
    goods = driver.find_elements_by_xpath(".//a[contains(., 'Duck')]")
    while x < len(goods):
        driver.find_elements_by_xpath(".//a[contains(., 'Duck')]")[x].click()
        for l in driver.get_log("browser"):
            print(l)
        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
        x+=1
