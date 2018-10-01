n=int(input())


#fabinaci series

n2=100

first=1

second=1

b=[1,1]

for i in range(n2):

    sum=first+second

    b.append(sum)

    
first=second

    second=sum

#print(b)



#Prime numbers

n1=545
c=[2]

for i in range(3,n1):

    t=0

    for j in range(2,i-1):

        if i%j==0:

            t=1

    if t==0:
        
    c.append(i)

#print(c)



#combine both series

a=[]

for i in range(n):

    a.append(b[i])

    a.append(c[i])

print(a[n])