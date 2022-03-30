""" Importando o módulo webdriver do Selenium """
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

""" Instanciando o navegador que irei usar """
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe")

""" Abro a página que quero navegar """
driver.get("https://www.imdb.com/")

""" Adiciono um tempo de espera implicito para o elemento aparecer na tela """
driver.implicitly_wait(3) # Espera de 3 segundos.

driver.find_elements_by_name('q')[0].send_keys('Titanic' + Keys.RETURN) # Digita no campo de busca e aperta enter.