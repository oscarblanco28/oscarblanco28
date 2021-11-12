from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import openpyxl as xl
from bs4 import BeautifulSoup

chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-proxy-server')
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument('---proxy-bypass-list=*')
PATHDRIVER = r"C:\Users\Oscar\Desktop\Python\scrap\chromedriver.exe"
driver= webdriver.Chrome(chrome_options=chrome_options, executable_path=PATHDRIVER)
driver.get("http://nas.net-uno.net/nas2/htdocs/inicio.php")
wb= xl.Workbook()
destino=r"C:\Users\Oscar\Desktop\Prueba6.xlsx"
ws=wb.active
ws.title="MBOHED00106A"

def sopa(html):
	b=BeautifulSoup(html,"html.parser")
	return b
def perfectinfo(a):
	if a == 53:
		b=[11,30,31]
		return b
	else:
		c=[11,31,32]
		return c

def perfectwan(a):
	if a == 40:
		b=[14,21]
		return b
	else:
		c=[15,22]
		return c

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

wait= WebDriverWait(driver,30)
microwait=WebDriverWait(driver,1)

nodoSelect= selection("text_nodo_nuevo")
nodoSelect.select_by_value("MBOHED00106A")
wait= WebDriverWait(driver,30)
microwait=WebDriverWait(driver,1)
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div[2]/h2/a"))).click()
time.sleep(5)
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
	wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div[2]/h2/a"))).click()
	wait.until(EC.element_to_be_clickable((By.ID,i))).click()
	wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/table[1]/tbody/tr[12]/td/a"))).click()
	wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/h2/a")))
	soup=sopa(driver.page_source)
	contrato.clear()
	detalle=soup.find(id="ftth_con_ont_div_1") #el codigo html dentro del tag div con la id que se especifica, se debe convertir en string para sopa.
	Info_Basica=sopa(str(detalle))
	Info_Basica_lista=[]
	for i in Info_Basica.find_all("td"):
		x=i.string
		Info_Basica_lista.append(x)

	weed_out=[1,3,5,7,11,15,17]
	Info_Basica_FINAL=[]
	for i in weed_out:
		Info_Basica_FINAL.append(Info_Basica_lista[i])

	try:
		microwait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/table[2]/tbody/tr[1]/th")))
		ONT=Info_Basica.find_all("pre")
		#INFO_ONT
		INFO_ONT=ONT[0].string.splitlines()
		
		x=len(INFO_ONT[30])
		perfect_info=perfectinfo(x)

		weed_out_INFO_ONT=perfect_info
		INFO_ONT_FINAL=[]
		for i in weed_out_INFO_ONT:
			pl=INFO_ONT[i][27:]
			INFO_ONT_FINAL.append(pl)

		INFO_WAN=ONT[1].string.splitlines()

		y=len(INFO_WAN[14])
		perfect_wan=perfectwan(y)

		weed_out_INFO_WAN=perfect_wan
		INFO_WAN_FINAL=[]
		for i in weed_out_INFO_WAN:
			yl=INFO_WAN[i][30:]
			INFO_WAN_FINAL.append(yl)

		INFO_OPTIC=ONT[2].string.splitlines()
		weed_out_INFO_OPTIC=[16,19]
		INFO_OPTIC_FINAL=[]
		for i in weed_out_INFO_OPTIC:
			zl=INFO_OPTIC[i][42:]
			INFO_OPTIC_FINAL.append(zl)

		TOTAL=Info_Basica_FINAL+INFO_ONT_FINAL+INFO_WAN_FINAL+INFO_OPTIC_FINAL
	except TimeoutException:
		TOTAL=Info_Basica_FINAL+["S/I","S/I","S/I","S/I","S/I","S/I","S/I"]

	print(c)
	c=c+1	
	ws.append(TOTAL)

wb.save(filename= destino)

driver.quit()

