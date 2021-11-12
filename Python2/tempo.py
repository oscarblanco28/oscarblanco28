o=["orcal","jes","uno","lill"]
n=[2,1]
void=[]
copy=[]

for item in n:
	void.append(o[:item])
	copy.append(void)
	void.clear()
	del o[:item]

print(copy)
