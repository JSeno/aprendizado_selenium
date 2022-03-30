""" Importando o Modulo Selenium """
from re import A
from selenium import webdriver

"""" Instanciando o navegador que irei usar """
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe")

""" Abro a página que quero navegar """
# driver.get("https://www.magazineluiza.com.br/smartphone-samsung-galaxy-a03-core-32gb-azul-4g-octa-core-2gb-ram-65-cam-8mp-selfie-5mp/p/233989900/te/galx/")

driver.get('https://www.magazineluiza.com.br/conjunto-de-xicara-de-cha-com-pires-06-pecas-puzzling-oxford/p/begc125kej/ud/cecn/')

driver.implicitly_wait(3) # Espera de 3 segundos.

# avaliacao = driver.find_element_by_class_name('js-rating-value').text # Busca o elemento pelo class_name


try:
    avaliacao = driver.find_element_by_class_name('js-rating-value').text # Busca o elemento pelo class_name

except:
    avaliacao = 'Não avaliado'



print(avaliacao)