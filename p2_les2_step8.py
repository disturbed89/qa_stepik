from selenium import webdriver
import math
import time
import os 

try: 
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    
    input1 = browser.find_element_by_xpath("//input[@name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//input[@name='email']")
    input3.send_keys("Ivan@gmail.com")

    element = browser.find_element_by_xpath("//input[@name='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'env.txt')
    element.send_keys(file_path)
    
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()