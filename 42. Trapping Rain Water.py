#TIME COMLEXITY O(N)
#SPACE COMPLEXITY O(N)
class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        stack=[]
        visited=False
        for i in range(len(height)-1,-1,-1):
            if stack and stack[-1][0]<=height[i]:
                value=stack.pop()
                visited=True
                
            while stack and stack[-1][0]<=height[i]:
                mini=min(height[i],stack[-1][0])
                ans+=(mini-value[0])*((stack[-1][1]-i)-1)
                value=stack.pop()
            if stack and visited:
                mini=min(height[i],stack[-1][0])
                ans+=(mini-value[0])*((stack[-1][1]-i)-1)
            stack.append([height[i],i])
            # print(stack,ans)
        
        return ans
