class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        zero=0
        one=0
        new=[]
        for i in range(len(board)):
            new.append([])
            for j in range(len(board[i])):
                new[-1].append(board[i][j])
       
        for i in range(len(board)):
            
            for j in range(len(board[0])):
                zero=0
                one=0
                for (n,m) in [(i+1,j),(i+1,j+1),(i,j-1),(i+1,j-1),(i,j+1),(i-1,j-1),(i-1,j),(i-1,j+1)]:
                    if n>=0 and n<len(board) and m>=0 and m<len(board[0]):
                        if board[n][m]==0:
                            zero+=1
                        else:
                            one+=1
                            
                if board[i][j]==0 and one==3:
                    new[i][j]=1
                elif board[i][j]==1 and one<2:
                    new[i][j]=0
                elif board[i][j]==1 and one>3:
                    new[i][j]=0
                else:
                    pass
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j]=new[i][j]
        