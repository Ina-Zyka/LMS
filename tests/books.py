import unittest
from unittest import TestCase
from src.books import Books


class TestBooks(TestCase):

    def test_display_books(self):
        try:
            self.bk = Books('Test')
            self.bk.list_books()
        except FileNotFoundError:
            self.assertRaises(FileNotFoundError)


if __name__ == '__main__':
    unittest.main()
