import unittest
from dataclasses import dataclass
import json
import pickle

# task 1 - Unitest
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

# task 2 - Data packing

@dataclass
class Book:
    title: str
    author: str
    year: int

    def to_json(self) -> str:
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json(json_data: str):
        data = json.loads(json_data)
        return Book(**data)

    def to_pickle(self) -> bytes:
        return pickle.dumps(self)

    @staticmethod
    def from_pickle(pickle_data: bytes):
        return pickle.loads(pickle_data)

class TestBook(unittest.TestCase):
    def test_json_serialization(self):
        book = Book("1984", "George Orwell", 1949)
        json_data = book.to_json()
        loaded_book = Book.from_json(json_data)
        self.assertEqual(book, loaded_book)

    def test_pickle_serialization(self):
        book = Book("1984", "George Orwell", 1949)
        pickle_data = book.to_pickle()
        loaded_book = Book.from_pickle(pickle_data)
        self.assertEqual(book, loaded_book)

if __name__ == "__main__":
    unittest.main()

    