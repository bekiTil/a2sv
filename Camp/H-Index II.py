class Solution:
    def hIndex(self, citations: List[int]) -> int:
        i=0
        j=len(citations)-1
        while i<=j:
            mid=(i+j)//2
            if citations[mid]==(len(citations)-mid):
                return len(citations)-mid
                break
            elif citations[mid]>(len(citations)-mid):
                j=mid-1
            else:
                i=mid+1
        return len(citations)-i
