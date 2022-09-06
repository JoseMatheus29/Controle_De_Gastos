import pyautogui as pc

pc.sleep(5)
pc.press('win')
pc.write('cmd')
pc.press('enter')
pc.sleep(2)
caminho = 'OneDrive\Documentos\Apresentacao tdd\Controle_de_Gastos'
pc.click(500,500)
pc.write(f'cd {caminho}')
pc.press('enter')
pc.write('py manage.py test')
pc.press('enter')
quit()