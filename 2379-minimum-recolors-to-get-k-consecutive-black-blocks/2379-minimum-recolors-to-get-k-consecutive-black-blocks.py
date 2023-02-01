class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans=[]
        for i in blocks:
            if i=="B":
                ans.append(1)
            else:
                ans.append(0)
        temp=len(blocks)
        for i in range(1,len(blocks)):
            ans[i]+=ans[i-1]
        temp=min(temp,k-ans[k-1])
      
        for i in range(k,len(blocks)):
          
            temp=min(temp,k - (ans[i]-ans[i-k]) )
        return temp
            
                
                
            