class Solution:
    def maximumSwap(self, num: int) -> int:
        num=list(str(num))
        pair=[]
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                if num[i]<num[j]:
                    heappush(pair,[i,-1*int(num[j]),-1*j])
        print(pair)
        if not pair:
            return int("".join(num))
        i,value,j=heappop(pair)
        num[i],num[-1*j]=num[-1*j],num[i]
        return int("".join(num))