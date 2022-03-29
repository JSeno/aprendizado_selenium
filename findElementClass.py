""" Importação da biblioteca do Selenium """
from selenium import webdriver

""" Instanciando o driver do navegador que irei usar """
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe")

""" Abro a página que quero navegar """
driver.get('https://statusinvest.com.br/fundos-imobiliarios/kfof11')

""" Espera 3 segundos para o elemento aparecer na tela """
driver.implicitly_wait(3) # Espera 3 segundos para o elemento aparecer na tela  

""" Busca dos elementos dentro da página pelo nome da classe"""
dados0 = driver.find_element_by_class_name('value').text # Busca de elemento pelo class_name
dados1 = driver.find_elements_by_class_name('value')[0].text # Busca de elemento pelo class_name em uma lista
dados2 = driver.find_elements_by_class_name('value')[3].text # Busca de elemento pelo class_name em uma lista
dados3 = driver.find_elements_by_class_name('value')[4].text # Busca de elemento pelo class_name em uma lista

# Mostra os dados na tela
print(dados0)
print(dados1)
print(dados2)
print(dados3)