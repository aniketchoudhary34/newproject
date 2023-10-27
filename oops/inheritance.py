# #single inheritance
#class A:
#     def displayA(self):
#         print("hello A")
#class B:
#     def displayB(self):
#         print("hello B")
#obj1=A()
#obj2=B()
#obj1.displayA()
#obj2.displayB()
#print("multilevel inheritance")
# #Multilevel inheritance 
#class a:
#     def displayA(self):
#         print("hello A")
#class b(a):
#     def displayB(self):
#         print("hello B")        
#class c(b):
#     def displayC(self):
#         print("hello C")
#c1=c()
#c1.displayA()
#c1.displayB()
#c1.displayC()
#    
#print("multiple inheritance ")
# #multiple inheritance
#class a:
#     def displayA(self):
#         print("hello A")
#class b:
#     def displayB(self):
#         print("hello B")        
#class c(a,b):
#     def displayC(self):
#         print("hello C")
#c1=c()
#c1.displayA()
#c1.displayB()
#c1.displayC()
#
#
#class A():
#    _a = 1
#
#class B():
#    b = 1
#
##print(B.b)
##print(A._a)
#
#
#class circle:
#    def __init__(self):
#        self.radius=int(input("enter a radius:"))
#    def perimeter(self):
#        print("perimeter:",2*3.14*self.radius)
#    def area(self):
#        print("area:",3.14*self.radius**2)
#obj=circle() 
#obj.perimeter() 
#obj.area()      
#
#class calculator:
#    def add(self,x,y):
#        print("addition",x+y)
#    def sub(self,x,y):
#        print("substraction",x-y)
#    def mul(self,x,y):
#        print("multiple",x*y)    
#    def div(self,x,y):
#        print("divide",x/y)    
# 
#obj1=calculator() 
#obj1.add(2,3)  
#obj1.sub(25,20)
##obj1.mul(5,4)
##obj1.div(20,10)
##
##
#class person:
#    def __init__(self):
#        self.name=input("enter your name: ")
#        self.age=int(input("enter a age: "))
#        self.country=input("enter a country:")
#        self.dob=(input("enter a date of birth: "))
#
#
#    def display(self):
#        print("name:",self.name)
#        print("age:",self.age)
#        print("country:",self.country)
#        print("dob:",self.dob)    
#
#obj=person()        
#obj.display()
#




class shape():
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass



class circle:
    def __init__(self):
        self.radius=int(input("enter a radius:"))
    def calculate_perimeter(self):
        print("perimeter:",2*3.14*self.radius)
    def calculate_area(self):
        print("area:",3.14*self.radius**2)
obj=circle() 
obj.calculate_perimeter() 
obj.calculate_area()      
class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self):
        print(self.length * self.width)

    def calculate_perimeter(self):
        print(2 * (self.length + self.width))

obj4=Rectangle(24,5)
obj4.calculate_area()
obj4.calculate_perimeter()
class triangle():
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def calculate_area(self):
        print( 0.5 * self.base * self.height)

    def calculate_perimeter(self):
        print(self.side1 + self.side2 + self.side3)

obj5=triangle(5,4,7,8,7)
obj5.calculate_area()
obj5.calculate_perimeter()