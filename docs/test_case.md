# Login Function Test Cases

## Test Case 1
- Test Case ID: TC_01
- Title: Valid login credentials
- Input: username=admin, password=admin123
- Expected Result: Login successful
- Actual Result: Login successful
- Status: Pass

## Test Case 2
- Test Case ID: TC_02
- Title: Login with valid username and password
- Input: username=admin, password=admin123
- Expected Result: Login successful
- Actual Result: Login successful
- Status: Pass

## Test Case 3
- Test Case ID: TC_03
- Title: Login with correct username
- Input: username=admin, password=admin123
- Expected Result: Login successful
- Actual Result: Login successful
- Status: Pass

## Test Case 4
- Test Case ID: TC_04
- Title: Login after retry
- Input: username=admin, password=admin123
- Expected Result: Login successful
- Actual Result: Login successful
- Status: Pass

## Test Case 5 (Negative)
- Test Case ID: TC_05
- Title: Login with incorrect password
- Input: username=admin, password=wrongpass
- Expected Result: Invalid credentials
- Actual Result: Invalid credentials
- Status: Pass

## Test Case 6 (Negative)
- Test Case ID: TC_06
- Title: Login with empty fields
- Input: username="", password=""
- Expected Result: Fields cannot be empty
- Actual Result: Fields cannot be empty
- Status: Pass
