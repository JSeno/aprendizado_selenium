""" Importando o Modulo Selenium """
from selenium import webdriver

""" Instanciando o navegador que irei usar """
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe")

""" Abro a página que quero navegar """
driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

""" Adiciono um tempo de espera implicito para o elemento aparecer na tela """
driver.implicitly_wait(3) # Espera de 3 segundos.

valorTabela = driver.find_elements_by_xpath("/html/body/main/div[2]/div[8]/div/div[6]/div/div[2]/table/tbody/tr[3]/td[3]")[0].text

proventos = driver.find_elements_by_xpath("/html/body/main/div[2]/div[8]/div/div[6]/div/div[2]/table/tbody/tr[3]/td[4]")[0].text

volumeAluguel = driver.find_elements_by_xpath("/html/body/main/div[2]/div[11]/div[2]/div[4]/div/div/strong")[0].text

nomeAdministrador = driver.find_elements_by_xpath("/html/body/main/div[3]/div/div/div[3]/div/div[2]/div[1]/div/strong")[0].text

""" Mostrando no console os resultados"""
print(valorTabela)
print(proventos)
print(volumeAluguel)
print(nomeAdministrador)


# Documentação
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.ui
