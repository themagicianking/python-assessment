import unittest
from python_assesment import subtract_numbers, divide_numbers


class TestCalculations(unittest.TestCase):
    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(6, 3), 3)
        self.assertEqual(subtract_numbers(-5, 2), -7)
        with self.assertRaises(TypeError):
            subtract_numbers("hi", "hello")

    def test_divide_numbers(self):
        self.assertEqual(divide_numbers(4, 2), 2)
        self.assertEqual(divide_numbers(9, 4), 2.25)
        with self.assertRaises(ZeroDivisionError):
            divide_numbers(10, 0)
        with self.assertRaises(TypeError):
            divide_numbers("hi", "hello")


if __name__ == "__main__":
    unittest.main()
