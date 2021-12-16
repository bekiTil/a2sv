def minSetSize(self, arr: List[int]) -> int:
        dic={}
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        
        sum=0
        j=0
        dic=dict(sorted(dic.items() , key=lambda items:items[1] ,reverse=True))
        
        for i in dic:
            sum+=dic[i]
            j+=1
            if sum>=len(arr)/2:
                return j
    
        
