class OrderedStream:

    def __init__(self, n: int):
        self.stream = ['']*(n+1)
        self.pos = 1
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        res = []
        
        while self.pos < len(self.stream) and self.stream[self.pos]:
            res.append(self.stream[self.pos])
            self.pos += 1
        return res
            
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)