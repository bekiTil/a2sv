#question link https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

#TimeComplexity O(nlogn)
#SpaceComplexity O(n)
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        num=[]
        for i in points:
            heapq.heappush(num,i)
        quantitiy=1
        
        start,end=heapq.heappop(num)
        while num:
            one,two=heappop(num)
            if one>end:
                quantitiy+=1
                end=two
            else:
                if end>two:
                    end=two
        return quantitiy
