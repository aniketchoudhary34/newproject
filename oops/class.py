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
#
#
#
#
#class student:
#    def __init__(self):
#            self.name=input("enter a number:")
#            self.rollno=int(input("enter a number:"))
#            self.percentage=float(input("enter a number:"))
#    def display(self):
#        print("name:",self.name)
#        print("rollno:",self.rollno)
#        print("percentage:",self.percentage)
#        
##c1=student()
##c1.display()        
#
#
#
#
#class circle:
#    def __init__(self,radius):
#          self.radius = radius
#    def perimeter(Self):                   
#        print()
#    def area(Self):
#        print(self.radius)
#obj=circle(8) 
#obj.area()
#obj.perimeter()       
#             


class stack:
    def __init__(self):
        self.items =[]
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        if not self.isempty():
            return self.isempty.pop()
        else:
            return "empty stack"
    def isempty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)    
    def peek(self):
        if not self.isempty():
            return self.items[-1]
        else:
            return "empty stack"
        
stk = stack()
stk.push(0)        
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)

print(stk.size())
print(stk.peek())

