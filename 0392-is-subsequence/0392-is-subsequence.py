class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        if len_s == 0:
            return True
        pos = 0
        
        for i in range(len(t)):
            if t[i] == s[pos]:
                pos += 1
            if pos == len_s:
                return True
        return False