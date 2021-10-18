def fruitsIntoBasket(arr):
    windowStart = 0
    count = {}
    maxCount = 0
    
    for windowEnd in range(len(arr)): # get count of all occurrences of an element in the dictionairy
        rightIdx = arr[windowEnd] 
        if rightIdx not in count:
            count[rightIdx] = 0
        count[rightIdx] += 1
        
        while len(count)>2: #   shrink the sliding window, until we are left with '2' fruits in the fruit frequency dictionary
            leftIdx = arr[windowStart]
            count[leftIdx] -=1
            if  count[leftIdx] == 0:
                del count[leftIdx]
            windowStart+=1
            
        maxCount = max(maxCount, windowEnd-windowStart+1)
    return maxCount


print(fruitsIntoBasket([3,3,3,1,2,1,1,2,3,3,4]))