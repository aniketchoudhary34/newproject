#class person:
#    def __init__(self,name,age):
#        self.name=name
#        self.age=age
#c1=person("aniket",18)
#print(c1.name)
#print(c1.age)        
#
#
#
#class Person(object):
# 
#    # __init__ is known as the constructor
#    def __init__(self, name, idnumber):
#        self.name = name
#        self.idnumber = idnumber
# 
#    def display(self):
#        print(self.name)
#        print(self.idnumber)
#         
#    def details(self):
#        print("My name is {}".format(self.name))
#        print("IdNumber: {}".format(self.idnumber))
#     
## child class
#class Employee(Person):
#    def __init__(self, name, idnumber, salary, post):
#        self.salary = salary
#        self.post = post
# 
#        # invoking the __init__ of the parent class
#        Person.__init__(self, name, idnumber)
#         
#    def details(self):
#        print("My name is {}".format(self.name))
#        print("IdNumber: {}".format(self.idnumber))
#        print("Post: {}".format(self.post))
# 
# 
## creation of an object variable or an instance
#a = Employee('aniket', 886012, 200000, "Intern")
# 
## calling a function of the class Person using
## its instance
#a.display()
#a.details()
#
#
#class Bird:
#
#	def intro(self):
#		print("There are many types of birds.")
#
#	def flight(self):
#		print("Most of the birds can fly but some cannot.")
#
#class sparrow(Bird):
#
#	def flight(self):
#		print("Sparrows can fly.")
#
#class ostrich(Bird):
#
#	def flight(self):
#		print("Ostriches cannot fly.")
#
#obj_bird = Bird()
#obj_spr = sparrow()
#obj_ost = ostrich()
#
#obj_bird.intro()
#obj_bird.flight()
#
#obj_spr.intro()
#obj_spr.flight()
#
#obj_ost.intro()
#obj_ost.flight()




class student:
    def __init__(self):
            self.name=input("enter a number:")
            self.rollno=int(input("enter a number:"))
            self.percentage=float(input("enter a number:"))
    def display(self):
        print("name:",self.name)
        print("rollno:",self.rollno)
        print("percentage:",self.percentage)
c1=student()
c1.display()        
