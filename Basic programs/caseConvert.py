#a=str(input())
a="Hello World"
b=[]
for i in a:
	if i.isupper():
		i=i.lower()
	else:i=i.upper()
	b.append(i)

for i in b:
	print(i, end='')