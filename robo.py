from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

compra = input("Oque você deseja comprar?: ")

class auto:
    def __init__(self):
        options = Options()
        self.webdriver =  webdriver.Chrome(options=options)
    def  busca(self, busca, max_resultados):
        resultado = 0
        url = (f"https://www.kabum.com.br/busca/{busca}")
        self.webdriver.get(url)
        #abre a opção de selecionar 
        escolha_promocao = self.webdriver.find_element(By.XPATH,"//select[@class='sc-5a083586-0 eGIppJ']")
        promocao = Select(escolha_promocao)
        promocao.select_by_index(7) #seleciona
        time.sleep(5)

        produtos = self.webdriver.find_elements(By.XPATH,"//span[@class='sc-d79c9c3f-0 nlmfp sc-27518a44-9 iJKRqI nameCard']")
        valores = self.webdriver.find_elements(By.XPATH,"//span[@class='sc-57f0fd6e-2 hjJfoh priceCard']")
        links = self.webdriver.find_elements(By.XPATH,"//a[@class='sc-27518a44-4 kVoakD productLink']")
        
        print("Esses foram os produtos em promoção encontrados")
        for produto, valor, link in zip (produtos, valores,links):
            if resultado <= max_resultados:
                print(f"{produto.text} {valor.text}\n{link.get_attribute('href')}\n\n")
                resultado +=1
       
bot = auto()
bot.busca(compra, 6)
input("aperte enter:")

