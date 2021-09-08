def container(height):
    
        maxArea = 0
        left = 0
        right = len(height) - 1
        while left<right:

            length = min(height[left],height[right])
            width = right - left
            area = length * width
            maxArea = max(maxArea,area)
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
    
    # Brute Force
    
    # maxArea = 0
    # left = 0
    # right = left + 1
    
    # if len(height) < 1:
    #     return None
    # for left in range(len(height)):
    #     for right in range(len(height)):
    #         length = min(height[left],height[right])
    #         width = right - left
    #         area = length * width
    #         maxArea = max(maxArea,area)
    #     return maxArea

# print(container([4,1,3,2,4]))

print(container([7,1,2,3,9]))