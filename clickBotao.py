""" Importando o módulo do Selenium """
from selenium import webdriver

""" Instanciando o navegador que irei usar """
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe")

""" Abro a página que quero navegar """
#driver.get('https://empresas.americanas.com.br/produto/1611315933/iphone-11-apple-64gb-preto-tela-6-1-4g-camera-12mp-ios?pfm_carac=Iphone%2011&pfm_index=0&pfm_page=category&pfm_pos=grid&pfm_type=vit_product_grid&sellerId')

""" Adiciono um tempo de espera implicito para o elemento aparecer na tela """
#driver.implicitly_wait(5) # Espera de 5 segundos.

#driver.find_element_by_id('btn-buy').click()

# Outra forma de fazer
# button = driver.find_element_by_id('btn-buy')
# button.click()

""" Abrindo a página """
driver.get('https://www.imdb.com/')

""" Procuro o elemento com nome 'q' que é o campo de busca e digito o nome do filme """
driver.find_element_by_name('q').send_keys('Titanic')

""" Tempo de espera implicito para o elemento aparecer na tela """
driver.implicitly_wait(5) # Espera de 5 segundos.

""" Clico na lupa para fazer a busca."""
driver.find_element_by_id('suggestion-search-button').click()

# Documentação
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.ui