import sys
sys.path.append("../../src")
from login import login

def test_login_flow():
    result = login("admin", "admin123")
    assert result == "Login successful"
