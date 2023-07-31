class Solution:
    def balancedStringSplit(self, s: str) -> int:
        Ls = Rs = answer = 0
        for x in s:
            if x == 'L':
                Rs -= 1
            else:
                Ls -= 1
            if Rs == Ls:
                answer += 1
        return answer