num = int(input("How many terms? "))
n=[0,1]
[n.append(n[i-1]+n[i-2]) for i in range(2,num)]
print(n)

'''
#from 0 to num
x,y=0,1
while y<num:
  print(y)
  x,y=y,x+y

or
# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
'''