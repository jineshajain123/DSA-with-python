nums=[-3,4,-1,2,1,-5,4]
n = len(nums)
result=[0]*n
pos=0
neg=1
for i in range(0,n):
    if nums[i]>=0:
        result[pos]= nums[i]
        pos += 2
    else:
        result[neg]= nums[i]
        neg += 2
print(result)    