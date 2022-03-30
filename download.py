"""Importando o módulo webdriver do Selenium"""
from ssl import Options
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_experimental_option('prefs',{
    'download.default_directory': r'D:\downloads',
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
})

"""Instanciando o navegador que irei usar"""
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe", chrome_options=options)

"""Abro a página que quero navegar"""
driver.get("https://www.opera.com/pt-br/download/")

spanBotao = driver.find_element_by_xpath('/html/body/main/section[1]/div/div/div[1]/div/span')
linkBotao = spanBotao.find_element_by_tag_name('a')
linkBotao.click()
