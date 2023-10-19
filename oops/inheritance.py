#single inheritance
class A:
    def displayA(self):
        print("hello A")
class B:
    def displayB(self):
        print("hello B")
obj1=A()
obj2=B()
obj1.displayA()
obj2.displayB()



print("multilevel inheritance")

#Multilevel inheritance 
class a:
    def displayA(self):
        print("hello A")
class b(a):
    def displayB(self):
        print("hello B")        
class c(b):
    def displayC(self):
        print("hello C")
c1=c()
c1.displayA()
c1.displayB()
c1.displayC()
     

print("multiple inheritance ")
#multiple inheritance

class a:
    def displayA(self):
        print("hello A")
class b:
    def displayB(self):
        print("hello B")        
class c(a,b):
    def displayC(self):
        print("hello C")
c1=c()
c1.displayA()
c1.displayB()
c1.displayC()