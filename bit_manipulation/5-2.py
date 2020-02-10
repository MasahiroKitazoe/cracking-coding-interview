import unittest


def binary_to_string(float_val):
    binary_representation = "0."
    while len(binary_representation) <= 32:
        if float_val == 0:
            return binary_representation
        multiplied = float_val * 2
        binary_representation += str(int(multiplied))
        float_val = multiplied - int(multiplied)
    return "ERROR"


class Test2(unittest.TestCase):
    def test_it(self):
        assert binary_to_string(float_val=0.72) == "ERROR"
        assert binary_to_string(float_val=0.5) == "0.1"


if __name__ == "__main__":
    unittest.main()
