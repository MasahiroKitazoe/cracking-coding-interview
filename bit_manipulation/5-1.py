import unittest


def insert_bit(n, m, i, j):
    """
    1. 入れないといけない桁数を数える
    2. mで足りてない桁数分右にシフトさせる
    3. i桁分mを左shiftする
    4. nのj桁目からi桁目をclearする
    5. n | mして終了
    """
    spaces = j - i + 1
    m_digits = len(bin(m)) - 2
    m = m>>spaces - m_digits
    m = m<<i
    mask = -1 << spaces + 1
    n = n & mask
    return n | m


class Test5(unittest.TestCase):
    def test_it(self):
        n = insert_bit(n=0b10000000000, m=0b10011, i=2, j=6)
        assert bin(n) == bin(0b10001001100)


if __name__ == "__main__":
    unittest.main()
