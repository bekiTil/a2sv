class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr=[0 for _ in range(n+1)]
        
        for i,j,k in bookings:
            arr[i-1]+=k
            arr[j]-=k
        for i in range(1,n):
            arr[i]+=arr[i-1]
        return arr[:-1]