class Solution:
    __scope__ = ['indices']
    
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        indices = {}
        for i, num in enumerate(sorted(nums)):
            indices.setdefault(num, i)
        return [indices[num] for num in nums]