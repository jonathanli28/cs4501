from django.test import TestCase

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class FrontEndLoginTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def test_login(self):
        driver = self.driver
        driver.get("http://159.203.136.147:8000/login")

        login = driver.find_element_by_id("username")
        login.send_keys("abc")

        password = driver.find_element_by_id("passwd")
        password.send_keys("abc")

        driver.find_element_by_xpath("//button[@type='submit' and @value='Submit']").click()


    def tearDown(self):
        self.driver.close()

class FrontEndLogoutTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/home/admin/cs4501/app/web/frontEnd/chromedriver')

    def test_logout(self):
        driver = self.driver
        driver.get("http://159.203.136.147:8000/login")

        login = driver.find_element_by_id("username")
        login.send_keys("abc")

        password = driver.find_element_by_id("passwd")
        password.send_keys("abc")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'container')))

        driver.find_element_by_xpath("//a[@href='/logout']").click()


    def tearDown(self):
        self.driver.close()


class FrontEndCreateItemTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/home/admin/cs4501/app/web/frontEnd/chromedriver')

    def test_creation(self):
        driver = self.driver
        driver.get("http://159.203.136.147:8000/login")

        login = driver.find_element_by_id("username")
        login.send_keys("abc")

        password = driver.find_element_by_id("passwd")
        password.send_keys("abc")

        driver.find_element_by_xpath("//button[@type='submit' and @value='Submit']").click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'container')))

        driver.get("http://159.203.136.147:8000/crlisting")

        name = driver.find_element_by_id('name')
        name.send_keys("boss")
        bike_style = driver.find_element_by_name("bike_style")
        bike_style.send_keys("boss")
        brake_style = driver.find_element_by_name("brake_style")
        brake_style.send_keys("boss")
        color = driver.find_element_by_name("color")
        color.send_keys("boss")
        frame_material = driver.find_element_by_name("frame_material")
        frame_material.send_keys("boss")
        speeds = driver.find_element_by_name("speeds")
        speeds.send_keys("boss")
        package_height = driver.find_element_by_name("package_height")
        package_height.send_keys("boss")
        shipping_weight = driver.find_element_by_name("shipping_weight")
        shipping_weight.send_keys("boss")
        wheel_size = driver.find_element_by_name("wheel_size")
        wheel_size.send_keys("boss")
        bike_description = driver.find_element_by_name("bike_description")
        bike_description.send_keys("boss")

        driver.find_element_by_xpath("//button[@type='submit' and @value='Submit']").click()
    def tearDown(self):
        self.driver.close()

class FrontEndSearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/home/admin/cs4501/app/web/frontEnd/chromedriver')

    def test_search(self):
        driver = self.driver

        driver.get("http://159.203.136.147:8000/search")

        query= driver.find_element_by_id("query")
        query.send_keys("boss")

        driver.find_element_by_css_selector(".btn.btn-default").click()
    def tearDown(self):
        self.driver.close()


if __name__== "__main__":
    unittest.main()
