from bs4 import BeautifulSoup
import codigo_html

soup=BeautifulSoup(codigo_html.html_doc2,"html.parser")

#p=soup.prettify()
#print(p)
c=soup.pre
print(c.string)
lista=c.string.splitlines()
print(lista)
print(len(lista))
#print(soup.div.name)
#print(soup.img["src"])
#print("fin")