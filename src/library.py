import re
import os
from src.users import User
from src.errors import InvalidUserException, InvalidPasswordException, InvalidEmailException, \
    InvalidTypeException

directory = os.path.dirname(__file__)
user_db_path = os.path.join(directory, '/LMS/db/UserData.txt')


class Login:

    def __init__(self, uname, passwd):
        self.username = uname
        self.password = passwd

    def user_role(self, uname, passwd):
        return True if uname == self.username and passwd == self.password else False

    def login(self):
        access_type = self.user_validation()
        user = User(self.username, access_type)
        if access_type.upper() == 'ADMIN':
            print(f" {self.username}  Successfully logged In as {access_type}!!\n")
            user.admin_actions()
        elif access_type.upper() == 'STAFF' or access_type.upper() == 'STUDENT':
            print(f" {self.username}  Successfully logged In as {access_type} !!\n")
            user.student_staff_actions()
        else:
            print(f"login failed for {self.username} \n")
            exit()

    def user_validation(self):
        with open(user_db_path, "r") as f:
            content = f.read().splitlines()
            for line in content:
                if len(line) != 0:
                    words = line.split(",")
                    user_username_pass_check = self.user_role
                    if user_username_pass_check(words[0], words[1]):
                        return words[3]
        return "None"


class Register:
    def __init__(self, uname, passwd, mail, type_of_user):
        self.username = uname
        self.password = passwd
        self.email = mail
        self.type = type_of_user

    def register_user(self):
        with open(user_db_path, "a") as f:
            f.write("\n")
            caps_username, caps_type = map(lambda x: x.upper(), [self.username, self.type])
            f.write(caps_username + "," + self.password + "," + self.email + "," + caps_type)
            print(f" {self.username} Successfully Registered in as {self.type}!!! ")


valid_user_check = lambda uname: True if re.match("^\w+$", uname) else False

valid_password_check = lambda passwd: True if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', passwd) else False

valid_email_check = lambda mail: True if re.search(r'[\w.-]+@[\w.-]+.\w+', mail) else False

valid_usertype_check = lambda type_of_user: True if any(
    word in type_of_user for word in ['Student', 'Staff', 'Admin']) else False


def validate_user(reg_func_user_check, u_name):
    try:
        if not reg_func_user_check(u_name):
            raise InvalidUserException("Invalid user")
    except InvalidUserException:
        print(f"You entered invalid username {str(u_name)}")
        exit()


def validate_password(reg_func_password_check, password):
    try:
        if not reg_func_password_check(password):
            raise InvalidPasswordException("Invalid password")
    except InvalidPasswordException:
        print(f"You entered invalid password {str(password)} and it should contain at least 8 chars")
        exit()


def validate_email(reg_func_email_check, email):
    try:
        if not reg_func_email_check(email):
            raise InvalidEmailException("Invalid email")
    except InvalidEmailException:
        print(f"You entered invalid email format {str(email)}")
        exit()


def validate_type(reg_func_user_type_check, user_ty):
    try:
        if not reg_func_user_type_check(user_ty):
            raise InvalidTypeException("Invalid usertype")
    except InvalidTypeException:
        print(f"Please enter valid user type {str(user_ty)}")
        exit()
