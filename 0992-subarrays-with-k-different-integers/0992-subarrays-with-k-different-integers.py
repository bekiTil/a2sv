class Solution:
    def subarraysWithKDistinct(self, num: List[int], k: int) -> int:
        def atMost(A, K):
            n = len(A)  
            count = defaultdict(int)
            left = 0
            res = 0

            for right in range(n):
                if count[A[right]] == 0:
                    K -= 1
                count[A[right]] += 1

                while K < 0:
                    count[A[left]] -= 1
                    if count[A[left]] == 0: 
                        K += 1
                    left += 1
                res += right - left + 1

            return res
        return atMost(num, k) - atMost(num, k - 1)
