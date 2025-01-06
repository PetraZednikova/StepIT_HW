import unittest
from dataclasses import dataclass

# task 1
@dataclass
class IntegerSet:
    numbers: set[int]

    def sum(self) -> int:
        return sum(self.numbers)

    def mean(self) -> float:
        return sum(self.numbers) / len(self.numbers) if self.numbers else 0

    def maximum(self) -> int:
        return max(self.numbers) if self.numbers else None

    def minimum(self) -> int:
        return min(self.numbers) if self.numbers else None


class TestIntegerSet(unittest.TestCase):
    def test_sum(self):
        s = IntegerSet({1, 2, 3, 4})
        self.assertEqual(s.sum(), 10)

    def test_mean(self):
        s = IntegerSet({1, 2, 3, 4})
        self.assertAlmostEqual(s.mean(), 2.5)

    def test_maximum(self):
        s = IntegerSet({1, 2, 3, 4})
        self.assertEqual(s.maximum(), 4)

    def test_minimum(self):
        s = IntegerSet({1, 2, 3, 4})
        self.assertEqual(s.minimum(), 1)

    def test_empty_set(self):
        s = IntegerSet(set())
        self.assertEqual(s.sum(), 0)
        self.assertEqual(s.mean(), 0)
        self.assertIsNone(s.maximum())
        self.assertIsNone(s.minimum())

if __name__ == "__main__":
    unittest.main()





    