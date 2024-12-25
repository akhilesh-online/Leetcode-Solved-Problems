class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join(f"{int(d):b}" for d in date.split("-"))