from selenium import webdriver
import math
import time

try: 

    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x = browser.find_element_by_id("input_value").text

    y =  str(math.log(abs(12*math.sin(int(x)))))

    y_element = browser.find_element_by_id("answer")
    y_element.send_keys(y)


    r_check = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", r_check)
    r_check.click()

    r_radio = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", r_radio)
    r_radio.click()




    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()