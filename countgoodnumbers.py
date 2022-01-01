class Solution:
    def countGoodNumbers(self, n: int) -> int:       
        modulo = (10 ** 9) + 7
        return pow(5, (n + 1) // 2, modulo) * pow(4, n // 2, modulo) % modulo
                      
                      
