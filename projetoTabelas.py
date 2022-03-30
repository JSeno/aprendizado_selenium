""" Importando o módulo selenium """
from selenium import webdriver
import pandas as pd # Importando o módulo pandas


""" Instanciando o navegador que irei usar """
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe")

""" Abro a página que quero navegar """
driver.get('https://br.investing.com/commodities/crude-oil-historical-data')

try: # Tentando encontrar o elemento
    driver.find_element_by_id('onetrust-accept-btn-handler').click() # Clica no botão de aceitar cookies.

except: # Se não encontrar o elemento
    print('Não existe alerta!') # Mostra que não existe alerta.

driver.implicitly_wait(5) # Espera de 5 segundos.

try: # Tentando encontrar o elemento
    driver.find_element_by_css_selector('#PromoteSignUpPopUp > div.right > 1').click() # Clica no botão de aceitar cookies.

except: # Se não encontrar o elemento
    print('Não há pop up') # Mostra que não existe alerta.


driver.find_element_by_id('widgetFieldDateRange').click() # Clica no campo de data.

dataInicial = driver.find_element_by_id('startDate') # Busca o elemento que tem o id startDate
dataFinal = driver.find_element_by_id('endDate') # Busca o elemento que tem o id endDate

driver.implicitly_wait(5) # Espera de 5 segundos.

dataInicial.clear() # Limpa o campo de data.
dataFinal.clear() # Limpa o campo de data.

driver.implicitly_wait(5) # Espera de 5 segundos.

dataInicial.send_keys('10/01/2019') # Preenche o campo de data.
dataFinal.send_keys('01/01/2021') # Preenche o campo de data.

driver.find_element_by_id('applyBtn').click() # Clica no botão de aplicar.

dados = [] # Cria uma lista vazia
dadosTabela = driver.find_element_by_id('curr_table') # Busca o elemento que tem o id curr_table

for linha in dadosTabela.find_elements_by_tag_name('tr'): # Para cada linha da tabela
    linhaDados = [] # Cria uma lista vazia
    for coluna in linha.find_elements_by_tag_name('td'): # Para cada coluna da linha
        linhaDados.append(coluna.text) # Adiciona o texto da coluna na lista
        dados.append(linhaDados) # Adiciona a lista na lista principal

df = pd.DataFrame(dados) # Cria um dataframe a partir da lista
df = df.iloc[1:, :] # Remove a primeira linha

df.columns = ['Data', 'Último', 'Abertura', 'Máxima', 'Mínima', 'vol', 'var%'] # Renomeia as colunas

print(df) # Mostra o dataframe

df.to_csv('dadosOil.csv') # Salva o dataframe em um arquivo csv
            