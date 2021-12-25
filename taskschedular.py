class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        dic={}
        for i in tasks:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        dic=dict(sorted(dic.items(), key=lambda item:item[1], reverse=True))
        print(dic)
        ls=list(dic.values())
        output=(n+1)*ls[0]-n
        for i in range(1,len(ls)):
            if ls[i]==ls[0]:
                output+=1
            else:
                break
        if output<len(tasks):
            return len(tasks)
        return output
      
