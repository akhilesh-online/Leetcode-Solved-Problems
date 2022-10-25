class Solution:
    __slots__ = ['product', 'sums']
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sums = 0
        for num in str(n):
            product *= int(num)
            sums += int(num)
        return product - sums