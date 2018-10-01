a="Hello There, my name is arun."
a=a.split(" ")
b=[]
for i in a[-1::-1]:
	b.append(i)
print(' '.join(b))