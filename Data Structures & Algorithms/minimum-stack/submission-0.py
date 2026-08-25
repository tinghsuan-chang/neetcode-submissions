class MinStack:

    def __init__(self):
        self.items = []
        self.mins = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if not self.mins:
            self.mins.append(val)
        else:
            min_val = self.mins[-1]
            if val < min_val:
                self.mins.append(val)
            else:
                self.mins.append(min_val)

    def pop(self) -> None:
        self.items.pop()
        self.mins.pop()
        
    def top(self) -> int:
        return self.items[-1]
        
    def getMin(self) -> int:
        return self.mins[-1]


