# for loop

a=[1,2,3,4,"arun","verma"]

for i in range(0,6):
    print(i)

for i in a:
    print(i)

b=[1,2,[3,4],5,6]

# Iteration in nested list
for i in b:
    if isinstance(i,list):
        for j in i:
            print(j)
    else: print(i)

#or

print([i for i in range(6)])

print([i for i in a])


# While loop

count=0
while count < len(a):
    print(a[count])
    count= count+1

