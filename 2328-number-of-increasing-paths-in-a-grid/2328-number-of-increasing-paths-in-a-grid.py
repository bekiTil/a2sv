class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        graph=defaultdict(list)
        back=defaultdict(list)
        count=defaultdict(int)
        dp=defaultdict(int)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                for x,y in [(-1,0),(1,0),(0,1),(0,-1)]:
                    n=i+x
                    m=j+y
                    if 0<=n<len(grid) and 0<=m<len(grid[0]) and grid[i][j]<grid[n][m]:
                        graph[(i,j)].append((n,m))
                        count[(n,m)]+=1
                        
        level=deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if count[(i,j)]==0:
                    level.append((i,j))
                dp[(i,j)]+=1
        ans=0
        while level:
            node=level.popleft()
            for val in graph[node]:
                count[val]-=1
                if count[val]==0:
                    level.append(val)
                dp[val]+=dp[node]
                dp[val]%=(1000000007)
            ans+=dp[node]
            ans%=1000000007  
      
      
        return ans
                
            