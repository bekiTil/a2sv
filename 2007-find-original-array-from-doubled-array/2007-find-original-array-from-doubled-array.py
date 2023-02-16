class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2!=0:
            return []
        length=len(changed)
        new=set(changed)
        memo=defaultdict(int)
        for i in changed:
            memo[i]+=1
        changed.sort()
        ans=[]
        for value in reversed(changed):
            if len(ans)<len(changed)//2:
                if memo[value]>0 and value%2==0:
                    memo[value]-=1
                    if value//2 in new and memo[value//2]>0:
                        memo[value//2]-=1
                        ans.append(value//2)

        if len(ans)==length//2:
            return ans
        return []