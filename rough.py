#s="hello"
#h=len(s)
#l=[]
#for i in range (h,0,-1):
##     print(s[i])  
##
##
#s=["h","e","l","l","o"]
#i=len(s)
#m=[]
#while i>0:
#    i=i-1
#    m.append(s[i])
#    
#print(m)    
#




#

#
#
#
#
#
#def findMinLength(arr, n):
#
#    min = len(arr[0])
#
#    for i in range(1,n):
#        if (min > len(arr[i])):
#            min = len(arr[i])
#
#    return(min)
#
#def commonPrefix(arr, n):
#
#    minlen = findMinLength(arr, n)
#    result =""
#    for i in range(minlen):
#    
#        #Current stores the letter
#        # to be compared
#        current = arr[0][i]
#
#        for j in range(1,n):
#            if (arr[j][i] != current):
#                return result
#
#        # Append to result
#        result = result+current
#
#    return (result)
#
#    
#arr = ["Favtutor", "Favour", "Favourite", "Favonian"]
#n = len(arr)
## Find the LCP using a function
#ans = commonPrefix (arr, n)
## Print the LCP
#print("The longest common prefix is ",ans)







#roman = {"i":1,"v":5,"x":10,"l":50,"c":100,"d":500,"m":1000}



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
    