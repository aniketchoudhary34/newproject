#method overriding):
class A:
    def vsp(self):
        print("hieee")
class B(A):
    def vsp(self):
        print("hello")
    def xyz(self):
        print("back to end")            
obj=()
obj.vsp()

#method overloading :      but not support python 
class vip:
    def vsp(self,x=None,y=None):
        if x==None and y==None:
            print("hello this is python polymorphism")
            print("thanks for visit")
        elif x!=None and y !=None:
            f=1
            for i in range (1,(x+1)):
                f=f*1
                print(f)
        else:
            print("addition is : "(x+y))
obj=vip()

obj.vsp()
obj.vsp(5)
obj.vsp(56+44)




#operator overloading
class A:
    def xyz(self,x):
         self.x=x
o1=A(10)
print(o1.x)


