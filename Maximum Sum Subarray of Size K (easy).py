# Problem Statement#
# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

# Example 1:

# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
# Example 2:

# Input: [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].


# BruteForce

# def bruteForce(arr,k):
#     maxSum =0
#     for i in range(len(arr)-k+1):
#         summ =0 
#         for j in range(i, i+k):
#             summ += arr[j]
#             maxSum = max(maxSum, summ)
#     return maxSum

def slidingWindow(arr,k):
    windowStart, windowSum, maxSum = 0,0,0
    for i in range(len(arr)):
        windowSum += arr[i]
        if i>=k-1:
            maxSum = max(windowSum,maxSum)
            windowSum -= arr[windowStart]
            windowStart += 1
    return maxSum


print("Maximum sum of a subarray of size K: " + str(slidingWindow([2, 1, 5, 1, 3, 2],3)))
print("Maximum sum of a subarray of size K: " + str(slidingWindow([2, 3, 4, 1, 5],2)))

