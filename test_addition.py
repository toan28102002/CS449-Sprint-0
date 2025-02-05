"test_addition"
import unittest

def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

class TestAddition(unittest.TestCase):
    """Unit tests for the add_numbers function."""

    def test_positive_numbers(self):
        """Test adding two positive numbers."""
        self.assertEqual(add_numbers(2, 3), 5)

    def test_negative_numbers(self):
        """Test adding two negative numbers."""
        self.assertEqual(add_numbers(-1, -4), -5)

if __name__ == "__main__":
    unittest.main()
