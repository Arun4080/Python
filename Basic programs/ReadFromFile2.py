f=open("data/test.txt")
d=f.read()
d=d.split(" ")
a=len(max(d,key=len))
for i in d:
	if len(i)==a:
		print(i)
f.close()