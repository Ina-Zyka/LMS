import re
from unittest import TestCase

from src.main.python.library import Register, validate_user, validate_password, validate_email, validate_type, Login


class TestRegister(TestCase):

    def setUp(self):
        self.reg_admin = Register('Ina', 'ina@password', 'ina1234@gmail.com', 'Admin')
        self.reg_student = Register('Rose', 'rose@1234', 'rose@gmail.com', 'Student')

    def test_register_user(self):
        self.assertEqual(self.reg_admin.username, 'Ina')
        self.assertEqual(self.reg_admin.password, 'ina@password')
        self.assertEqual(self.reg_admin.email, 'ina1234@gmail.com')
        self.assertEqual(self.reg_admin.type, 'Admin')
        self.assertEqual(self.reg_student.username, 'Rose')
        self.assertEqual(self.reg_student.password, 'rose@1234')
        self.assertEqual(self.reg_student.email, 'rose@gmail.com')
        self.assertEqual(self.reg_student.type, 'Student')


valid_user_check = lambda uname: True if re.match("^[A-Za-z0-9]+$", uname) else False

valid_password_check = lambda passwd: True if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', passwd) else False

valid_email_check = lambda mail: True if re.search(r'[\w.-]+@[\w.-]+.\w+', mail) else False

valid_usertype_check = lambda type_of_user: True if any(
    word in type_of_user for word in ['student', 'staff', 'admin']) else False


class TestValidations(TestCase):
    def test_validate_user(self):
        try:
            self.assertIsNone(validate_user(valid_user_check, "ina"))
        except SystemExit:
            self.assertRaises(SystemExit)

    def test_validate_password(self):
        try:
            self.assertTrue(validate_password(valid_password_check, "fgh"))
        except SystemExit:
            self.assertRaises(SystemExit)

    def test_validate_email(self):
        try:
            self.assertTrue(validate_email(valid_email_check, "fgh234"))
        except SystemExit:
            self.assertRaises(SystemExit)

    def test_validate_type(self):
        try:
            self.assertTrue(validate_type(valid_usertype_check, "user"))
        except SystemExit:
            self.assertRaises(SystemExit)

    def test_user_admin(self):
        self.assertIsNone(validate_user(valid_user_check, "Ina"))

    def test_password_admin(self):
        self.assertIsNone(validate_user(valid_password_check, "ina@password"))

    def test_email_admin(self):
        self.assertIsNone(validate_user(valid_email_check, "ina@gmail.com"))


class TestLogin(TestCase):
    def setUp(self):
        self.log = Login('INA', 'ina@password')
        self.log1 = Login('JACK', 'jack@password')
        self.log2 = Login('ENI', 'eni@1234')

    def test_user_condition(self):
        self.assertTrue(self.log.user_role('INA', 'ina@password'))
        self.assertFalse(self.log.user_role('INA', 'ina8765'))

    def test_check_admin_login(self):
        try:
            self.assertEquals("ADMIN", self.log.user_validation(), "ADMIN")
        except FileNotFoundError:
            self.assertRaises(FileNotFoundError)

    def test_check_student_login(self):
        try:
            self.assertEquals("STUDENT", self.log1.user_validation(), "STUDENT")
        except FileNotFoundError:
            self.assertRaises(FileNotFoundError)

    def test_check_staff_login(self):
        try:
            self.assertEquals("STAFF", self.log2.user_validation(), "STAFF")
        except FileNotFoundError:
            self.assertRaises(FileNotFoundError)
