import unittest


def binary_to_string(float_val):
    binary_representation = "0."
    while len(binary_representation) <= 32 and float_val > 0:
        multiplied = float_val * 2
        binary_representation += str(int(multiplied))
        float_val = multiplied - int(multiplied)
    return "ERROR"


class Test2(unittest.TestCase):
    def test_it(self):
        assert binary_to_string(float_val=0.72) == "ERROR"


if __name__ == "__main__":
    unittest.main()
