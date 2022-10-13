class Solution:
    def minimumSum(self, num: int) -> int:
        list_of_num = list(map(int, str(num)))
        list_of_num.sort()
        return list_of_num[0]*10+list_of_num[2] + list_of_num[1]*10+list_of_num[3]