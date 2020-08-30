import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_for_lection_8(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_xpath(".//a[contains(., 'Afghanistan')]").click()
    windows = {}
    windows["main_page"] = driver.current_window_handle
    external_links = driver.find_elements_by_xpath(".//i[contains(@class, 'fa-external-link')]")
    for link in external_links:
        link.click()
        open_windows = driver.window_handles
        for window in open_windows:
            if window not in windows:
                windows["second_page"] = window
        driver.switch_to.window(windows["second_page"])
        driver.close()
        driver.switch_to.window(windows["main_page"])

