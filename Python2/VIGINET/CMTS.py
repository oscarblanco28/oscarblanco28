import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook


#URLL="http://172.30.31.17/cmts1/index.php"
#payload={"port":"",
#"status":""}

#with requests.Session() as session:
#	session.get(URLL)
#	p=session.post(URLL,data=payload)
#	f=p.text

def func1():
	with open(r"C:\Users\Oscar\Desktop\newtext.txt","r") as readd:
		nodos=readd.read()
		print("Archivo abierto")

def sopa():
	soup=BeautifulSoup(nodos,"html.parser")
	c=soup.pre.string

def escribir():
	with open(r"C:\Users\Oscar\Desktop\newtext.txt","w") as nodofile:
		nodofile.write(c)
		print("archivo escrito con exito")

lines=[]
with open(r"C:\Users\Oscar\Desktop\newtext.txt","r") as nodosexcel:
	lines=nodosexcel.readlines()


cmts={}
x="nada"
for linea in lines:
	splitter=linea.split()
	if len(splitter)==13:
		nodo=splitter[12]
		number=int(splitter[2])
		if nodo==x:
			cmts[nodo]=cmts[nodo]+number
			x=nodo
		else:
			cmts[nodo]=number
			x=nodo
	else:
		pass

print(cmts)
print(type(cmts["59"]))

nombres={"59":"COROMOTO","68A":"TREBOL","52":"RICHMOND","57":"SAN FELIPE I","58":"SAN FELIPE II","18":"LA FUENTE",
"24":"VERITAS II","1B":"PARAISO B","26A":"CUMBRES DE MBO","36A":"PAZ A","36B":"PAZ B","81":"LA CIMA","16":"18 DE OCTUBRE",
"17A":"TIERRA NEGRA","39":"SANTA MARIA","31":"VICTORIA II","34":"LA FLORESTA","33":"ROSALEDA","19":"LAS MERCEDES",
"35B":"REY DE REYES","40":"NUEVA VÍA","22A":"EL MILAGRO","67B":"LAGUNITA B","67E":"LAGUNITA E","15":"PARAGUA II",
"23":"VERITAS I","64A":"PUERTO RICO","67C":"LAGUNITA C","72":"CUATRICENTENARIO","30":"VICTORIA I","48":"SABANETA III",
"74A":"LOS ALTOS","20":"VALLE FRÍO","73B":"LOS ALTOS IIIB","73A":"LOS ALTOS IIIA","1A":"PARAISO A","67A":"LAGUNITA A",
"14A":"PARAGUA I","29":"LAS TUNAS","67D":"LAGUNITA D","35":"SAN MIGUEL","28":"VALLE CLARO","21":"SANTA LUCIA",
"25":"AMPARO"}

ONOFF={True:"ON",False:"OFF"}
wb= Workbook()
wa= wb.active

for i,n in cmts.items():
	tof= n > 0
	indexar=[nombres[i],ONOFF[tof]]
	wa.append(indexar)
else:
	print("DONE!")

wb.save(r"C:\Users\Oscar\Desktop\excelss.xlsx")