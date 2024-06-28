class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        c1 = float('inf')
        c2 = float('inf')
        for x in nums:
            if x <= c1:
                c1 = x
            elif x <= c2:
                c2 = x
            else:
                return True
            
        return False