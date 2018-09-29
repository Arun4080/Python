a=[int(input("Enter value of "+str(i+1)+" side: ")) for i in range(3)]
a.sort()
if a[0]<1 or a[-1]>=sum(a[0:-1]):
	print("This is not a Traingle")
else:print("This is a traingle")