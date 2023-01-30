class Solution:
    def minSteps(self, n: int) -> int:
        total = 0
        num = 2
        while n > 1:
            while n % num == 0:
                total += num
                n /= num
            num += 1
        return total