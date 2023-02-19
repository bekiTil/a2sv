class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        left = nums
        right = list(reversed(nums))
       
        for i in range(1,len(left)):
            left[i]+=left[i-1]
            
        
        for i in range(1,len(right)):
            right[i]+=right[i-1]
            
        
        bench_mark=float('inf')
        for i in range(len(left)):
            if left[i]==x:
                bench_mark = i+1
                break
                
        for i in range(len(right)):
            if right[i]==x:
                bench_mark = min (bench_mark , i+1)
                
        for idx,val in enumerate(left):
            value = x - val
            if value <= 0:
                break
            
            i  = 0
            
            j  = (len(right)-idx)-2
            
            index = -1
            
            
            while i <= j:
                
                mid = (i+j)//2
                
                if right[mid]==value:
                    index = mid
                    break
                elif right[mid]>value:
                    j = mid-1
                else:
                    i= mid + 1
            if index!=-1:
                bench_mark = min (bench_mark , (index + idx)+2)
        if bench_mark== float('inf'):
            return -1
        return bench_mark
            
            
      
        
        