#s="hello"
#h=len(s)
#l=[]
#for i in range (h,0,-1):
##     print(s[i])  
##
##
#s=["h","e","l","l","o"]
#i=len(s)
#m=[]
#while i>0:
#    i=i-1
#    m.append(s[i])
#    
#print(m)    
#




#
#arr = ["mint", "mini", "mineral"]
## The longest common prefix of an empty array is "".
#if not arr:
#  print("Longest common prefix:", "")
## The longest common prefix of an array containing 
## only one element is that element itself.
#elif len(arr) == 1:
#  print("Longest common prefix:", arr[0])
#else:
#  # Sort the array
#  arr.sort()
#  result = ""
#  # Compare the first and the last string character
#  # by character.
#  for i in range(len(arr[0])):
#      #  If the characters match, append the character to
#      #  the result.
#      if arr[0][i] == arr[-1][i]:
#          result += arr[0][i]
#      # Else, stop the comparison
#      else:
##          break
##  print("Longest common prefix:", result)
#
#
#
#
#
#
#def findMinLength(arr, n):
#
#    min = len(arr[0])
#
#    for i in range(1,n):
#        if (min > len(arr[i])):
#            min = len(arr[i])
#
#    return(min)
#
#def commonPrefix(arr, n):
#
#    minlen = findMinLength(arr, n)
#    result =""
#    for i in range(minlen):
#    
#        #Current stores the letter
#        # to be compared
#        current = arr[0][i]
#
#        for j in range(1,n):
#            if (arr[j][i] != current):
#                return result
#
#        # Append to result
#        result = result+current
#
#    return (result)
#
#    
#arr = ["Favtutor", "Favour", "Favourite", "Favonian"]
#n = len(arr)
## Find the LCP using a function
#ans = commonPrefix (arr, n)
## Print the LCP
#print("The longest common prefix is ",ans)




a=["flower","flow","fly"]
#a=["minute","min","minimum"]

s=a[0]
print(s)