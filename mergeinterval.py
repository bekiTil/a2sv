class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        new=[]
        for interval in intervals:
            if not new :
                new.append(interval)
            elif  interval[0]> new[-1][-1]:
                new.append(interval)
                
            else:
                new[-1][-1]=max(new[-1][-1], interval[-1])
                
        return new
                
