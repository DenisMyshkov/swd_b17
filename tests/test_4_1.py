import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(15)
    request.addfinalizer(wd.quit)
    return wd

def test_for_lection_4_task_1(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    menu_items_len = len(driver.find_elements_by_class_name("name"))

    x = 0

    if x < menu_items_len:
        menu_items = driver.find_elements_by_class_name("name")
        menu_items[x].click()
        element = driver.find_elements_by_tag_name("h1")
        assert len(element) == 1
        new_menu_items_len = len(driver.find_elements_by_class_name("name"))
        y = new_menu_items_len - menu_items_len
        c = 1
        if y > 0:
            menu_items = driver.find_elements_by_class_name("name")
            menu_items[x+c].click()
            element = driver.find_elements_by_tag_name("h1")
            assert len(element) == 1
            c+=1
            y-=1
        driver.find_element_by_class_name("logotype").click()
        x+=1

