
"""
:MaxStack implementation:
using two stack to maintain the stats.
Retrieves max takes constant time.
"""

class MaxStack:

    def __init__(self) -> None:
        self.stack = []
        self.max_stack = []

    def __repr__(self):
        return "\tStack: %s\n \tMaxStack: %s" % (
            self.stack, self.max_stack)

    def push(self, value) -> None:
        self.stack.append(value)
        if not self.max_stack or self.max_stack[-1][0] < value:
            self.max_stack.append([value, 1])
        else:
            self.max_stack[-1][1] += 1

    def pop(self) -> None:
        if self.max_stack[-1][0] == self.stack[-1]:
            self.max_stack[-1][1] -= 1

        if self.max_stack[-1][1] == 0:
            self.max_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_max(self):
        return self.max_stack[-1][0]


max_stack = MaxStack()
max_stack.push(2)
max_stack.push(3)
max_stack.push(3)
max_stack.push(3)
max_stack.push(3)
max_stack.push(1)
assert max_stack.get_max() == 3
assert max_stack.top() == 1
max_stack.pop()
assert max_stack.top() == 3
max_stack.push(-1)
assert max_stack.get_max() == 3
max_stack.pop()
max_stack.pop()
max_stack.pop()
assert max_stack.get_max() == 3