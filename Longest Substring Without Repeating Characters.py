def longestSubstring(s,k):
    windowStart = 0
    count = {}
    maxLen = 0
    for windowEnd in range(len(s)):
        rightIdx = s[windowEnd] #right pointer will be start of string for now
        if rightIdx not in count: #if alphabet is not in dictionary
            count[rightIdx]= 0 # it will insert it
        count[rightIdx]+=1 # and increment if already there
        while len(count)>k: # while length of dictionary is greater than k 
            leftIdx = s[windowStart] # alphabet string of 1st element
            count[leftIdx] -=1 #decrements the first letter and if it is zero it will delete it
            if count[leftIdx] == 0:
                del count[leftIdx]
            windowStart += 1 # shrink the window
        maxLen = max(maxLen, windowEnd-windowStart+1)
    return maxLen
print(longestSubstring('araaci',2))