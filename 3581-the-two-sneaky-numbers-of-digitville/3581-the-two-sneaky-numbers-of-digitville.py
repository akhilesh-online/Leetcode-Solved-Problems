class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        result = []
        for i, n in enumerate(nums):
            if n in nums[i+1:]:
                result.append(n)
                if len(result) == 2:
                    break
        return result