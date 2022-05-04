class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        degree=[0]*numCourses
        ans=defaultdict(set)
        
        memo={}
        for i in prerequisites:
            degree[i[1]]+=1
            if i[0] in memo:
                memo[i[0]].append(i[1])
            else:
                memo[i[0]]=[i[1]]
        level=deque([])
        for i in range(numCourses):
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
        
        for i in ans:
            
            ans[i]=sorted(ans[i])
        
        solve=[]
        
        for i in queries:
            if i[1] not in ans:
                solve.append(False)
            else:
                if i[0] not in ans[i[1]]:
                    solve.append(False)
                else:
                    solve.append(True)
        
        return solve
