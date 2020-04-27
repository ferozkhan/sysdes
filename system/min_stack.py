

class MinStack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, value) -> None:
        if not self.stack:
            self.stack.append((value, value))
        else:
            self.stack.append((value, min(self.stack[-1][1], value)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def get_min(self) -> int:
        return self.stack[-1][1]


min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
assert min_stack.get_min() == -3
min_stack.pop()
assert min_stack.top() == 0
assert min_stack.get_min() == -2
