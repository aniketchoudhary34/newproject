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

s
st="geeks for ++*& geeks"
c = 0
for i in range (len(st)):
    
    if st[i] == "=" or st[i] == "+" or st[i] == "-" or st[i] == "*" or st[i] == "%" or st[i] == "&" or st[i] == "!" or st[i] == ":":
        c +=1
if c:
    print("special character is used")   
else:
    print("no special character")