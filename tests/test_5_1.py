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

def test_for_lection_5_task_1_chapter_a(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    country_list = []
    table = driver.find_element_by_xpath("/html/body/div/div/div/table")
    rows = table.find_elements_by_tag_name("tr.row")

    for row in rows:
        country_list.append(row.find_element_by_xpath("./td[5]").text)

    x = 1
    y = 0
    while x < len(country_list) - 1:
        if country_list[x] > country_list[x+1]:
            y = 1
        else:
            x+=1
    assert y == 0

def test_for_lection_5_task_1_chapter_b(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")

    table = driver.find_element_by_xpath("/html/body/div/div/div/table")
    rows = table.find_elements_by_tag_name("tr.row")
    country_with_zones = []
    for row in rows:
        if int(row.find_element_by_xpath("./td[6]").text) > 0:
            country_with_zones.append(row.find_element_by_xpath("./td[5]/a").get_attribute('href'))

    y = 0
    for country in country_with_zones:
        driver.get(country)
        zones_table = driver.find_element_by_xpath("/html/body/div/div/div/table/tbody/tr/td[3]/form/table[2]/tbody")
        rows = zones_table.find_elements_by_tag_name("tr")

        zones_list = []
        for row in rows[1:-1]:
            zones_list.append(row.find_element_by_xpath("./td[3]").get_attribute('innerText'))

        x = 1
        while x < len(zones_list) - 1:
            if zones_list[x] > zones_list[x+1]:
                y = 1
            else:
                x+=1
    assert y == 0


def test_for_lection_5_task_2(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")

    table = driver.find_element_by_xpath("/html/body/div/div/div/table/tbody/tr/td[3]/form/table/tbody")
    rows = table.find_elements_by_tag_name("tr.row")
    country_with_zones = []
    for row in rows:
        country_with_zones.append(row.find_element_by_xpath("./td[3]/a").get_attribute('href'))

    y = 0
    for country in country_with_zones:
        driver.get(country)
        zones_table = driver.find_element_by_xpath("/html/body/div/div/div/table/tbody/tr/td[3]/form/table[2]/tbody")
        rows = zones_table.find_elements_by_tag_name("tr")

        zones_list = []
        for row in rows[1:-1]:
            zones_list.append(row.find_element_by_xpath("./td[3]/select/option[@selected='selected']").get_attribute('innerText'))

        x = 1
        while x < len(zones_list) - 1:
            if zones_list[x] > zones_list[x+1]:
                y = 1
            else:
                x+=1
    assert y == 0


