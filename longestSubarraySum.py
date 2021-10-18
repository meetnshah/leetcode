# Problem Statement#
# Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

# Example 1:

# Input: [2, 1, 5, 2, 3, 2], S=7 
# Output: 2
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
# Example 2:

# Input: [2, 1, 5, 2, 8], S=7 
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
# Example 3:

# Input: [3, 4, 1, 1, 6], S=8 
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] 
# or [1, 1, 6].
# Try it yourself#

import math
def slidingWindow(arr,s):
    windowStart,windowSum = 0 ,0 #initializing start pointer and Sum
    min_len = math.inf
    for windowEnd in range(len(arr)): #iterating thru the array
        windowSum += arr[windowEnd] # Sum of all elements until the next condition
        while windowSum>=s:
            min_len = min(min_len, windowEnd-windowStart+1) # minimum len and windowEnd(3 in this case) - windowStart (0 in this case) +1(since index would be equal to 0)
            windowSum -= arr[windowStart] #sliding window removing first element
            windowStart += 1 #incrementing the element to add the next index
    if min_len == math.inf:
        return 0
    return min_len 
        

print(slidingWindow([3,4,1,1,6],8))
    