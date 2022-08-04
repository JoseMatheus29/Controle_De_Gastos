from django.test import TestCase
from selenium import webdriver
from .views import transacao
from django.urls import resolve
import unittest

class TestGerenciador(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    def tearDown(self):
        self.browser.quit()

    def test_title_in_app(self):
        self.browser.get('http://127.0.0.1:8000/home')
        self.assertIn('Transacao', self.browser.title)

    def test_open_homePage(self):
        page = resolve('/home')
        self.assertEqual(transacao, page.func)

if __name__ == 'main':
    unittest.main(warnings=ignore)
