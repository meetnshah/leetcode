# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order. 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

def squareSorted(array):
#     sortedSquares = [0 for _ in array]

#     for idx in range(len(array)):
#         value = array[idx]
#         sortedSquares[idx] = value * value
        
#     sortedSquares.sort()
#     return sortedSquares
    output = [0 for _ in array]
    left = 0
    right = len(array)-1
    for i in reversed(range(len(array))):
        leftVal = array[left]
        rightVal = array[right]
        
        if abs(leftVal) < abs(rightVal):
            output[i] = rightVal * rightVal
            right -= 1
        else:
            output[i] = leftVal * leftVal
            left += 1
    return output
			

print(squareSorted([-4,-1,0,3,10]))
