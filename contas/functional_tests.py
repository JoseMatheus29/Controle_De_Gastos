from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class TestNewVisitor(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Google()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://127.0.0.1:8000/")
        header_text = self.browser.find_element_by_tag_name("h2").text
        self.assertIn('Lista de transições',header_text)
        
