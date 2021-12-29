class Solution:
    def maxArea(self, height: List[int]) -> int:
        max=0
        i=0
        j=len(height)-1
        while i<j:
            new=min(height[i],height[j])*(j-i)
            if new>max:
                max=new
            if height[i]==min(height[i],height[j]):
                i+=1
            else:
                j-=1
        return max
      
