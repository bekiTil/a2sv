class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        degree=[0]*n
        ans=[]
        for _ in range(n):
            ans.append(set())
        
        memo={}
        for i in edges:
            degree[i[1]]+=1
            if i[0] in memo:
                memo[i[0]].append(i[1])
            else:
                memo[i[0]]=[i[1]]
        level=deque([])
        for i in range(n):
            if degree[i]==0:
                level.append(i)
        while level:
            first=level.popleft()
            
            if first not in memo:
                continue
            for i in memo[first]:
                degree[i]-=1
                for m in ans[first]:
                    ans[i].add(m)
                ans[i].add(first)
                if degree[i]==0:
                    level.append(i)
        
        for i in range(n):
            
            ans[i]=sorted(list(ans[i]))
       
        return ans
