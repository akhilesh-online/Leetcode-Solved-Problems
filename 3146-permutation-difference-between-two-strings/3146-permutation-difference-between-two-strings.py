class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        return sum(abs(i - t.find(ch)) for i, ch in enumerate(s))
            