import unittest

from stack import Stack


class MyQueue:
    def __init__(self, iterable=None):
        self._oldest_stack = Stack(iterable[::-1])
        self._newest_stack = Stack()

    def enqueue(self, x):
        self._newest_stack.push(x)

    def dequeue(self):
        if len(self._oldest_stack) == 0:
            for val in [self._newest_stack.pop() for _ in range(len(self._newest_stack))]:
                self._oldest_stack.push(val)
        return self._oldest_stack.pop()


class TestCase(unittest.TestCase):
    def test_it(self):
        queue = MyQueue([1,2,3])
        queue.enqueue(4)
        queue.enqueue(5)
        assert queue._oldest_stack.stack == [3,2,1]
        assert queue._newest_stack.stack == [4,5]

        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.dequeue() == 4
        assert queue.dequeue() == 5
        assert queue._oldest_stack.stack == []
        assert queue._newest_stack.stack == []


if __name__ == "__main__":
    unittest.main()
