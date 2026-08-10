class MinStack:

    def __init__(self):
        self.stack = []
        self.secondary_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.secondary_stack:
            self.secondary_stack.append(val)
        else:
            self.secondary_stack.append(min(val, self.secondary_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.secondary_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.secondary_stack[-1]
