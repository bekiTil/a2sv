class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        ans=[i for i in range(len(quiet))]
        
        graph = defaultdict(list)
        inDegree = defaultdict(int)
        
        for i,j in richer:
            graph[i].append(j)
            inDegree[j]+=1
            
        level =deque([])
        
        for i in range(len(quiet)):
            if inDegree[i]==0:
                level.append(i)
            
        
        
        while level:
            length = len(level)
            
            for _ in range(length):
                node = level.popleft()
                
                for nex in graph[node]:
                    inDegree[nex]-=1
                    if quiet[ans[nex]] > quiet[ans[node]]:
                        ans[nex]= ans[node]
                   
                    if inDegree[nex]==0:
                        level.append(nex)
        print(ans)
        return ans