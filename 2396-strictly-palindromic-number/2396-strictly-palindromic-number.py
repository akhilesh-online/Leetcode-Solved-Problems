class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n-1):
            res = []
            k = n
            while k > 0:
                res.append(k % n)
                k //= base
            if res != res[::-1]: return False
        return True