class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = list(map(lambda x: sum(x), accounts))
        return max(wealth)