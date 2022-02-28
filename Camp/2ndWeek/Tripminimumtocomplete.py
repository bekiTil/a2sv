#Time Complexity
# O(nlog(m)) where m is the time interval
#Space Complexity
#O(1)

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def totaltrips(arr,num):
            total=0
            for i in arr:
                total+=math.floor(num/i)
            return total
        maximum=max(time)
        left=min(time)
        right=totalTrips*maximum
        new=0
        while left<=right:
            mid=(left+right)//2
            if totaltrips(time,mid)>=totalTrips:
                new=mid
                right=mid-1
            else:
                left=mid+1
        return new
                
        
