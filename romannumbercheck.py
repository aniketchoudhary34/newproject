roman= {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
 
# name =(input("enter a class name: ").upper())
# print(type(name))
# l = ["i","ii","vi","xl","lxxxiii"]
# for name in l:





name = input("enter a roman number: ").upper()         # input 
num=0                        #count
i=0                         
while i < len(name):    #loop
    
    l=roman[name[i]]       #value print store
    
    r=roman[name[i+1]] if i+1 < len(name) else 0      #plus on value
                           
    temp = 0                           #temperary store 
    
    if l < r:                    #condition check on l less then r temp  store
        temp = r-l
        i+=1
        temp
    else:                       
        
        temp = l
    num+=temp
    i+=1
        
print(num)    
    