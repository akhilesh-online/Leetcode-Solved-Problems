class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n-1):
            res = self.isPalindrome(self.getPalindrome(n, i))
            if res == False:
                return False
        return True
    
    def getPalindrome(self, n: int, base: int) -> str:
        result = ''
        while n > 0:
            result = str(n%base) + result
            n = n//base
        return result

    def isPalindrome(self, n: str) -> bool:
        l = len(n)
        count = 0
        while count <= l/2:
            if n[count] != n[l-1-count]:
                return False
            count += 1
        return True