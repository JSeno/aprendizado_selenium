"""Importando modulo Selenium"""
from selenium import webdriver

"""Instanciando o navegador que irei usar"""
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe")

"""Abro a página que quero navegar"""
driver.get('https://br.gearbest.com/celulares-c_11293/')

"""Adiciono um tempo de espera implicito para o elemento aparecer na tela"""
driver.implicitly_wait(3) # Espera de 3 segundos.

listaLinks = [] # Cria uma lista vazia.

existePagina = True # Cria uma variavel que vai receber True.
primeiraPagina = True # Cria uma variavel que vai receber True.

while (existePagina):

    if(primeiraPagina):
        primeiraPagina = False

    else:
        try: # Tenta executar o codigo abaixo.
            driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div/footer/div[2]/div/a[5]/1').click() # Clica no botão de paginação.
            driver.implicitly_wait(3) # Espera de 3 segundos.

        except: # Se der erro, executa o codigo abaixo.
            print('Acabaram as páginas')
            existePagina = False # Altera a variavel para False.
            driver.close() # Fecha o navegador.
    
    for produtoAtual in driver.find_element_by_class_name('gbGoodsItem_outBox'):
        link = produtoAtual.find_element_by_tag_name('a')
        listaLinks.append(link.get_attribute('href'))

    for linkAtual in listaLinks:
        driver.get(linkAtual)
        driver.implicitly_wait(3) # Espera de 3 segundos.

        nomeProduto = driver.find_element_by_class_name('goodsIntro_title').text
        preco = driver.find_element_by_id('js-panelIntroNormalPrice').find_element_by_tag_name('span').text

        try:
            avaliacao = driver.find_element_by_class_name('gbStarGrade_count').text

        except:
            avaliacao = 'Não avaliado'

        print(nomeProduto)
        print(preco)
        print(avaliacao)
        

