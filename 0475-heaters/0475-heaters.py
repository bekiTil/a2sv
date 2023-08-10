class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def merge(arr):
            length = len(arr)
            start, end = arr[0][0], arr[0][1]
            merged_arr = []
            for i in range(1, length):
                if end >= arr[i][0]:
                    end = max(end, arr[i][1])
                else:
                    merged_arr.append([start, end])
                    start = arr[i][0]
                    end = arr[i][1]
            merged_arr.append([start,end])
            return merged_arr

        def checker(houses, heaters, radius):
            interval = []
            for heater in heaters:
                interval.append([heater - radius, heater + radius])

            merge_intervals = merge(interval)
            index = 0
            count = 0
            size = len(merge_intervals)
            for house in houses:
                while index < size and not(merge_intervals[index][0] <= house <= merge_intervals[index][1]):
                    index += 1

                if index < size:
                    count += 1

            return count == len(houses)
    
    
        houses.sort()
        heaters.sort()

        left = -1
        diff_houses = abs(max(houses) - min(houses))
        diff = abs(max(heaters) - min(houses))
        right = max(diff_houses, diff) + 1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if checker(houses, heaters, mid):
                right = mid
            else:
                left = mid

        return right
        