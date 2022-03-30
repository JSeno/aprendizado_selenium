""" Importando o módulo webdriver do Selenium """
from selenium import webdriver

""" Instanciando o navegador que irei usar """
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe")


""" Abro a página que quero navegar """
driver.get("https://www.infomoney.com.br/")

driver.implicitly_wait(3) # Espera 3 segundos para o elemento aparecer na tela

""" Busco o elemento pelo id """
dados1 = driver.find_element_by_id("high").text # Busca o elemento pelo id
dados2 = driver.find_elements_by_id("high")[0].text # Busca uma lista de elementos pelo id

print(dados1)
print('----------')
print(dados2)

driver.get('https://empresas.americanas.com.br/produto/3742917483/smartphone-multilaser-e-32gb-5-android-8-1-camera-5mp-dourado?chave=hmem_cronometro_3742917483&cor=Dourado')

driver.implicitly_wait(3) # Espera 3 segundos para o elemento aparecer na tela

dados3 = driver.find_element_by_id("product-name-default").text # Não encontrei nesse site o id default, mas entendi a ideia.

print(dados3)


# Documentação
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.ui