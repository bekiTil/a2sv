class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        double=defaultdict(int)
        single=defaultdict(int)
        distnict=list(set(nums))
        distnict.sort()
        
        
        value=[]
        for i in range(len(nums)):
            value.append((nums[i],cost[i]))
        value.sort()
        
        for i in range(len(nums)):
            x,y=value[i]
            double[x]+=(x*y)
            single[x]+=y
        
        visited=set()
        ans=[]
        temp=[]
        for val,tem in value:
            if val not in visited:
                visited.add(val)
                ans.append(double[val])
                temp.append(single[val])  
        prefix=[0]
        sprefix=[0]
        for i in range(len(ans)):
            prefix.append(prefix[-1]+ans[i])
            sprefix.append(sprefix[-1]+temp[i])
        
        minimum=float("inf")
        for i in range(len(ans)):
            n=distnict[i]
            
            left,right=prefix[i],prefix[-1]-prefix[i+1]
            mleft,mright=sprefix[i],sprefix[-1]-sprefix[i+1]
            
            variable=(mleft-mright)*n
            constant=(left-right)
            total=variable-constant
            minimum=min(minimum,total)
        return minimum
            