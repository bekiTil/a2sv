class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        
        arr = []
        
        
        for i,j in intervals:
            
            if arr and arr[-1][-1]>=i:
                arr[-1][-1] = max(arr[-1][-1],j)
            else:
                arr.append([i,j])
        return arr