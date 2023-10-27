#class abc:
#    def getvalue(self,x):
#        self.a=x
#    def fun(self):
#        print(self.a)
#
#obj=abc()
#obj.fun()            

class A:
    _a=10        #protected
    __b=20         #private
    c=100
    def show(self):
        print("a= ",self._a)
        print("b= ",self.__b)
        print("c= ",self.c)
obj=A()
obj.show()        
print(obj._a)
#print(obj.__b)


