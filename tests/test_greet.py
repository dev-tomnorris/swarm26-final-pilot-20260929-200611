import unittest

from greet import greet


class GreetTests(unittest.TestCase):
    def test_greet_uses_welcome(self) -> None:
        self.assertEqual(greet("Waggle"), "Welcome, Waggle!")


if __name__ == "__main__":
    unittest.main()
