def longestMountain(array):
        longestPeak = 0
        i = 1
        end = len(array) - 1
        
        while i < end:
            isPeak = array[i-1] < array[i] and array[i] > array[i+1]
            
            if not isPeak:
                i += 1
                continue
            
            leftIdx = i - 2
            while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
                leftIdx -= 1
                
            rightIdx = i + 2
            
            while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
                rightIdx += 1
                
            currentPeak = rightIdx - leftIdx - 1
            longestPeak = max(currentPeak, longestPeak)
            i = rightIdx
        return longestPeak

print(longestMountain([2,1,4,7,3,2,5]))
