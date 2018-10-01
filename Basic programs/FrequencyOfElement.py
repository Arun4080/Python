import collections as cl
a=[10,10,10,10,3,3,3,3,3,3,3,5,5,5,5,7,7,7,8,8]

num=cl.Counter(a)
print(num)

''' or
a=[10,10,10,10,3,3,3,3,3,3,3,5,5,5,5,7,7,7,8,8]
num={}
for i in set(a):
	num[i]=0
for i in a:
	num[i]=num[i]+1
print(num)
'''