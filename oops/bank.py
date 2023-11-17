num=[1,2,3,0,5,-2]
target=5
m=[]
for i in range (len(num)):
      
    for j in (num):
        s=num[i]+num[j]
        if s == target:
           l=[num[i],num[j]]
           m.append(l)
                     
print(m)