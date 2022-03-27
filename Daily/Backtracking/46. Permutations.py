#time Complexity O(n!)
#Space Complexity O(n!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        ans.append([])
        
        def helper(nums):
            if len(nums)==1:
                ans[-1].append(nums[0])
                
                return 
                
            else:
                for i in range(len(nums)):
                    ans[-1].append(nums[i])
                    if i==0:
                        num=nums[i+1:]
                    elif i==len(nums)-1:
                        num=nums[:i]
                    else:
                        num=nums[:i] +nums[i+1:]
                    helper(num)
                    if i==len(nums)-1:
                        pass
                    else:
                        ans.append(ans[-1][:(0-len(nums))])
                    
        helper(nums)
        return ans
        
                
