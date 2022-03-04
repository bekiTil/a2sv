#time Complexity
#O(n^2)
#Space Complexity
#O(R) where R means rotten orange 
#link to question https://leetcode.com/problems/rotting-oranges/
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten=deque()
        visited=set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    rotten.append((i,j))
        
        
        time=-1
        while rotten:
            n=len(rotten)
            for i in range(n):
                x,y=rotten.popleft()
                visited.add((x,y))
                for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if 0<=i<len(grid) and 0<=j<len(grid[0]) and (i,j) not in visited:
                        if grid[i][j]==1:
                            grid[i][j]=2
                            rotten.append((i,j))
                            visited.add((i,j))
            time+=1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        new=0
        for i in grid:
            new+=sum(i)
        if new==0:
            return new
        return time
                
        
        
        
