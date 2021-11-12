from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from datetime import datetime
import openpyxl as xl
from bs4 import BeautifulSoup
import os
from webdriver_manager.chrome import ChromeDriverManager

diccionario={"PARAISO_A":"MBOHED00100A","PARAISO_B":"MBOHED00101A","PARAISO_M":"MBOHED00112A",}

entrada=input("Buscar por nodo o abonado?")
if entrada=="abonado":
	cliente=input("Introduzca el numero de abonado: ")
else:
	nodo=input("Escriba el nodo que quiere buscar: ")

driver = webdriver.Chrome()
driver.get("http://nas.net-uno.net/nas2/htdocs/inicio.php")
wb= xl.Workbook()
wa=wb.active
wa.title=diccionario.get(nodo)

def sopa(html):
	b=BeautifulSoup(html,"html.parser")
	return b
	
def selection(a):
	b=Select(driver.find_element_by_id(a))
	return b

def log_in():
	Userelem= driver.find_element_by_name("login")
	print(Userelem)
	Userelem.send_keys("operatormbo")
	Pwelem= driver.find_element_by_name("password")
	Pwelem.send_keys("123456")
	clickElem= driver.find_element_by_link_text("Entrar")
	clickElem.click()
	driver.get("http://nas.net-uno.net//nas2/htdocs/ftth_mbo/ftth_con_ont.php")

log_in()

def driver_wait(a):
    WebDriverWait(driver,a)

driver_wait(30)

nodoSelect= selection("text_nodo_nuevo")
nodoSelect.select_by_value(diccionario.get(nodo))
driver_wait(30)
driver_wait(30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div[2]/h2/a"))).click()
driver_wait(5) #Con lo anterior me sale una página con todos los abonados
soup=sopa(driver.page_source)
abonados=soup.find_all('tr')

empty=[]
for item in abonados:
	c=item.get("id")
	empty.append(c)
lista=empty[8:]
c=1

for i in lista:
	contrato= driver.find_element_by_id("text_contrato_nuevo")
	contrato.send_keys(i)
	driver_wait(30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div[2]/h2/a"))).click()
	driver_wait(30).until(EC.element_to_be_clickable((By.ID,i))).click()
	driver_wait(30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/table[1]/tbody/tr[14]/td/a"))).click()
	driver_wait(30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/h2/a")))
	soup=sopa(driver.page_source)
	contrato.clear()
	detalle=soup.find(id="ftth_con_ont_div_1") #el codigo html dentro del tag div con la id que se especifica, se debe convertir en string para sopa.
	Info_Basica=sopa(str(detalle))
	Info_Basica_lista=[]

	for i in Info_Basica.find_all("td"):
		x=i.string
		Info_Basica_lista.append(x)

	weed_out=[1,3,5,7,9,13]
	Info_Basica_FINAL=[]
	for i in weed_out:
		Info_Basica_FINAL.append(Info_Basica_lista[i])

	try:
		driver_wait(5).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/table[2]/tbody/tr[1]/th")))#Texto ONT INFO del cuadro que sale
		info=Info_Basica.find_all("pre")
		buscar=["ONT distance(m)","Last down cause","Last down time","IPv4 Connection status","Rx optical power(dBm)","fin"]
		infostring=info[0].string.splitlines()+info[1].string.splitlines()+info[2].string.splitlines()
		contador=0
		for linea in infostring:
			if contador == len(buscar):
				break
			elif buscar[contador] in linea:
				exacta_info=linea.split(":")
				Info_Basica_FINAL.append(exacta_info[1])
				contador+=1
			else:
				continue
	except:
		Info_Basica_FINAL=["SI"+"SI"+"SI"+"SI"+"SI"+"SI"+"SI"+"SI"+"SI"+"SI"+"SI"+"SI"]

	wa.append(Info_Basica_FINAL)
else:
	print('listo')

now=datetime.now()
fecha=now.strftime("%d-%m-%Y")
pathacon=os.path.dirname(os.path.abspath(__file__))
destino=pathacon+"\\"+nodo+fecha+".xlsx"
wb.save(filename= destino)

driver.quit()