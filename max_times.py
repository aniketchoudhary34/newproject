a=[1,1,2,3,3,4,3,4,6,6,4,4,3,2,3,4,4,3,2,1,6,6,6,4]
n=len(a)
s={}

for i in range(n):
    count = 0
    for j in range (n):
      if a[i] == a[j]:
        count+=1
    s[a[i]] = count



m = 0
num = 0

for k,v in s.items():
    if v>m:
        m = v
        num = k

print(num,":", m)