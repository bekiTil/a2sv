class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row=len(board)
        column=len(board[0])
        new=set()
        visited=set()
        num=0
        
        for i in range(len(board)):
            if board[i][0]=="O":
                new.add((i,0))
                visited.add((i,0))
            if board[i][len(board[0])-1]=="O":
                new.add((i,len(board[0])-1))
                visited.add((i,len(board[0])-1))
               
        for i in range(len(board[0])):
            if board[0][i]=="O":
                new.add((0,i))
                visited.add((0,i))
            if board[len(board)-1][i]=="O":
                new.add((len(board)-1,i))
                visited.add((len(board)-1,i))

        def dfs(arr,pair):
            x,y=pair
            for i,j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0<=i<row and 0<=j<column and (i,j) not in visited and arr[i][j]=="O":
                    visited.add((i,j))
                    dfs(arr,(i,j))
        for i in new:
            dfs(board,i)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in visited and board[i][j]=="O":
                     board[i][j]="X"
        return board
                    
        
