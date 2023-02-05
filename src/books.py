import datetime
import os
import uuid

from src import constants

directory = os.path.dirname(__file__)

issued_book_path = os.path.join(directory, '/LMS/db/IssuedBook.txt')
books_db_path = os.path.join(directory, '/LMS/db/Books.txt')


class Books:
    def __init__(self, uname):
        self.book_list = list_of_books()
        self._username = uname

    def list_books(self):
        print("The books are present at the LMS")
        for book in list_of_books():
            print(book)

    def borrow_book(self, book_name):
        found = [book[0] == book_name for book in self.book_list]
        if found:
            issued_date = datetime.datetime.today()
            return_date = datetime.datetime.today() + datetime.timedelta(days=constants.NUMBER_OF_DAYS)
            with open(issued_book_path, "a+") as f:
                f.write(self._username + "," + book_name + "," + str(issued_date) + "," + str(return_date))
                f.write("\n")
            print(f"You have borrowed {book_name} and you have 15 days to read book. please return book on time!")

    def return_book(self, book_name, username):
        calculate_fine(username, book_name)
        update_issued_book_data(username, book_name)

    def search_by_title(self, book_name):
        for book in self.book_list:
            if book_name == book[0]:
                return True
        return False

    def add_book(self, book, author, copies, price):
        with open(books_db_path, "a+") as bf:
            bf.write("\n")
            bf.write(str(uuid.uuid4()) + "," + book + "," + author + "," + copies + "," + "€" + price)
            print(f"\n{book} successfully added to database")

    def delete_book(self, book_id):
        with open(books_db_path, "r+") as f:
            books = f.readlines()
            f.seek(0)
            for b in books:
                if book_id not in b:
                    f.write(b)
            f.truncate()
            print(f"\n{book_id} successfully deleted from the database")


def list_of_books():
    books = []
    with open(books_db_path, "r") as bf:
        book_list = bf.readlines()
        [books.append(split_books_by_newline(book)) for book in book_list]
        return books


split_books_by_newline = lambda x: x.replace('\n', '').split(',')


def fine_calc_decorator(func):
    def fine_function_wrapper(user, book):
        fine = func(user, book)
        if fine is None or fine == constants.FINE_ZERO:
            print(f"You have {fine} Euro fine !!! for the book {book}")
        else:
            print(f"You have {fine} Euro fine !!! :) please pay before returning {book}")

    return fine_function_wrapper


@fine_calc_decorator
def calculate_fine(user_name, book_name):
    with open(issued_book_path, "r") as f:
        book_list = f.readlines()
        for book in book_list:
            book_data = book.split(",")
            if book_data[0] == user_name.upper() and book_data[1] == book_name:
                book_data[3] = book_data[3].strip('\n')
                issued_date = datetime.datetime.strptime(book_data[2], constants.DATE_FORMAT_FOR_FINE_CALC)
                return_date = datetime.datetime.strptime(book_data[3], constants.DATE_FORMAT_FOR_FINE_CALC)
                fine = constants.NUMBER_OF_DAYS - abs(issued_date.day - return_date.day)
                money = constants.FINE_ZERO
                if fine < constants.FINE_ZERO:
                    money = abs(fine)
                return money


def update_issued_book_data(user_name, book_name):
    with open(issued_book_path, "r+") as f:
        books = f.readlines()
        f.seek(0)
        found = False
        for issued_book in books:
            if user_name in issued_book and book_name in issued_book:
                f.truncate()
                found = True
                print(f"\n{book_name} successfully returned to library")
            else:
                f.write(issued_book)
        if not found:
            print(f"\n Hey!! {user_name} No {book_name} has not been issued to you!!")
