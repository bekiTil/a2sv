class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictionary=dict()
        stack=[]
        ans=[]
        for i in range(len(nums2)-1,-1,-1): 
            while(len(stack)!=0 and stack[-1]<=nums2[i]):
                stack.pop()
            if len(stack)==0:
                dictionary[nums2[i]]=(-1)
            else:
                dictionary[nums2[i]]=(stack[-1])
            stack.append(nums2[i])
        for i in nums1:
            if i in dictionary:
                ans.append(dictionary[i])
        return ans
