# a=["flower","flow"]
# n=len(a)
# s=[]

# for i in range(n):
#     print(a[i])
#     for j in range (n):
#       print(a[j])
    
#a=["flower","flow","fly"]
#a=["minute","min","minimum"]
#n=len(a)
#s=a[0]
##
#
#for i in range(1,n):
#    #print(i)
#    if len(s) >0:
#        string = a[i]
#        temp = ""
#        for j in range(len(string)):
#            if j < len(s) and s[j] == string[j]:
#                temp+=s[j]
#            else:
#                break
#        s=temp
#    else:
#        break
#if s:
#    print("Common prefix is ", s)
#else:
#    print("No common prefix")





user = input('enter a letter')
d = {'a': 1, 'b': 2, 'c':3}
for i in user:
    print(d[i])