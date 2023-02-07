class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        rot =[0,1]
        move=[0,0]
        dxn=[(-1,-1),(1,-1),(1,1),(-1,1)]
        index=0
        for i in instructions:
            if i=="R":
                
                rot[0]+=(-1*dxn[index-1][0])
                rot[1]+=(-1*dxn[index-1][1])
                
                if index-1<0:
                    index=3
                else:
                    index-=1
            elif i=="L":
                rot[0]+=dxn[index][0]
                rot[1]+=dxn[index][1]
                index+=1
                index%=4
            else:
                move[0]+=rot[0]
                move[1]+=rot[1]
              
                
       
        
        if  (move[0]==0 and move[1]==0) or not (rot[0]==0 and rot[1]==1):
            return True
        return False
            
        
        
      