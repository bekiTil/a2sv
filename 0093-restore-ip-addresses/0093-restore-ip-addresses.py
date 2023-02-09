class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(s, index, path, sol ):
            if index > 4:
                return 
            if index == 4 and not s:
                sol.append(path[:-1])
                return 
            for i in range(1, len(s)+1):
                if s[:i]=='0' or (s[0]!='0' and 0 < int(s[:i]) < 256):
                    dfs(s[i:], index+1, path+s[:i]+".", sol)
         
        solu = []
        dfs(s, 0, "", solu)
        return solu
    
        
