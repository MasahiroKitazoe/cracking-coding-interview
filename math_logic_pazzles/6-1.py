import unittest

import random


class Bottle:
    def __init__(self, pills):
        self.pills = pills

    def drop_pills(self, amount):
        dropped = self.pills[:amount]
        self.pills = self.pills[amount:]
        return dropped


class Pill:
    def __init__(self, weight):
        self.weight = weight


def main(bottles):
    """return heavy bottle idx"""
    weight_sum = 0
    for i, bottle in enumerate(bottles):
        dropped = bottle.drop_pills(amount=i + 1)
        for pill in dropped:
            weight_sum += pill.weight
    return round((weight_sum - 210) * 10)


class Test1(unittest.TestCase):
    def test_it(self):
        bottles = []
        heavy_bottle_idx = random.randint(1, 20)
        for i in range(20):
            weight = 1.1 if i + 1 == heavy_bottle_idx else 1.0
            bottle = Bottle(pills=[Pill(weight) for _ in range(20)])
            bottles.append(bottle)

        res = main(bottles)
        assert heavy_bottle_idx == res


if __name__ == "__main__":
    unittest.main()
