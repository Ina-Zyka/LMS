from unittest import TestCase
from src.main.python.books import Books


class TestBooks(TestCase):

    def test_display_books(self):
        try:
            self.bk = Books('Test')
            self.bk.list_books()
        except FileNotFoundError:
            self.assertRaises(FileNotFoundError)
