class Stack:
    def __init__(self, iterable=None):
        self.stack = [val for val in iterable] if iterable else []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def __len__(self):
        return len(self.stack)
