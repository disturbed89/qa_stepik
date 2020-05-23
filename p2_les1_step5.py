from selenium import webdriver
import math
import time

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y =  str(math.log(abs(12*math.sin(int(x)))))
    y_element = browser.find_element_by_id("answer")
    y_element.send_keys(y)

    r_check = browser.find_element_by_id("robotCheckbox")
    r_check.click()

    r_radio = browser.find_element_by_css_selector("[for='robotsRule']")
    r_radio.click()


    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
    