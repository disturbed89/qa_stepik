from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text

    res = str(int(x) + int(y))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(res) 


    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()