row=int(input("enter a row number: "))
col=int(input("enter a col number: "))
matrix=[]
for i in range(row):
    a=[]
    for j in range (col):
        val=int(input("enter a number: "))
        a.append(val)
    matrix.append(a)




l=[]

for i in range (row):
    for j in range (col):
        if i == 0 or j == 0 or i == row -1 or j == col -1:
        # print(matrix[i][j],end=" ")    
          l.append(matrix[i][j])

print(l)
