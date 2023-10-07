class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        dxn_arr = [(0,1),(1,0),(-1,0),(0,-1)]
        
        def check(index_x,index_y):
            
            if 0<=index_x<len(grid) and 0<=index_y<len(grid[0]):
                return True
            return False
                
        visited = set()
        def dfs(space):
            x , y = space
            for i , j in dxn_arr:
                if check(x+i,y+j) and (x+i,y+j) not in visited and grid[x+i][y+j] == "1":
                    visited.add((x+i,y+j))
                    dfs((x+i,y+j))
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row,col) not in visited:
                    visited.add((row,col))
                    dfs((row,col))
                    ans+=1
        return ans