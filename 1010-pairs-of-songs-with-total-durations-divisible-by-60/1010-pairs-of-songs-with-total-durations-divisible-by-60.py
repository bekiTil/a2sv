class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count=defaultdict(int)
        for i in time:
            count[i%60]+=1
        temp=[]
        for i in count:
            temp.append(i)
        visited=set()
        ans=0
        print(temp)
        for val in temp:
            if val==0:
                ans+=(count[val]*(count[val]-1))//2
            elif 60-val==val :
                visited.add(val)
                ans+=(count[val]*(count[val]-1))//2
            elif val not in visited :
                visited.add(60-val)
                ans+=count[(60-val)]*count[val]
        return ans
                