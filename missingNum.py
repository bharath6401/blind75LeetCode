
# input: nums=[1,0,3] 
# output: 2  #2 is missing in the range of 0,4


missingNum=sum(range(len(nums)+1))-sum(nums)
print(missingNum)
