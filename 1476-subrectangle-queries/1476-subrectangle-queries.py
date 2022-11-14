class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = copy.deepcopy(rectangle)
        self.history = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.history.append([row1, col1, row2, col2, newValue])

    def getValue(self, row: int, col: int) -> int:
        for his in reversed(self.history):
            if his[0] <= row <= his[2] and his[1] <= col <= his[3]:
                return his[4]
        return self.rectangle[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)