# Time:O(m*n); traversal
# Space:O(n) for hashset
# Leetcode: Yes
# Issues:None


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        count = 0
        hset = set()
        
        s = 0
        t = 0

        for i in source:
            hset.add(i)

        count = 0
        while t < len(target):

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

            

