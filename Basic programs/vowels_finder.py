a="satu is chu***a"
a=a.split(" ")
y=[]
for i in a:
	if i[0] in 'aeiouAEIOU':
		i=i[-1]+i[0]
		y.append(i)
	else:
		i=i+'ay'
		y.append(i)
print(y)
