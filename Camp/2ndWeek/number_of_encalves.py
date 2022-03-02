class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row=len(grid)
        column=len(grid[0])
        new=set()
        visited=[]
        num=0
        
        for i in range(len(grid)):
            if grid[i][0]==1:
                new.add((i,0))
                grid[i][0]=0
            if grid[i][len(grid[0])-1]==1:
                new.add((i,len(grid[0])-1))
                grid[i][len(grid[0])-1]=0
        for i in range(len(grid[0])):
            if grid[0][i]==1:
                new.add((0,i))
                grid[0][i]=0
            if grid[len(grid)-1][i]==1:
                new.add((len(grid)-1,i))
                grid[len(grid)-1][i]=0

        def dfs(arr,pair):
            x,y=pair
            for i,j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0<=i<row and 0<=j<column and (i,j) not in visited and arr[i][j]==1:
                    arr[i][j]=0
                    dfs(arr,(i,j))
        for i in new:
            dfs(grid,i)
        for i in grid:
            num+=sum(i)
        
        return num
                    
        
