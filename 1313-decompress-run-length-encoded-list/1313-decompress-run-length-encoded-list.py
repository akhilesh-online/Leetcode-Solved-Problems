class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        i = 0
        length_nums = len(nums)
        while (i+i+1) < length_nums:
            result.extend([nums[2*i+1]]*nums[2*i])
            i+=1
        return result