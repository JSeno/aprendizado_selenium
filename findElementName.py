""" Importando o Modulo Selenium """
from selenium import webdriver

""" Instanciando o navegador que irei usar """
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe")

""" Abro a página que quero navegar """
driver.get("https://www.imdb.com/")

""" Adiciono um tempo de espera implicito para o elemento aparecer na tela """
driver.implicitly_wait(3) # Espera de 3 segundos.

campoBusca = driver.find_elements_by_name('q')[0] # Busca o elemento pelo nome que no caso é o campo de busca.

campoBusca.send_keys('Titanic') # Digita no campo de busca.

