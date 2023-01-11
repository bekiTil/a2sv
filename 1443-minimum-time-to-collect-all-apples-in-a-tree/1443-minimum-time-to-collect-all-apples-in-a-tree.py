class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.ans=0
        def dfs(node,path,find):
            exist=False
            for value in graph[node]:
                if value not in visited:
                    visited.add(value)
                    if dfs(value,path+1,exist):
                        exist=True
            if hasApple[node] or exist==True:
                self.ans+=2
                exist=True
           
           
            return exist
        graph=defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited=set()
        visited.add(0)
        dfs(0,0,False)
      
        return self.ans-2 if self.ans-2>0 else 0
                        