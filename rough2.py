class hello:
    def star(self):
        m=int(input("enter a number:"))

        if(m>=80):
          print("A grade")
        elif(m>=60):
           print(" B grade")
        elif(m>=40):
          print(" C grade")
        else:
           print("Failed ")
obj1=hello()           
obj1.star()




class hello:
    def __init__(self,radius):
        self.radius=radius
    def perameter(self):
        print(self.radius*2)    