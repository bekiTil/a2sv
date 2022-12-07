class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        index=[0]
        prefix=[0]
        for i in range(len(nums)):
            if nums[i]==1:
                index.append(i)
                prefix.append(prefix[-1]+i)
        j=1
        minimum=float("inf")
        print(prefix,index)
        for i in range(k,len(prefix)):
            mid=(j+i)//2
            val=index[mid]
            length=mid-j
            ans=val*length-(prefix[mid-1]-prefix[j-1])
            ans-=((length*(length+1))//2)
            length=i-mid
            temp=(prefix[i]-prefix[mid])-val*length
            temp-=((length*(length+1))//2)
            minimum=min(minimum,temp+ans)
            # print(minimum)
            # print(ans,temp,i,j,mid)
            j+=1
        # print(minimum)
        return minimum