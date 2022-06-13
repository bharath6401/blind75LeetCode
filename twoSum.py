# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

arr=[2,7,11,2]
arrIndexDic={}
k=4
newDic={}
output=-1
for index in range(len(arr)):
    target=k-arr[index]
    if(arr[index] in newDic.keys()):
        print([newDic[arr[index]],index])
    else:
        newDic[k-arr[index]]=index


# recursive method

def twoSum(arr,k,i,j=0):
    
    if(i>=len(arr)-1):
        return
    
    
    for j in range(i+1,len(arr)):
        if(arr[i]+arr[j]==k):
            return([i,j])
        
    
    return(twoSum(arr,k,i+1,j=0))
    

output=twoSum(arr,k,i=0)
print(output)
