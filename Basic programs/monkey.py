n=int(input("enter no of stairs"))
a, t, d=0, 5, 2
for _ in range(n):
   if n<t or n==t:
       a=a+1
       print("no. of jumps are "+str(a))
       break
   n=(n-t)+d
   a=a+2
    
