from django.test import TestCase

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class FrontEndTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox

    def step_impl(self):
        driver = self.driver
        driver.get("127.0.0.1:8000/login")

        login = driver.find_element_by_id("Username")
        login.send_keys("ianian")

        password = driver.find_elemnt_by_id("Password")
        password.send_keys("pbkdf2_sha256$20000$exwutgpqJGHU$RYW6u5d/ikcxCv5qnXCW0NbwCRXPTE0uWZczlS5nros=")

        driver.find_element("Login").click()

    def tearDown(self):
        self.driver.close()



