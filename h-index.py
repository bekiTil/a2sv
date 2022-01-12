class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations=sorted(citations,reverse=True)
        i=0
        new=0
        index=0
        while i<len(citations):
            if citations[i]>=i+1:
                new=i+1
            index=max(index,new)
            i+=1
        return index
