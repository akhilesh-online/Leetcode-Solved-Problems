class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        repeat = {} # dict of number in nums as key and number of their repeatition as value
        for n in nums:
            if n in repeat:
                count += repeat[n]
                repeat[n] += 1
            else:
                repeat[n] = 1
        return count
            