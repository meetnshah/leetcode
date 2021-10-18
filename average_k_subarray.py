# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# def bruteForce(arr,k):
#     res =[]
#     for i in range(len(arr)-k+1):
#         sum = 0
#         for j in range(i,i+k):
#             sum += arr[j]
#         res.append(sum/k)
            
#     return res


#Sliding Window:
def slidingWindow(arr,k):
    res = []
    windowSum, windowStart = 0.0,0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k-1:
            res.append(windowSum/k)
            windowSum -= arr[windowStart]
            windowStart += 1
    return res

print(slidingWindow([1,3,2,6,-1,4,1,8,2],5))