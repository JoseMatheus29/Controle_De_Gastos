from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class TestVisitor(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r'C:\Users\mateu\OneDrive\Área de Trabalho\Apresentação tdd\Controle_de_Gastos\chromedriver.exe')
        self.browser.get("http://127.0.0.1:8000/home")

    def tearDown(self):
        self.browser.quit()

    def test_add_an_account_and_go_back_to_the_home_page(self):
        #inserindo nova conta
        new_account = self.browser.find_element(By.NAME, 'NovaConta')
        new_account.send_keys(Keys.ENTER)

        #selecionando categoria
        category = self.browser.find_element(By.NAME, 'categoria')
        category.click()
        category.send_keys(Keys.ARROW_DOWN)
        category.send_keys(Keys.ENTER)

        #adicionando a data
        date = self.browser.find_element(By.NAME, 'data')
        date.send_keys('10/08/2022')

        #adicionando o valor
        value = self.browser.find_element(By.NAME, 'valor')
        value.send_keys(200)

        #adicionando descrição
        description = self.browser.find_element(By.NAME, 'descricao')
        description.send_keys('test')

        #adicionando observações
        comments = self.browser.find_element(By.NAME, 'observacoes')
        comments.send_keys('test')

        #salvando nova conta
        save = self.browser.find_element(By.ID, 'salvar')
        save.send_keys(Keys.ENTER)

        #verificando a tabela
        table = self.browser.find_element(By.TAG_NAME, 'table')
        tr = table.find_element(By.ID, 'Valores')
        self.assertEqual(tr.text, 'test 200.00 Diversos Out. 8, 2022')

       
    def test_remove_and_update_an_account_and_go_back_to_the_home_page(self):

        with self.subTest('Test of update'):
            # Verificando a tabela
            table = self.browser.find_element(By.TAG_NAME, 'table')

            # Selecionando elemento para remover
            atualizar = table.find_element(By.ID, 'remove')
            atualizar.click()

            # Mudando a descrição
            description = self.browser.find_element(By.NAME, 'descricao')
            description.send_keys('1')
            # Selecionando ação de atualizar
            acaoAtt = self.browser.find_element(By.ID, 'salvar')
            acaoAtt.click()

            table1 = self.browser.find_element(By.TAG_NAME, 'table')
            atualizado = table1.find_element(By.ID, 'remove')

            # Verificando a execeção chamada pois elemento não existe mais
            self.assertEqual(atualizado.text, 'test1')

            with self.subTest('Test of delete'):
                # Verificando a tabela
                table = self.browser.find_element(By.TAG_NAME, 'table')

                # Selecionando elemento para remover
                remover = table.find_element(By.ID, 'remove')
                remover.click()

                # Selecionando ação de remover
                acaoRemover = self.browser.find_element(By.ID, 'delete')
                acaoRemover.click()

                # Verificando a execeção chamada pois elemento não existe mais
                with self.assertRaises(Exception):
                    print(remover.text)





      

