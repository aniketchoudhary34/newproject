standard =["A", "34", "46", "B", "D", "98", "57", "78", "F", "E","34","44"]


grade=[]
i=0         

for i in standard:
    if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == "F":
      grade.append(i)
    
    else:
      number = int(i)
      if number>85:
        grade.append("A")
      elif number>70:
        grade.append("B")
      elif number>55:
        grade.append("C")   
      elif number>40:
        grade.append("D")
      elif number>30:
        grade.append("E")
      else:
        grade.append("F")   
print(grade)
    




