import os
from PIL import Image

base=r'C:\Users\Oscar\Desktop\Revision medica'
imagenes = os.listdir(base)

forbidden=["Operacion_Oscar_Blanco.pdf", 'Mediphone.jpg']
for item in forbidden:
	if item in imagenes:
		imagenes.remove(item)

directorio=[]

for i in imagenes:
	nombre=base + '\\'+ i
	directorio.append(nombre)

ld=[]
for item in directorio:
	n=0
	pre=Image.open(item)
	impro=pre.convert('RGB')
	ld.append(impro)

uinput= input("Deseas hacer un pdf por imagen o todos juntos?")
if uinput == "uno":
	for rgb in ld:
		print("imagen actual es %s" %rgb)
		inputus=input('Ponle nombre al pdf: ')
		pdfname=base + '\\'+ inputus
		rgb.save(pdfname)
else:
	inputus=input('Ponle nombre al pdf: ')
	pdfname=base + '\\'+ inputus
	ld[0].save(pdfname,save_all= True, append_images=ld[1:])

html_doc="""<html><head><title> Prueba de bs4 </title></head>>
<body><a href="www.oscar.com/pic1.jpeg" id="link1" class="link"> Primer link </a>
<a href="www.oscar.com/pic2.jpeg" id="link2" class="link"> Segundo link </a>
<a href="www.oscar.com/pic3.jpeg" id="link3" class="link"> Tercero link </a>
</body>
</html>"""