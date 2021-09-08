def rainWater(height):
    
    # 2 loop pointers
    # maxSeenLeft = 0
    # maxSeenRight = 0
    # left = 0
    # right = len(height) - 1
    
    # for left in range(len(height)):
    #     if height[left] < height[left+1]:
    #         maxSeenLeft = height[left]
    #     left += 1
    # for right in range(len(height)):
    #     if height[right] < height[right - 1]:
    #         maxSeenRight = height[right]
    #     right -= 1
    # maxSeenLeft = max(height[left],maxSeenLeft)
    # maxSeenRight = max(height[left],maxSeenRight)
    # walls = min(height[maxSeenLeft],height[maxSeenRight])
    # totalArea = walls - height[left]
    # return totalArea
    
    maxSeenLeft = 0
    maxSeenRight = 0
    totalWater = 0
    left = 0
    right = len(height) - 1
    while left<right:
        if height[left]<=height[right]:
            if height[left] >=maxSeenLeft:
                maxSeenLeft = height[left]
            else:
                totalWater += maxSeenLeft - height[left]
            left += 1
        else:
            if height[right] >= maxSeenRight:
                maxSeenRight = height[right]
            else:
                totalWater += maxSeenRight - height[right]
            right -= 1
    return totalWater
    
    # Brute Force
    # totalWater = 0
    # p = 0
    # for p in range(len(height)):
    #     left = p
    #     right = p
    #     maxLeft = 0
    #     maxRight = 0
    #     while left>=0:
    #         maxLeft = max(height[left],maxLeft)
    #         left -= 1
    #     while right<len(height):
    #         maxRight = max(height[right],maxRight)
    #         right += 1
    #     currentWater = min(maxRight,maxLeft) - height[p]
    
    #     if currentWater >= 0:
    #         totalWater += currentWater
    # return totalWater    
    
print(rainWater([0,1,0,2,1,0,3,1,0,1,2]))
