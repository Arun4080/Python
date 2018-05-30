# simple exaple of class
class simpleClass:
    name='Arun'
    age='20'
    def seyHi(self):
        return("Hello everone")

simpleobject=simpleClass()
print("{x} myself {y} and i am {z} years old.".format(x=simpleobject.seyHi(), y=simpleobject.name, z=simpleobject.age))

# Lets addup some more features

class MyName:
    def createName(self,name):
        self.name=name
    def displayName(self):
        return self.name
    def saying(self):
        print("Hello %s" % self.name)

first=MyName()
first.createName("Arun")
print(first.displayName())
first.saying()
