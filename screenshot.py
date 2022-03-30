""" Importando o módulo webdriver do Selenium """
from selenium import webdriver

""" Instanciando o navegador que irei usar """
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe")

""" Abro a página que quero navegar """
driver.get("https://statusinvest.com.br/fundos-imobiliarios/kfof11")

driver.maximize_window() # Abrir em tamanho total da tela

driver.get_screenshot_as_file(r'D:\screenshots\screenshot1.png') # Salva a tela em um arquivo

driver.close() # Fecha o navegador