#time Complexity O(n)
#Space Complexity O(n)

class Solution:
    def minDeletions(self, s: str) -> int:
        memo=defaultdict(int)
        for i in s:
            memo[i]+=1
        
        dup=[]
        
        for i in memo:
            dup.append(memo[i])
        
        dup=sorted(dup,reverse=True)
        ans=0
        check=set()
        print(dup)
        for i in dup:
            if i not in check:
                check.add(i)
                minium=i
            else:
                if minium==0:
                    ans+=(i)
                else:
                    ans+=(i-minium)+1
                    minium-=1
                check.add(minium)
        return ans
                
                
