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

def test_for_lection_4_task_1(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    menu_items_len = len(driver.find_elements_by_class_name("name"))

    x = 0

    while x < menu_items_len:
        menu_items = driver.find_elements_by_class_name("name")
        menu_items[x].click()
        try:
            Element = driver.find_element_by_tag_name('h1')
        except NoSuchElementException:
            return False
        new_menu_items_len = len(driver.find_elements_by_class_name("name"))
        y = new_menu_items_len - menu_items_len
        c = 1
        while y > 0:
            menu_items = driver.find_elements_by_class_name("name")
            menu_items[x+c].click()
            try:
                Element = driver.find_element_by_tag_name('h1')
            except NoSuchElementException:
                return False
            c+=1
            y-=1
        x+=1

    WebDriverWait(driver, 10).until(EC.title_is("vQmods | My Store"))

