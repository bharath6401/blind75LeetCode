def twoSum(arr,k,i,j=0):
    
    if(i>=len(arr)-1):
        return
    
    
    for j in range(i+1,len(arr)):
        if(arr[i]+arr[j]==k):
            return([i,j])
        
    
    return(twoSum(arr,k,i+1,j=0))
    

output=twoSum(arr,k,i=0)
print(output)
