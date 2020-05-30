import unittest
from selenium import webdriver
import time 


class TestRegisration(unittest.TestCase):
    def steps(tmp_link):
        browser = webdriver.Chrome()
        browser.get(tmp_link)               
        input1 = browser.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block .third")
        input3.send_keys("Ivan@gmail.com")        
        button = browser.find_element_by_xpath("//button[text()='Submit']")
        button.click()      
        time.sleep(5)
        res_tmp = browser.find_element_by_tag_name("h1").text
        browser.quit()
        return res_tmp

    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        res = TestRegisration.steps(link)
        self.assertEqual(res, "Congratulations! You have successfully registered!", "Error registration")

    def test_reg2(self):        
        link = "http://suninjuly.github.io/registration2.html"
        res = TestRegisration.steps(link)
        self.assertEqual(res, "Congratulations! You have successfully registered!", "Error registration")



        
if __name__ == "__main__":
    unittest.main()