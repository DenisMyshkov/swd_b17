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

def test_for_lection_5_task_2(driver):
    driver.get("http://localhost/litecart/")
    product = driver.find_elements_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[4]/div/ul/li")[0]

    product_name = product.find_element_by_xpath("./a[1]").get_attribute("title")
    price_normal = product.find_element_by_xpath("./a[1]/div[4]/s").get_attribute("innerText")
    price_normal_text_decoration = product.find_element_by_xpath("./a[1]/div[4]/s").value_of_css_property("text-decoration-line")
    price_normal_color = product.find_element_by_xpath("./a[1]/div[4]/s").value_of_css_property("color")
    a = int(price_normal_color[5:8])
    b = int(price_normal_color[10:13])
    c = int(price_normal_color[15:18])
    price_normal_font_size = float(product.find_element_by_xpath("./a[1]/div[4]/s").value_of_css_property("font-size")[0:-2])
    price_special = product.find_element_by_xpath("./a[1]/div[4]/strong").get_attribute("innerText")
    price_special_font_weight = product.find_element_by_xpath("./a[1]/div[4]/strong").value_of_css_property("font-weight")
    price_special_color = product.find_element_by_xpath("./a[1]/div[4]/strong").value_of_css_property("color")
    price_special_font_size = float(product.find_element_by_xpath("./a[1]/div[4]/strong").value_of_css_property("font-size")[0:-2])

    product.click()

    pp_name = driver.find_element_by_tag_name("h1").get_attribute("innerText")
    pp_price_normal = driver.find_element_by_class_name("regular-price").get_attribute("innerText")
    pp_price_normal_text_decoration = driver.find_element_by_class_name("regular-price").value_of_css_property("text-decoration-line")
    pp_price_normal_color = driver.find_element_by_class_name("regular-price").value_of_css_property("color")
    pp_price_special = driver.find_element_by_class_name("campaign-price").get_attribute("innerText")
    pp_price_special_font_weight = driver.find_element_by_class_name("campaign-price").value_of_css_property("font-weight")
    pp_price_special_color = driver.find_element_by_class_name("campaign-price").value_of_css_property("color")
    d = int(pp_price_normal_color[5:8])
    e = int(pp_price_normal_color[10:13])
    f = int(pp_price_normal_color[15:18])
    pp_price_normal_font_size = float(driver.find_element_by_class_name("regular-price").value_of_css_property("font-size")[0:-2])
    pp_price_special_font_size = float(driver.find_element_by_class_name("campaign-price").value_of_css_property("font-size")[0:-2])

    assert product_name == pp_name
    assert price_normal == pp_price_normal
    assert price_normal_text_decoration == pp_price_normal_text_decoration
    assert a == b == c
    assert price_normal_font_size < price_special_font_size
    assert price_special == pp_price_special
    assert price_special_font_weight == pp_price_special_font_weight 
    assert d == e == f
    assert pp_price_normal_font_size < pp_price_special_font_size

