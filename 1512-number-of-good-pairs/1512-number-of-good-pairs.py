class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        repeat = {}  # dict of 'values in nums' as key and 'their repeatition' as value
        for n in nums:
            if n in repeat:
                count += repeat[n]
                repeat[n] += 1  # repeatition value of key 'n' increased by 1 
            else:
                repeat[n] = 1  # inserted a new key value pair as {n: 1} in dict
        return count
            