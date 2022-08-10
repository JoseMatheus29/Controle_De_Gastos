from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class TestVisitor(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r'C:\Users\mateu\OneDrive\Área de Trabalho\Apresentação tdd\Controle_de_Gastos\chromedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_add_an_account_and_go_back_to_the_home_page(self):
        self.browser.get("http://127.0.0.1:8000/home")
        header_text = self.browser.find_element(By.TAG_NAME, 'h2').text
        print(header_text)

        new_account = self.browser.find_element(By.NAME, 'NovaConta')

        new_account.send_keys(Keys.ENTER)

        category = self.browser.find_element(By.NAME, 'categoria')
        category.click()
        category.send_keys(Keys.ARROW_DOWN)
        category.send_keys(Keys.ENTER)

        date = self.browser.find_element(By.NAME, 'data')
        date.send_keys('10/08/2022')


        value = self.browser.find_element(By.NAME, 'valor')
        value.send_keys(200)

        description = self.browser.find_element(By.NAME, 'descricao')
        description.send_keys('test')

        comments = self.browser.find_element(By.NAME, 'observacoes')
        comments.send_keys('test')

        save = self.browser.find_element(By.NAME, 'salvar')

        time.sleep(2)





      

