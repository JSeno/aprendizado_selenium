""" Importando modulo Selenium """
from selenium import webdriver

""" Instanciando o navegador que irei usar """
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe")

""" Abro a página que quero navegar """
driver.get("https://www.e-crvsp.sp.gov.br/")

""" Adiciono um tempo de espera implicito para o elemento aparecer na tela """
driver.implicitly_wait(3) # Espera de 3 segundos.

framePagina = driver.find_elements_by_tag_name('frame')[1] # Busca o elementos pelo tag_name

driver.switch_to.frame(framePagina) # Muda para o frame

driver.find_element_by_name('codigo').send_keys('123456789') # Digita no campo de busca.
driver.find_element_by_name('senha').send_keys('123456789') # Digita no campo de busca.

# Exemplo 2

# driver.get('https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas-listadas.htm')

# driver.implicitly_wait(3) # Espera de 3 segundos.

# driver.switch_to.frame(bvmf_iframe) # Muda para o frame

# botao = driver.find_element_by_css_selector('#accordionName > div > app-companies - home - filter - name > form > div > div:nth-child(4) > button')
# botao.click()

# dados = driver.find_elements_by_class_name('card-body')
# sigla = dados[0].find_element_by_tag_name('h5').text
#nome = dados[0].find_element_by_class_name('card-title').text
# descricao = dados[0].find_element_by_class_name('card-text').text

# print(sigla)
# print(nome)
# print(descricao) 

