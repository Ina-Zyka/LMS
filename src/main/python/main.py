from src.main.python import constants
from src.main.python.library import Login, validate_user, validate_password, validate_email, validate_type, Register, \
    valid_user_check, valid_password_check, valid_email_check, valid_usertype_check


def actions():
    while True:
        print("###################################\n")
        print("   Welcome to Library Management System (LMS) ")
        print("-------------------------------------------------\n")
        print(""" ======LMS MENU=======
    1. Sign in
    2. Register
    3. Exit""")

        option = int(input("Enter the choice 1 or 2 or 3:\n"))
        if option == constants.USER_OPTION_ONE:
            username = input("Enter the Username:\n")
            password = input("Enter the Password:\n")
            login = Login(username.upper(), password)
            login.login()
        elif option == constants.USER_OPTION_TWO:
            print("You have selected the option to Register to LMS")
            print("Please enter valid username, password, email and usertype[Admin, Student,Staff]")
            username = input("Username:\n")
            validate_user(valid_user_check, username)
            password = input("Password:\n")
            validate_password(valid_password_check, password)
            email = input("Email:\n")
            validate_email(valid_email_check, email)
            user_type = input("User Role:\n")
            validate_type(valid_usertype_check, user_type)
            register = Register(username, password, email, user_type)
            register.register_user()
        else:
            print("You decided to exit the LMS")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    actions()

