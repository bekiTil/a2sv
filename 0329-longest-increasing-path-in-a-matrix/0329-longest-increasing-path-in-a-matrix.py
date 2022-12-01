class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        graph=defaultdict(list)
        count=defaultdict(int)
        back=defaultdict(list)
        cache=defaultdict(int)
        for i in range(len(matrix)):
            
            for j in range(len(matrix[0])):
                
                for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
                    
                    n=i+x
                    m=j+y
                    
                    if 0<=n<len(matrix) and 0<=m<len(matrix[0]) and matrix[i][j]<matrix[n][m]:
                        graph[(i,j)].append((n,m))
                        count[(n,m)]+=1
                        # back[(n,m)].append((i,j))
        level=deque([])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if count[(i,j)]==0:
                    level.append((i,j))
        # print(level)
        maximum=0
        while level:
            node=level.popleft()
            for val in graph[node]:
                count[val]-=1
                if count[val]==0:
                    level.append(val)
            for val in graph[node]:
                cache[val]=max(cache[val],cache[node]+1)
                maximum=max(cache[val]+1,maximum)
        # print(cache)
        if maximum==0:
            return 1
        return maximum
            