class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.mini = float('inf')
        def backtrack(arr, path,k,maxi):
            if len(arr)==0:
                self.mini = min(self.mini, maxi)
                return 
            for i in range(k):
                path[i]+=arr[0]
                
                
                backtrack(arr[1:], path,k,max(maxi,path[i]))
                path[i]-=arr[0]
        value =[0 for _ in range(k)]
        if  k == len(cookies):
            return max(cookies)
        backtrack(cookies,value,k,0)
        
        return self.mini
        