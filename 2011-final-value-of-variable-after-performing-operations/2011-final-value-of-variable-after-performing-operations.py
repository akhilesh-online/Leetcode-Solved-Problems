class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        string_data = "".join(operations)
        return string_data.count("++") - string_data.count("--")