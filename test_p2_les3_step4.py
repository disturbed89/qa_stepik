from selenium import webdriver
import math
import time
import os 

try: 
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    
    button = browser.find_element_by_css_selector("button")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y =  str(math.log(abs(12*math.sin(int(x)))))
    y_element = browser.find_element_by_id("answer")
    y_element.send_keys(y)

    
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
    