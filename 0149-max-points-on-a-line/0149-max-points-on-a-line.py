class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        total=1
        for i in range(len(points)):
            
            count=defaultdict(int)
            x,y=points[i]
            for j in range(i+1,len(points)):
                n,m=points[j]
                if x-n==0:
                    count[float('inf')]+=1
                else:
              
                    
                    count[((m-y)/(n-x))]+=1
            maximum=float("-inf")
            
            for val in count:
                maximum=max(maximum,count[val])
            total=max(total,maximum+1)
            # print(count,total,maximum)
        return total
                
                