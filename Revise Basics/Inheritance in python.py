# single level inheritance

class parentClass1:
    var="its from parent class"
    var1="parent class calling"

class childClass1(parentClass1):
    pass

parentobject=parentClass1()
print(parentobject.var)

childobject=childClass1()
print(childobject.var)


#overwriting

class childClass2(parentClass1):
    var="its from childClass2 overwritten on parentClass"

childobject1=childClass2()

print(childobject1.var)
print(childobject1.var1)

#multiple parent

class Dad:
    var1="hey son im your dad"

class Mom:
    var2="hey son im your mom"

class child(Dad,Mom):
    var3="I am child"

childobject2=child()
print(childobject2.var1)
print(childobject2.var2)
print(childobject2.var3)
