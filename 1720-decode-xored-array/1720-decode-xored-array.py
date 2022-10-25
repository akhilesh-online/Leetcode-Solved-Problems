class Solution:
    __scope__ = ['result']
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        for n in encoded:
            result.append(result[-1] ^ n)
        return result