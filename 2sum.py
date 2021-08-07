def twoSum(nums, target):
        # O(nlogn)
        # nums.sort()
        # begin = 0
        # end = len(nums) - 1
        # while begin<end:
        #     curSum = nums[begin] + nums[end]
        #     if curSum == target:
        #         return [begin, end]
        #     elif curSum < target:
        #         left += 1
        #     else:
        #         end -= 1
        # return []
        # //////////////////////////////////////////
        # O(n2)
        # for i in range(len(nums)-1):
        #     first = nums[i]
        #     for j in range(i+1, len(nums)):
        #         second = nums[j]
        #         if first + second == target:
        #             return[i,j]
        # return[]
        # //////////////////////////////////////////
        # O(n)
        dic = {}
        for i,match in enumerate(nums):
            if match in dic:
                return [dic[match], i]
            else:
                dic[target - match] = i
                
print(twoSum([2,7,11,15],9))