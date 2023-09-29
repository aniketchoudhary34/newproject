

row=int(input("enter a number row"))
col=int(input("enter a number col"))
matrix=[]
for i in range(row):
   a=[]
   for j in range(col):
      val=int(input("enter a number"))
      a.append(val)
   matrix.append(a)

for i in range (row):
    for j in range(col):
      print(matrix[i][j],end=" ")
    print()  




#x=int(input("enter a number row:"))
#y=int(input("enter a number col:"))
#mat=[]
#for i in range(0,x):
#   mat.append([])
#for i in range(0,x):
#   for j in range (0,col):
#      mat[i].append(j)
#      mat[i][j]=0




