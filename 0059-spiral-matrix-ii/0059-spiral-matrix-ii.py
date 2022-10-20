class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans=[[0 for _ in range(n)] for _ in range(n)]
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        count,value,dxn=0,1,0
        row,col=0,0
        visited=set()
        while count < n*n:
            
            if 0<= row < n and 0<= col< n:
                ans[row][col]=value
                visited.add((row,col))
                value+=1
                count+=1
            di , dj = direction[dxn]
            row ,col=row+di, col + dj
            
            if (not (0<=row <n and 0<=col<n)) or (row,col) in visited:
                row-=di
                col-=dj
                
                dxn+=1
                dxn%=4
                di , dj = direction[dxn]
                row ,col=row+di, col + dj
        return ans
        
            