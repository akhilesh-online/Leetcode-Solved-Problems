class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        l = min(len(word1), len(word2))
        for i in range(l):
            result += word1[i] + word2[i]
        result += word1[l:] + word2[l:]
        return result