#Constructor in python -- passing var along with object declaration

class new:
    def __init__(self,name):
        self.name1=name
        print("you are in constructor")

    def printName(self):
        print("hello %s" % self.name1)

a=new("arun")
a.printName()
