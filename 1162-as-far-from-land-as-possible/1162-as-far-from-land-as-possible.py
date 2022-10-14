class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        level=deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    level.append((i,j,0))
        visited=set()
        ans=-1
        while level:
            for _ in range(len(level)):
                x,y,dist=level.popleft()
                for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
                    k=x+i
                    m=y+j
                    if 0<=k<len(grid) and 0<=m<len(grid[0]) and (k,m) not in visited and grid[k][m]==0:
                        new=(abs(k-x)+abs(m-y))+dist
                        ans=max(new,ans)
                        visited.add((k,m))
                        level.append((k,m,new))
        #     print(level)
        # print(ans)
        return ans
                        
                    