import sys
sys.path.append("../../src")
from login import login

def test_valid_login():
    assert login("admin", "admin123") == "Login successful"

def test_invalid_password():
    assert login("admin", "wrong") == "Invalid credentials"

def test_empty_username():
    assert login("", "admin123") == "Fields cannot be empty"

def test_empty_password():
    assert login("admin", "") == "Fields cannot be empty"
