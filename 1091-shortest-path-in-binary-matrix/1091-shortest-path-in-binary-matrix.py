class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direction=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
        row=len(grid)
        column=len(grid[0])
        parents=[[(-1,-1) for j in range(column)]for i in range(row)]
        def validate(pos):
            if 0<=pos[0]<row and 0<=pos[1]<column:
                return True
            return False
        
        level=deque([])
        if grid[0][0]!=0:
            return -1
        level.append((0,0,1))
        visited=set()
        visited.add((0,0))
        while level:
          
            cur=level.popleft()
            if cur[0]==row-1 and cur[1]==column-1:
                return cur[2]
            for (i,j) in direction:
                if validate((cur[0]+i,cur[1]+j)) and grid[cur[0]+i][cur[1]+j]==0 and (cur[0]+i,cur[1]+j) not in visited:
                    parents[cur[0]+i][cur[1]+j]=(cur[0],cur[1])
                    visited.add((cur[0]+i,cur[1]+j))
                    level.append((cur[0]+i,cur[1]+j,cur[2]+1))
                    
            
        return -1