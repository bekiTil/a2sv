 def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
       
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        print(dic)
        dic=dict(sorted(dic.items(), key=lambda items:items[1] ,reverse=True))
        new=list(dic.keys())
        return new[:k]
