class Solution:
    def sumOfMultiples(self, n: int) -> int:
        result = 0
        for x in range(n+1):
            if ((x%3==0) or (x%5==0) or (x%7==0)):
                result += x
        return result