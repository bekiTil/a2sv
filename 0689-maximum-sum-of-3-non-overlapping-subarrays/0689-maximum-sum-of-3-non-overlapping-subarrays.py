class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        
        
        def find(i,k):
            return prefix[i+k]-prefix[i]
        
        prefix=[0]
        
        for i in nums:
            prefix.append(prefix[-1]+i)
        
        
        left=[float("-inf") for _ in range(len(nums))]
        
        right=[float("-inf") for _ in range(len(nums))]
        
        for i in range(k,len(prefix)):
            if i!=k:
                if prefix[i]-prefix[i-k]>prefix[left[i-2]+k]-prefix[left[i-2]]:
                    left[i-1]=i-k
                else:
                    left[i-1]=left[i-2]
            else:
                left[i-1]=i-k
           
                
        
        for i in range(len(prefix)-k,0,-1):
            if i!=len(prefix)-k:
                if prefix[i+k-1]-prefix[i-1]>=prefix[right[i]+k]-prefix[right[i]]:
                    right[i-1]=i-1
                else:
                    right[i-1]=right[i]
            else:
                right[i-1]=i-1
        
        
        maximum=float("-inf")
        
        
        for i in range(k*2-1,len(nums)-k):
            total=prefix[i+1]-prefix[i+1-k]
           
            total+=find(left[i-k],k)
            
            total+=find(right[i+1],k)
            
            
            if total>maximum:
                ans=[left[i-k],i-k+1,right[i+1]]
                maximum=total
        return ans