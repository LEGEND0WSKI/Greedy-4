# Time:O(m*n); traversal
# Space:O(n) for hashset
# Leetcode: Yes
# Issues:None

# greedy 22ms
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        count = 0
        hset = set()
        
        s = 0
        t = 0

        for i in source:
            hset.add(i)

        count = 0
        while t < len(target):          # tchar and shar were giving time limit exceeded

            if target[t] not in hset:                   # unique letter not in source
                return -1

            if source[s] == target[t]:                  # search
                t+=1
            s+=1
            
            if t == len(target):                        # end of target
                return count+1
                
            if s == len(source):                        # reset 
                s = 0
                count +=1
                    
        return -1

# binary search 3ms     T:O(nlogn) and S:O(n)    
from collections import defaultdict
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        hmap = defaultdict(list)

        for i in range(len(source)):           # create a hashmap of letter: [indexes]
            hmap[source[i]].append(i)
        # print(hmap)
        
        i = 0
        j = 0
        count = 1
    
        while j < len(target):

            if target[j] not in hmap:
                return -1

            li = hmap[target[j]]                # fetch list from hmap
            idx = self.binarySearch(li,i)       # identify index in list
            
            if idx == len(li):                  # if index exceeds list size reset
                count +=1                       
                i = 0
            else:
                i = li[idx] + 1                 #  increment i and j
                j += 1

        return count

    def binarySearch(self,li, target):
        low = 0
        high = len(li)-1

        while low <= high:
            mid = low + (high-low)//2
            if li[mid] == target:
                return mid
            elif li[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return low



