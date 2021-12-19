class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack and self.minStack[-1] >= val:
            self.minStack.append(val)
        elif not self.minStack:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if self.minStack and val == self.minStack[-1]:
                self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]


