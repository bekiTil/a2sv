class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(list)
        visited=set()
        
        for index,val in enumerate(equations):
            a,b=val
            graph[a].append((b,values[index]))
            if values[index]!=0:
                graph[b].append((a,1/values[index]))
            visited.add(a)
            visited.add(b)
        def bfs(a,b):
            value=1
            level=deque([(a,1)])
            new=set()
            new.add(a)
            while level:
                length=len(level)
                for _ in range(length):
                    
                    val,num=level.popleft()
                    for node in graph[val]:
                        if node[0] not in new:
                            if node[0]==b:
                                return num*node[1]
                            level.append((node[0],node[1]*num))
                            new.add(node[0])
            return -1
        ans = []  
        for a,b in queries:
            
            if a==b and b in visited:
                ans.append(1)
                continue
            normal=bfs(a,b)
            
            if normal==-1:
                reverse=bfs(b,a)
                if reverse==-1 or reverse==0:
                    ans.append(-1)
                else:
                    ans.append(1/reverse)
            else:
                ans.append(normal)

                
            
        return ans
            
        