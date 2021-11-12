import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime


URLL="http://172.30.31.17/cmts1/index.php"
payload={"port":"",
"status":""}

with requests.Session() as session:
	session.get(URLL)
	p=session.post(URLL,data=payload)
	f=p.text

def sopa():
	soup=BeautifulSoup(f,"html.parser")
	c=soup.pre.string

def escribir():
	with open(r"C:\Users\oblanco\Desktop\Python\VIGINET\nodos.txt","w") as nodofile:
		nodofile.write(c)
		print("archivo escrito con exito")

sopa()
escribir()

lines=[]
with open(r"C:\Users\oblanco\Desktop\Python\VIGINET\nodos.txt","r") as nodosexcel:
	lines=nodosexcel.readlines()

cuenta=0
for item in lines:
	print(f"{cuenta} {item}")
	cuenta= cuenta+1
else:
	print("Done!")
