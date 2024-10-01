class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder = []
        
        for val in arr:
            remainder.append(val%k)
        count=defaultdict(int)
        for rem in remainder:
            count[rem]+=1
        for rem in remainder:
            if count[rem]>0:
                count[rem]-=1
                if count[(k-rem)%k]:
                    count[(k-rem)%k]-=1
                else:
                    return False
        for rem in remainder:
            if count[rem]:
                return False
        return True