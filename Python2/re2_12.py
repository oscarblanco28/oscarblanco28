import re

lista=["azul y rosa","azul","azul&rosa"]

#rtest=re.compile("[0-9]+")
#newlist=list(filter(rtest.match,lista))

for i in lista:
	if ["azul","rosa"] in i:
		print(i)
	else:
		print("0")

