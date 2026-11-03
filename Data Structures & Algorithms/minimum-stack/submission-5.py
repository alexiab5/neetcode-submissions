class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minimums) == 0:
            self.minimums.append(val)
        else:
            self.minimums.append(min(val, self.minimums[-1]))

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()
        self.minimums.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.minimums[-1]
