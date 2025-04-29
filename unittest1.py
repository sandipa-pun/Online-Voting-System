import unittest
from tkinter import Tk, Frame
from registerVoter import reg_server

class TestVoterRegistration(unittest.TestCase):
    def test_reg_server_valid_registration(self):
        root = Tk()
        frame1 = Frame(root)
        result = reg_server(root, frame1, "12345", "John Doe", "29", "Computing", "password", "password")
        self.assertEqual(result, None)

    def test_reg_server_missing_fields(self):
        root = Tk()
        frame1 = Frame(root)
        result = reg_server(root, frame1, "", "John Doe", "29", "Computing", "password", "password")
        self.assertEqual(result, -1)
        
    def test_reg_server_password_mismatch(self):
        root = Tk()
        frame1 = Frame(root)
        result = reg_server(root, frame1, "12345", "John Doe", "29", "Computing", "password", "different_password")
        self.assertEqual(result, -1)

if __name__ == "__main__":
    unittest.main()


