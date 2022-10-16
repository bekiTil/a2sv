class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        find=None
        for i in range(2):
            for j in range(3):
                if board[i][j]==0:
                    find=(i,j)
                    break
            if find:
                break
                    
        level=deque([(board,find[0],find[1])])
        check=[]
        h=0
        for i in range(2):
            check.append([])
            for j in range(3):
                h+=1
                check[-1].append(h)
        def checkvisited(arr):
           
            for a in visited:
                found=True
                for i in range(2):
                    for j in range(3):
                        if a[i][j]!=arr[i][j]:
                            found=False
                            break
                    if not found:
                        break
                if found:
                    return True
            return False
                        
        check[-1][-1]=0
        def checkup(arr1,arr2):
            for i in range(2):
                for j in range(3):
                    if arr1[i][j]!=arr2[i][j]:
                        return False
            return True
        visited=[]
        def change(board,i,j):
            ans=[]
            for k,m in [(-1,0),(1,0),(0,-1),(0,1)]:
                
                
                x=i+k
                y=j+m
                temp=deepcopy(board)
                if 0<=x<len(board) and 0<=y<len(board[0]) :
                    temp[i][j]=temp[x][y]
                    temp[x][y]=0
                    if not checkvisited(temp):
                        ans.append((temp,x,y))
                        visited.append(temp)
            return ans
        visited.append(board)  
        length=0
        while level:
            for _ in range(len(level)):
                node,n,m=level.popleft()
                if checkup(node,check):
                    return length
                value=change(node,n,m)
                for i in value:
                    level.append(i)
            length+=1
        # print(visited)
        return -1
                
            
            