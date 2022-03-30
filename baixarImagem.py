""" Importando o módulo selenium """
from selenium import webdriver
import urllib.request

""" Instanciando o navegador que irei usar """
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe")

""" Abro a página que quero navegar """
driver.get("https://www.imdb.com./title/tt0120338/mediaindex?ref_=tt_pv_mi_sm")

""" Adiciono um tempo de espera implicito para o elemento aparecer na tela """
driver.implicitly_wait(3) # Espera de 3 segundos.

divImagens = driver.find_element_by_id('media_index_thumbnail_grid') # Busca o elemento pelo id

primeiraImagem = divImagens.find_elements_by_tag_name('img')[0] # Busca o elemento pelo tag_name

atributoHref = primeiraImagem.get_attribute('src') # Busca o atributo src


try: # Tenta fazer o download da imagem
    urllib.request.urlretrieve(atributoHref, r'D:\screenshots\teste.jpg') # Salva a imagem
    print('Imagem salva com sucesso!')

except: # Se der erro, mostra a mensagem
    print('Erro ao salvar a imagem!')