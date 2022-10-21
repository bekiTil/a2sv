class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        n,m=len(matrix),len(matrix[0])
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        
        count,dxn=0,0
        row,col=0,0
        visited=set()
        while count < n*m:
            
            if 0<= row < n and 0<= col< m:
                ans.append(matrix[row][col])
                visited.add((row,col))
                count+=1
            di , dj = direction[dxn]
            row ,col=row+di, col + dj
            
            if (not (0<=row <n and 0<=col<m)) or (row,col) in visited:
                row-=di
                col-=dj
                
                dxn+=1
                dxn%=4
                di , dj = direction[dxn]
                row ,col=row+di, col + dj
        return ans
        
            