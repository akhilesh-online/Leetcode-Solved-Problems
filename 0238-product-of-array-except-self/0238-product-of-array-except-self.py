class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_length = len(nums)
        leftside_product = 1
        rightside_product = 1
        result = [0] * arr_length
        
        for i in range(arr_length):
            result[i] = leftside_product
            leftside_product *= nums[i]
        
        for i in range(arr_length-1, -1, -1):
            result[i] *= rightside_product
            rightside_product *= nums[i]
        
        return result