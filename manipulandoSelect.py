""" Importando o módulo selenium """
from selenium import webdriver
from selenium.webdriver.support.ui import Select # Importando o módulo Select do Selenium

""" Instanciando o navegador que irei usar """
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe")

""" Abro a página que quero navegar """
driver.get("https://imdb.com/title/tt0120338/videogallery/")

elementoSelect = Select(driver.find_element_by_name('sort')) # Busco o elemento que tem o name sort

elementoSelect.select_by_value('expiration') # Seleciono o valor expiration

driver.implicitly_wait(3) # Espera de 3 segundos.

elementoSelect = Select(driver.find_element_by_name('sort')) # Busco o elemento que tem o name sort

elementoSelect.select_by_visible_text('Date') # Seleciono o texto Date

Select(driver.find_element_by_name('sort')).select_by_index(1) # Seleciono o index 1

# Documentação
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.ui


