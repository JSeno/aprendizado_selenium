""" Importando modulo Selenium """
from selenium import webdriver

""" Importando Pandas """
import pandas as pd

""" Instanciando o navegador que irei usar """
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe")

""" Abro a página que quero navegar """
driver.get('https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/derivativos/ajustes-do-pregao/')

driver.switch_to.frame('bvmf_iframe')

tabela = driver.find_element_by_id('tblDadosAjustes')

m = []

for linha in tabela.find_elements_by_tag_name('tr'):
    linhaDados = []
    for coluna in linha.find_elements_by_tag_name('td'):
        linhaDados.append(coluna.text)
    m.append(linhaDados)

df = pd.DataFrame(m)
print(df)