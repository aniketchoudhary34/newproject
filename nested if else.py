
#age = 15
#
#if age >= 60:
#    print("You are a senior citizen.")
#else:
#    if age >= 18:
#        print("You are an adult.")
#    else:
#        print("You are a teenager.")



#age =20
#own_car= "true"
#if (age >=18):
#    if (own_car == "true"):
#        print('drive your car')
#    else:
#        print("work hard & purchase a new car")        
#else:#
#    print("not eligible")        



username = input("enter your name: ")
password = input("enter your password: ")
if username == "admin":
    if password == "password":
        print ("login successful welcome, admin")
    elif password == "12345":
        print("weak password.please reset your passwod")
    else:
        print("please incorrect your password")
else:
    if username == "guest": 
        if password == "guest":
         print("login successful welcome, guest")
        else:
            print("incorrect password, please try again")
    else:
        print("unknow user ,please try again")         


