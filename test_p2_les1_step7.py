from selenium import webdriver
import math
import time

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element_by_css_selector("img")
    x_res = x_element.get_attribute("valuex")
    y =  str(math.log(abs(12*math.sin(int(x_res)))))
    y_element = browser.find_element_by_id("answer")
    y_element.send_keys(y)

    r_check = browser.find_element_by_id("robotCheckbox")
    r_check.click()

    r_radio = browser.find_element_by_id("robotsRule")
    r_radio.click()


    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
    