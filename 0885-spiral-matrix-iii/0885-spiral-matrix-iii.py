class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dxn = [(0,1),(1,0),(0,-1),(-1,0)]
        row = rStart
        col = cStart
        result=[]
        count=0
        cur_count=0
        cur_len=2
        cur_dxn=0
        
        
        while count < rows * cols:
            # print(cur_count,(row,col),cur_dxn,cur_len)
            if 0<=row<rows and 0<=col<cols:
                count+=1
                result.append([row,col])
            cur_count+=1
            
            if cur_count==cur_len:
                if cur_dxn==1 or cur_dxn==3:
                    cur_len+=1
                cur_count=1
                cur_dxn+=1
                cur_dxn%=4
            di , dj =dxn[cur_dxn]
            row,col=row+di ,col+dj
        return result
        
                
            
           
                
                
        