import unittest


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.stack:
            self.stack.pop()

    def __len__(self):
        return len(self.stack)


class SetOfStacks:
    MAXIMUM_STACKS = 10

    def __init__(self):
        self._set_of_stacks = []

    def push(self, x):
        if not self._set_of_stacks or len(self._set_of_stacks[-1]) == self.MAXIMUM_STACKS:
            self._set_of_stacks.append(Stack())
        self._set_of_stacks[-1].push(x)

    def pop(self):
        if not self._set_of_stacks:
            return

        self._set_of_stacks[-1].pop()
        if len(self._set_of_stacks[-1]) == 0:
            del self._set_of_stacks[-1]

    def pop_at(self, idx):
        self._set_of_stacks[idx].pop()
        if len(self._set_of_stacks[idx]) == 0:
            del self._set_of_stacks[idx]


class TestCase(unittest.TestCase):
    def test_it(self):
        set_of_stacks = SetOfStacks()
        for i in range(10):
            set_of_stacks.push(i)
        assert len(set_of_stacks._set_of_stacks) == 1
        assert set_of_stacks._set_of_stacks[0].stack == [i for i in range(10)]

        set_of_stacks.push(11)
        set_of_stacks.push(12)
        assert len(set_of_stacks._set_of_stacks) == 2
        assert set_of_stacks._set_of_stacks[1].stack == [11, 12]

        set_of_stacks.pop()
        assert len(set_of_stacks._set_of_stacks) == 2
        assert set_of_stacks._set_of_stacks[0].stack == [i for i in range(10)]
        assert set_of_stacks._set_of_stacks[1].stack == [11]

        set_of_stacks.pop()
        assert len(set_of_stacks._set_of_stacks) == 1
        assert set_of_stacks._set_of_stacks[0].stack == [i for i in range(10)]

    def test_pop_at(self):
        set_of_stacks = SetOfStacks()
        for i in range(35):
            set_of_stacks.push(i)
        assert len(set_of_stacks._set_of_stacks) == 4

        set_of_stacks.pop_at(0)
        assert set_of_stacks._set_of_stacks[0].stack == [0,1,2,3,4,5,6,7,8]
        assert set_of_stacks._set_of_stacks[1].stack == [i for i in range(10, 20)]
        assert set_of_stacks._set_of_stacks[2].stack == [i for i in range(20, 30)]
        assert set_of_stacks._set_of_stacks[3].stack == [i for i in range(30, 35)]

        for _ in range(10):
            set_of_stacks.pop_at(0)

        assert len(set_of_stacks._set_of_stacks) == 3
        assert set_of_stacks._set_of_stacks[0].stack == [i for i in range(10, 19)]


if __name__ == "__main__":
    unittest.main()
