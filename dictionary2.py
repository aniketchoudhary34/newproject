


 
this_school = {"class9":[10,20,30,40,50]
     ,
    "class10":[44,55,67,45,85]
    ,
     "class11":[56,84,21,35,45]
     ,
      "class12":[65,84,24,36,45]
}
 
name =(input("enter a class name: "))
counter=0

if name in this_school.keys():  
                                                  
    i=0
    for i in  (this_school[name]):       
           counter+=1
           print("student",counter,name,i)
    for i in  range(len(this_school[name])):
            print("student ",i , " of ", name," scored ", this_school[name][i])
    else:
      print("no record")

    






















#if this_school == "class9" or this_school == "class10" or this_school == "class11" or this_school == "class12":
    

