import requests
from bs4 import BeautifulSoup
import time

postloginURL="http://nas.net-uno.net/nas2/htdocs/redirect.php"
getURL="http://nas.net-uno.net//nas2/htdocs/ftth_mbo/ftth_con_ont.php"
ajaxx="http://nas.net-uno.net//nas2/htdocs/ftth_mbo/ajax/ftth_con_ont.php"

payload={"login": "operatormbo",
"password": "123456"}
nodo={"aa_afunc": "call",
"aa_sfunc":"ajax_handler",
"aa_cfunc":"_callback",
"aa_sfunc_args":"BUSCAR",
"aa_sfunc_args":"1,1,,,,,MBOHED00106A,,"}

head={"Accept": "*/*",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "es-ES,es;q=0.9.",
"Connection": "keep-alive",
"Content-Length": "116",
"Content-type": "application/x-www-form-urlencoded",
"Cookie": "PHPSESSID=fa72ick6u02r9iaeve0dticfl1",
"Host": "nas.net-uno.net",
"Origin":"http://nas.net-uno.net",
"Referer": "http://nas.net-uno.net//nas2/htdocs/ftth_mbo/ftth_con_ont.php",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
"X-KL-Ajax-Request": "Ajax_Request"}

with requests.Session() as session:
	loginn=session.post(postloginURL,data=payload)
	print(loginn.status_code)
	print(loginn.encoding)
	print(loginn.headers)
	pconsultaONT=session.get(getURL)
	print(pconsultaONT.status_code)
	nodoconsulta=session.post(ajaxx,data=nodo)
	print(nodoconsulta.status_code)
	time.sleep(10)
	print(nodoconsulta.text)
	#post=session.post("http://nas.net-uno.net//nas2/htdocs/ftth_mbo/ajax/ftth_con_ont.php",data=nodo,headers=head)
	#print(post.status_code)
	#print(post.text)

