a="python 3.2"
#a=list(a)
n={"letter":0,"numbers":0}
for i in a:
	if i.isdigit():
		n['numbers']+=1
	elif i.isalpha():
		n["letter"]+=1
	else:
		pass
print(n)