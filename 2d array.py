

#row=int(input("enter a number row"))
#col=int(input("enter a number col"))
#matrix=[]
#for i in range(row):
#   a=[]
#   for j in range(col):
#      val=int(input("enter a number"))
#      a.append(val)
#   matrix.append(a)
#
#for i in range (row):
#    for j in range(col):
#      print(matrix[i][j],end=" ")
#    print()  
#


#x=int(input("enter a number row:"))
#y=int(input("enter a number col:"))
#mat=[]
#for i in range(0,x):
#   mat.append([])
#for i in range(0,x):
#   for j in range (0,col):
#      mat[i].append(j)
#      mat[i][j]=0


#digits = [1, 2, 5]
#n = len(digits) -1
#for i in range (n):
#
#      print(i)
#        
#      if i < 0:
#              print(digits)
#              digits = [1] + digits
#      else:
#              print(digits)
#              digits[n] = digits[n] + 1
#print(digits)
#
#


#=1235


#list_string = [1, 12, 15, 21, 131]
#   
#   
#list_int = []
## using iteration and sorted() 
#for i in list_string:
#    list_int.append(i)
#   
## printing output 
#
#

#cir_moon = 10921
#
#



#n = 1234
#digits = []
#while n>0:
#    digits.append(n%10)
#    n//=10
#    
#
#print(digits)
#
#
#
#


#divisible
num=54
div=6
if num%div ==0:
    print("yes")
else:
    print("no")    

#divisible
num=[12,13,45,54,60]
div=6
s=[]
for nums in num:   
   if nums%div == 0:
    s.append("yes")
   else:
    s.append("no")        
print(s)    


#multiple

num=13

if num%3 ==0:
    print("yes")
else:
    print("no")    


#special


st="geeks for ++*& geeks"
c = 0
for i in range (len(st)):
    
    if st[i] == "=" or st[i] == "+" or st[i] == "-" or st[i] == "*" or st[i] == "%" or st[i] == "&" or st[i] == "!" or st[i] == ":":
        c +=1
if c:
    print("special character is used")   
else:
    print("no special character")