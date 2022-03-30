""" Importando o modulo Selenium """
from selenium import webdriver

""" Instanciando o navegador que irei usar """
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe")

""" Abro a página que quero navegar """
driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

elementoAImagem = driver.find_element_by_class_name('navbar-brand') # Busco o elemento que tem a classe navbar-brand
elementoImg = elementoAImagem.find_element_by_tag_name('img') # Busco o elemento que tem a tag img dentro do elemento que tem a classe navbar-brand
atributoSrc = elementoImg.get_attribute('src') # Pego o atributo src do elemento que tem a tag img dentro do elemento que tem a classe navbar-brand
print(atributoSrc) #

driver.get('https://www.melhorcambio.com/dolar-hoje') # Abro a página que quero navegar

elementoCotacao = driver.find_element_by_id('comercial') # Busco o elemento que tem a classe comercial
valorCotação = elementoCotacao.get_attribute('value') # Pego o atributo value do elemento que tem a classe comercial
classeElemento = elementoCotacao.get_attribute('class') # Pego o atributo class do elemento que tem a classe comercial
tipoElemento = elementoCotacao.get_attribute('type') # Pego o atributo type do elemento que tem a classe comercial

print(valorCotação) # Imprimo o valor da cotação
print(classeElemento) # Imprimo a classe do elemento
print(tipoElemento) # Imprimo o tipo do elemento

driver.close() # Fecho a janela do navegador.


# Documentação
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.ui