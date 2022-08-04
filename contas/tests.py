from django.test import TestCase
from selenium import webdriver
import unittest

class TestGerenciador(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    def tearDown(self):
        self.browser.quit(self)

    def test_title_in_app(self):
        self.browser.get('http://127.0.0.1:8000/home')
        self.assertIn('Transacao', self.browser.title)
    
if __name__ == 'main':
    unittest.main(warnings=ignore)
