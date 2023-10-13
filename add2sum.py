nums=[2,3,7,11,15,9,6,8]
target=3

for i in range (len(nums)):
    if nums[i] == target:
        print(i)

a=0
flag = False
for i in range (len(nums)):
            if nums[i] >= target:
                a=i
                flag = True
                break
            print (a if flag else len(nums) )        



