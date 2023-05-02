class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        maximum =deque([])
        temp =[y-x for x,y in points]
        print(temp)
        ans = float("-inf")
        for index in range(len(points)):
            x ,y  = points[index]
            
            while maximum and  x-points[maximum[0]][0]>k:
                maximum.popleft()
            if maximum:
                ans = max(temp[maximum[0]]+x+y,ans)
                
            while maximum and temp[maximum[-1]] <temp[index] :
                maximum.pop()
            maximum.append(index)
           
        return ans