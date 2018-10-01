a="arun verma"
a=a.split(" ")
for i in a:
	i=list(i)
	for j in range(0,len(i)-1,2):
		i[j],i[j+1]=i[j+1],i[j]
	print(''.join(i), end=" ")