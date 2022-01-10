class Solution:
    def maxFrequency(self, arr: List[int], k: int) -> int:
        frequent=1
        l=1
        old=k
        start=0
        end=1
        arr=sorted(arr,reverse=True)
        sum=0
        while end<len(arr):
            while end<len(arr) and arr[start]-arr[end]<=k:
                sum+=arr[start]-arr[end]
                k-=(arr[start]-arr[end])
                l=(end-start)+1
                end+=1 
          
            sum-=(((end-1)-start)*(arr[start]-arr[start+1]))
            k=old-sum
            frequent=max(l,frequent)
            start+=1
            if start==end:
                end+=1
        return frequent
