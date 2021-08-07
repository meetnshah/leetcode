def threeSum(nums):
    
    nums=sorted(nums)
    res=[]
    
    for i in range(len(nums)-2):
        if(i==0 or i>0 and nums[i]!=nums[i-1]):
            left=i+1
            right=len(nums)-1
            total=0-nums[i]
            while(left<right):
                if(nums[left]+nums[right]==total):
                    res.append([nums[i],nums[left],nums[right]])
                    while(left<right and nums[left]==nums[left+1]):
                        left+=1
                    while(left<right and nums[right]==nums[right-1]):
                        right-=1
                    left+=1
                    right-=1
                elif (nums[left]+nums[right]>total):
                    right-=1
                else:
                    left+=1
    return res

print(threeSum([-1,0,1,2,-1,4]))
    