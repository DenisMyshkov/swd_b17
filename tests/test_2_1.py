import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_for_lection_2_task_1(driver):
    driver.get("http://google.com/")
    WebDriverWait(driver, 10).until(EC.title_is("Google"))

