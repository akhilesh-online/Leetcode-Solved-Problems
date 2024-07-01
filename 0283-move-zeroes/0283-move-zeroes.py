class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroth_position = 0
        
        for pos in range(len(nums)):
            if nums[pos] != 0 and nums[zeroth_position] == 0:
                nums[zeroth_position], nums[pos] = nums[pos], nums[zeroth_position]
            
            if nums[zeroth_position] != 0:
                zeroth_position += 1