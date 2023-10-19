#class person:
#    def __init__(self,name,age):
#        self.name=name
#        self.age=age
#obj1=person("aniket",21)
#print(obj1.name)
#print(obj1.age)
#
#
#
#class student:
#    def __init__(self):
#        self.name=input("enter a name: ")
#        self.rollno=int(input("enter a rollno: "))
#        self.percentage=float(input("enter a percentage: "))
#    def display(self):
#        print("name:",self.name) 
#        print("rollno:",self.rollno)
#        print("percentage:",self.percentage)   
#c1=student()
#c1.display()        
#
#
##
#
#class apple:
#    def mobile(self):
#        print("  all phone list ")
#    def iphone(self):
#        print("iphone 15")
#class android:
#    def android(self):
#        print("mi,oppo,vivo,oneplus")     
#class anyphone:
#    def anyphone(self):
#        print("no any phone ")  
#
#obj1=apple()
#obj2=android()
#obj3=anyphone()
#
#obj1.mobile()
#obj1.iphone()
#
#obj1.mobile()



class a:
    def displayA(self):
        print("welcome to wscubetech A")
class b(a):
    def displayB(Self):
        print("welcome to wscubetech B")
class c(b):
    def displayC(self):
        print("welcome to wscubetec C")        
obj=c()
obj.displayA()
obj.displayB()
obj.displayC()