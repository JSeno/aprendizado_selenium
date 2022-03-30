""" Importando modulo Selenium """
from selenium import webdriver

""" Instanciando o navegador que irei usar """
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe")

""" Abro a página que quero navegar """
driver.get("https://www.imdb.com/title/tt0120338/?ref_-fn_al_tt_1")

driver.minimize_window() # Minimizo a janela do navegador.

driver.implicitly_wait(2) # Espera de 2 segundos.

driver.maximize_window() # Maximizo a janela do navegador.

driver.implicitly_wait(2) # Espera de 2 segundos.

driver.get('https://empresas.americanas.com.br/produto/1611315933/iphone-11-apple-64gb-preto-tela-6-1-4g-camera-12mp-ios?pfm_carac=Iphone%2011&pfm_index=0&pfm_page=category&pfm_pos=grid&pfm_type=vit_product_grid&sellerId')

driver.back() # Volto para a página anterior.

driver.implicitly_wait(5) # Espera de 5 segundos.

driver.refresh() # Atualiza a página.

driver.implicitly_wait(5) # Espera de 5 segundos.

driver.close() # Fecho a janela do navegador.

# Documentação
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.ui


