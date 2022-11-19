class Solution:
    def minSwaps(self, array: List[int]) -> int:
        count=sum(array)
        # creating new arry 
        new_array=array*2
        left=0
        # sum of my first 
        window=sum(new_array[:count])
        # maximum ==window for start 
        maximum=window
        for right in range(count,len(new_array)):
            window-=new_array[left]
            window+=new_array[right]
            left+=1
            maximum=max(window,maximum)
        return count-maximum
        