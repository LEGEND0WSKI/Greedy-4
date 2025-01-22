# Time:O(n); traversal to find target; 2nd to find min rotations
# Space:O(1) for hashset
# Leetcode: Yes
# Issues:None

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        hmap = {}
        target = -1

        for i in range(len(tops)):
            if tops[i] not in hmap:
                hmap[tops[i]] = 1
            hmap[tops[i]] += 1

            if hmap[tops[i]] == len(tops):          # case [1,1,1,1] and [1,1,1,1]
                target = tops[i]
                break 

            if bottoms[i] not in hmap:
                hmap[bottoms[i]] = 1
            hmap[bottoms[i]] +=1

            if hmap[bottoms[i]] == len(tops):
                target = bottoms[i]
                break 
        
        topR = botR = 0                             # rotate min value

        for i in range(len(tops)):
            if tops[i] != target and bottoms[i] != target:      # faulty
                return -1
            if tops[i] != target:
                topR +=1
            if bottoms[i] != target:
                botR += 1

        return min(topR,botR)

        