""" Só estaremos usando o webdriver do selenium e não a biblioteca inteira. """
from selenium import webdriver

""" Aqui faço a instanciação do navegador que usarei no selenium. """
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe")

""" Comando quando for usar o Firefox - Não instalei o webdriver do firefox nem mesmo o navegador. """
#driver = selenium.Firefox(executable_path=r"E:\Webdriver\geckodriver.exe")

""" Aqui abro a página que quero navegar. """	
driver.get("https://www.google.com")