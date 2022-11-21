class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        level=deque([])
        level.append((entrance[0],entrance[1]))
        step=0
        visited=set()
        visited.add((entrance[0],entrance[1]))
        
        while level:
            length=len(level)
            
            for _ in range(length):
                x,y=level.popleft()
                for i,j in [(-1,0),(1,0),(0,1),(0,-1)]:
                    n=x+i
                    m=y+j
                    if 0<=n<len(maze) and 0<=m<len(maze[0]) and (n,m) not in visited and maze[n][m]!="+":
                        if n==0 or n==len(maze)-1 or m==0 or m==len(maze[0])-1:
                            return step+1
                        visited.add((n,m))
                        level.append((n,m))
             
            step+=1
        return -1