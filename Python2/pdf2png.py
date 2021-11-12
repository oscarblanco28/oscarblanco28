pizz={
	"Pizza pequeña":3.00,
	"Pizza mediana":4.00,
	"Pizza familiar":5.00
}
adic={
	"Borde de queso":0.5,
	"Peperonni":1.00,
	"Maíz":1.00,
	"Tocineta":1.00
}

def listaing(col=0,row=0,*args,**dicto):
	n=1
	void=[]
	y=dicto.values()
	match=re.search("\APizza",y[0])
	pizzas=[]
	if match:
		if len(pizzas) < 3:
		for tamano, precio in dicto.items():
			button=InlineKeyboardButton(text="{0} ----->{1}".format(tamano,precio))
			pizzas.append()
		return pizzas
		else:
			for ingrediente, valor in dicto.items():
				i="{0}.{1} ----->  {2}".format(n,ingrediente,valor)
				void.append(i)
				n=n+1
				mnsj="\n".join(void)
			return mnsj