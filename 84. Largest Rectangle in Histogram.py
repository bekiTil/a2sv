class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maximum=float("-inf")
        stack=[]
        n=len(heights)
        for i,num in enumerate(heights):
            if not stack or stack[-1][1]<=num:
                stack.append((i,num))
                continue
            while stack and stack[-1][1]>num:
                j,current=stack.pop()
                if stack:
                    j=stack[-1][0]+1
                else:
                    j=0
                new=(i-j)*current
                maximum=max(new,maximum)
            stack.append((i,num))
       
        while stack:
            j,current=stack.pop()
            if not stack:
                index=0
            else:
                index=stack[-1][0]+1
            maximum=max(maximum,current*(n-index))
        return maximum
