class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maximum=0
        stack=[]
        heights.append(0)
        n=len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]]> heights[i]:
                value = stack.pop()
                if stack:
                    j = stack[-1] + 1
                else:
                    j = 0 
                maximum = max(maximum,(i-j)*heights[value])
            stack.append(i)
        return maximum