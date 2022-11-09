class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        
        prefix=[0]
        left_first=[float("-inf") for _ in range(len(nums))]
        right_first=[float("-inf") for _ in range(len(nums))]
        
        left_second=[float("-inf") for _ in range(len(nums))]
        right_second=[float("-inf") for _ in range(len(nums))]
        
        for i in nums: 
            prefix.append(prefix[-1]+i)
        
        for i in range(firstLen,len(prefix)):
            if i-2<0:
                left_first[i-1]=prefix[i]-prefix[i-firstLen]
            else:
                left_first[i-1]=max(prefix[i]-prefix[i-firstLen],left_first[i-2])
           
        for i in range(len(prefix)-firstLen-1,-1,-1):
            if i+1>=len(nums):
                right_first[i]=prefix[i+firstLen]-prefix[i]
            else:
                right_first[i]=max(prefix[i+firstLen]-prefix[i],right_first[i+1])
        
        for i in range(secondLen,len(prefix)):
            if i-2<0:
                left_second[i-1]=prefix[i]-prefix[i-secondLen]
            else:
                left_second[i-1]=max(prefix[i]-prefix[i-secondLen],left_second[i-2])
        
        
        for i in range(len(prefix)-secondLen-1,-1,-1):
            if i+1==len(nums):
                right_second[i]=prefix[i+secondLen]-prefix[i]
            else:
                right_second[i]=max(prefix[i+secondLen]-prefix[i],right_second[i+1])
        
        maximum=float("-inf")
        for i in range(min(firstLen,secondLen)-1,len(nums)):
            
            if i+1<firstLen:
                total=prefix[i+1]-prefix[i+1-secondLen]
                
                if i-secondLen<0:
                    if i + secondLen<len(nums):
                        total+=right_first[i+secondLen]
                    else:
                        total=0
                elif i+secondLen>=len(nums):
                    total+=left_first[i-secondLen]
                else:
                    total+=max(left_first[i-secondLen],right_first[i+secondLen])
            elif i+1<secondLen:
                total=prefix[i+1]-prefix[i+1-firstLen]
                
                if i-firstLen<0:
                    if i + firstLen<len(nums):
                        total+=right_second[i+firstLen]
                    else:
                        total=0
                elif i+firstLen>=len(nums):
                    total+=left_second[i-firstLen]
                else:
                    total+=max(left_second[i-firstLen],right_second[i+firstLen])
            else:
                total1=prefix[i+1]-prefix[i+1-secondLen]
                
                if i-secondLen<0:
                    if i + secondLen<len(nums):
                        total1+=right_first[i+secondLen]
                    else:
                        total1=0
                elif i+secondLen>=len(nums):
                    total1+=left_first[i-secondLen]
                else:
                    total1+=max(left_first[i-secondLen],right_first[i+secondLen])
                
                total2=prefix[i+1]-prefix[i+1-firstLen]
                
                if i-firstLen<0:
                    if i + firstLen<len(nums):
                        total2+=right_second[i+firstLen]
                    else:
                        total=0
                elif i+firstLen>=len(nums):
                    total2+=left_second[i-firstLen]
                else:
                    total2+=max(left_second[i-firstLen],right_second[i+firstLen])
                total=max(total1,total2)
           
            maximum=max(total,maximum)
                
        return maximum
                
                
                    
                        
                
        
            