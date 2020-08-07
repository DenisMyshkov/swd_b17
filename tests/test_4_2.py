import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd

def test_for_lection_4_task_2(driver):
    driver.get("http://localhost/litecart/")
    products_list = driver.find_elements_by_css_selector(".image-wrapper")
    for product in products_list:
        element = product.find_elements_by_css_selector("[class*=sticker]")
        assert len(element) == 1
    WebDriverWait(driver, 10).until(EC.title_is("Online Store | My Store"))

