""" Importação da biblioteca do Selenium """
from selenium import webdriver

""" Instanciando o navegador que irei usar """
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe")

""" Abro a página que quero navegar """
driver.get("https://statusinvest.com.br/fundos-imobiliarios/kfof11")

""" Espera 3 segundos para o elemento aparecer na tela """
driver.implicitly_wait(3) # Espera 3 segundos para o elemento aparecer na tela

driver.execute_script('window.open()') # Abre uma nova janela

driver.switch_to.window(driver.window_handles[1]) # Abre a nova janela

driver.get("https://statusinvest.com.br/fundos-imobiliarios/kfof11") # Abre a nova janela

driver.implicitly_wait(3) # Espera 3 segundos para o elemento aparecer na tela

driver.switch_to.window(driver.window_handles[0]) # Abre a nova janela

driver.close() # Fecha a nova janela