class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # num2 = m + 2m + 3m + .. + km
        # num2 = (1 + 2 + 3 + .. + k) * m
        # km <= n
        
        k = n // m
        
        num2 = (k * (k+1))// 2 * m
        
        num1 = (n*(n+1))//2 - num2
        
        return num1 - num2