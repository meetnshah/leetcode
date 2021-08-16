def revPair(nums):
    res = 0
    for i in range(len(nums)):
        i = nums[0]
        for j in range(len(nums)-1):
            if nums[i] > nums[j] * 2:
                res += 1
            i += 1
    return res

print(revPair([1,3,2,3,1]))
