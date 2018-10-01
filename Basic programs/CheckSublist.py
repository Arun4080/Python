
def isSublist(A, X):
  return ''.join(map(str, X)) in ''.join(map(str, A))

a=[1,2,3,4,5,6]
b=[4,6]
c=[1,2,3]
print(isSublist(a,b))
print(isSublist(a,c))
