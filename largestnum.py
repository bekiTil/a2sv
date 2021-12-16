def largestNumber(self, nums: List[int]) -> str:
        new=[]
        for i in nums:
            new.append(str(i))
        for i in range(1,len(new)):
            j=i-1
            num=str(nums[i])
            print(num)
            while j>=0 and num+new[j]> new[j]+num:
                new[j],new[j+1]=new[j+1],new[j]
                j-=1
        if new[0]=="0":
            return "0"
        return "".join(new)
