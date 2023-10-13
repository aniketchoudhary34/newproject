num=8
a=0
b=1
i=0
for i in range (num):
    if i == 0:
     print (0)
    elif i == 1:
       print (1)
    else:
         ans=a+b
         a=b
         b=ans
         print(ans)
    i=i+1