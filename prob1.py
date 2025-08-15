nums= [6,4,7,9,1,5]
small=nums[0]
for i in range (len(nums)):
    if nums[i]<small:
        small=nums[i]

print(small)