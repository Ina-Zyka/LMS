from src.books import Books, calculate_fine
from src import constants


class User:
    def __init__(self, username, access_type):
        self._username = username
        self._access_type = access_type
        self.b1 = Books(self._username)

    def student_staff_actions(self):
        while True:
            print("Please choose an option:")
            print("1", "display_books")
            print("2", "search book By book_Name")
            print("3", "borrow_book")
            print("4", "return book")
            print("5", "pay fine")
            print("Press any number for exit")
            student_staff_decision = input("Enter your choice \n")
            if student_staff_decision not in ["1", "2", "3", "4", "5"]:
                print("You have selected different choice and logging out from the system")
                exit()
            else:
                student_staff_decision = int(student_staff_decision)
                self.user_choice(self.b1, student_staff_decision)

    def user_choice(self, b1, user_choice):
        if user_choice == constants.USER_OPTION_ONE:
            b1.list_books()
            print("\n")

        elif user_choice == constants.USER_OPTION_TWO:
            book_name = input("Enter the name of book: ")
            if b1.search_by_title(book_name):
                print(f"\n The Book {book_name} is found !! \n")
            else:
                print(f"\nThe Book {book_name} your searching is not found !! give it another short\n")

        elif user_choice == constants.USER_OPTION_THREE:
            book = input("please Enter the name of the book you want to borrow :")
            b1.borrow_book(book)
            print("\n")

        elif user_choice == constants.USER_OPTION_FOUR:
            book = input("please Enter the name of the book you want to return :")
            user = input("please enter your name:")
            b1.return_book(book, user.upper())
            print("\n")

        elif user_choice == constants.USER_OPTION_FIVE:
            book = input("please Enter the name of the book having fine :")
            calculate_fine(self._username, book)

    def admin_actions(self):
        while True:
            print("Let's do some actions as admin!!")
            print("1", "Display a book")
            print("2", "Add a book")
            print("3", "Remove a book")
            print("Press any number for exit")
            admin_choice = int(input("Enter your choice \n"))
            if admin_choice == constants.USER_OPTION_ONE:
                self.b1.list_books()
                print("\n")

            elif admin_choice == constants.USER_OPTION_TWO:
                book_name = input("Enter the name of book : ")
                author = input("Enter the author name :  ")
                numbers = input("Enter the number of copies :  ")
                price = input("Enter the price of the book : ")
                self.b1.add_book(book_name, author, numbers, price)

            elif admin_choice == constants.USER_OPTION_THREE:
                book_id = input("please Enter the id of the book you want to delete :")
                self.b1.delete_book(book_id)
                print("\n")

            else:
                exit()
