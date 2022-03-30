""" Importando o módulo webdriver do Selenium """
from selenium import webdriver

""" Instanciando o navegador que irei usar """
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe")

""" Abro a página que quero navegar """
driver.get("https://statusinvest.com.br/fundos-imobiliarios/kfof11")

""" Espera 3 segundos para o elemento aparecer na tela """
driver.implicitly_wait(3) # Espera 3 segundos para o elemento aparecer na tela

nomeFii = driver.find_elements_by_tag_name('h1')[0].text # Busca de elemento pelo tag_name

valorAtual = driver.find_elements_by_tag_name('strong')[0].text # Busca de elemento pelo tag_name em uma lista

tabelaRendimentos = driver.find_elements_by_tag_name('table')[0].text # Busca de elemento pelo tag_name em uma lista

tabelaResultados = driver.find_elements_by_tag_name('table')[1].text # Busca de elemento pelo tag_name em uma lista

print(nomeFii)
print(valorAtual)
print(tabelaRendimentos)
print(tabelaResultados)


# Documentação
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.ui
