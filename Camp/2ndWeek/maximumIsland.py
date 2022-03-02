class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.width=len(grid[0])
        self.height=len(grid)
        new=[]
        visited=[]
        
        def dfs(total,grid,pair):
            x,y=pair
            for i,j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0<=i<self.height and 0<=j<self.width and 1==grid[i][j] and (i,j) not in visited:
                    total[0]+=1
                    visited.append((i,j))
                    dfs(total,grid,(i,j))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j]==1:
                    visited.append((i,j))
                    total=[1]
                    dfs(total,grid,(i,j))
                    new.append(total[0])
        if not new:
            return 0
        else:
            return max(new)
