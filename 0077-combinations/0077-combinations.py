class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(arr,path,k,n):
            if k == 0:
                
                ans.append(deepcopy(path))
                
                return 
            
            for index in range(arr,n+1):
                path.append(index)
                k-=1
                backtrack(index+1,path,k,n)
                k+=1
                path.pop()
        
        backtrack(1,[],k,n)
       
        return ans