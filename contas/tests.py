from django.test import TestCase
from selenium import webdriver
from .views import transacao
from django.urls import resolve
from django.http import HttpRequest
import unittest

class TestGerenciador(unittest.TestCase):

    def test_roort_url_resolves_to_homePage(self):
        page = resolve('/home')
        self.assertEqual(transacao, page.func)

    def test_home_page_returns_html(self):
        request = HttpRequest()
        response = transacao(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith(''))
        self.assertIn('<title>Transacao</title>', html)
        self.assertTrue(html.endswith('</html>'))
        
if __name__ == 'main':
    unittest.main(warnings=ignore)
