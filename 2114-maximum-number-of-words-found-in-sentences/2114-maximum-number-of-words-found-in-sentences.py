class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(map(lambda x: x.count(" ") + 1, sentences))