class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(lambda : [0,0])
        for index, val in enumerate(s):
            count[val][0]+=1
            if count[val][0]==1:
                count[val][1]=index

        for val in count:
            if count[val][0]==1:
                return count[val][1]
        return -1