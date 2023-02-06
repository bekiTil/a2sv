class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        memo=defaultdict(list)
        maxi=1
        value=defaultdict(int)
        for index,word in enumerate(words):
            memo[len(word)].append(index)
            maxi=max(len(word),maxi)
        def checker(prev,nex):
            i=0
            for char in nex:
                if i<len(prev) and char==prev[i]:
                    i+=1
            return i==len(prev) and len(nex)-1==len(prev)
        dp=[1]*len(words)
        for i in range(1,maxi+1):
            for val in memo[i]:
                for v in memo[i-1]:
                    if checker(words[v],words[val]):
                        dp[val]=max(dp[v]+1,dp[val])
        return max(dp)
            