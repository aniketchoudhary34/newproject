#remove element

arr=[1,2,4,5,4,3,4,1,2,4,5]
#set_1=set(arr)
#print(set_1)
#



#



def plusOne(digits):
    n = len(digits) - 1
    while digits[n] == 9:
        
        digits[n] = 0
        n = n - 1
        
    if n < 0:
        print(digits)
        #digits = [1] + digits
    else:
        
        digits[n] = digits[n] + 1
    return digits

digits = [1, 2, 5, 0]
print(plusOne(digits))
