def countmaxones(nums):
    i=0
    n=len(nums)
    cur_len,max_len=0,0
    for i in range(len(nums)):
        if nums[i] == 1:
            cur_len += 1
        else:
            cur_len = 0
        max_len = max(max_len,cur_len)
    return max_len

# print(countmaxones([1,0,1,1,1,1,0,1,1]))
print(countmaxones([0,1,1,0,1,0]))