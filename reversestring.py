s=["p","y","t","h","o","n"]
j=len(s)
i=0
while i<j:
    j-=1
    print(s[i])
    temp=s[i]
    s[i]=s[j]
    s[j]=temp
    i+=1
print(s)    