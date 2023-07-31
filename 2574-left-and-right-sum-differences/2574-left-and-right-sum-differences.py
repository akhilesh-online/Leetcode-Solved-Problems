class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        prefix = 0
        suffix = sum(nums)
        for num in nums:
            suffix -= num
            answer.append(abs(prefix - suffix))
            prefix += num 
        return answer