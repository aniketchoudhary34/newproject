
#n=1
# 
#while n<10: 
#   
#    print(n)
#     
#    n=n+1
#



n=4

for i in range (n):
    
    for j in range (n):
        if i == 0 or i == 3  or j == n-1 or i == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")    

    print()        
