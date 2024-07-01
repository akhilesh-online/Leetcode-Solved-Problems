class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroth_position = 0
        
        for pos, num in enumerate(nums):
            if num != 0 and nums[zeroth_position] == 0:
                nums[zeroth_position], nums[pos] = num, nums[zeroth_position]
            
            if nums[zeroth_position] != 0:
                zeroth_position += 1