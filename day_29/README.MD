🧠 Concepts Used
try
except
else
finally
raise
Custom Exceptions
ValueError
while loop
User input

⚙️ Features
Check balance
Deposit money
Withdraw money
Validate transaction amounts
Handle invalid menu choices
Handle insufficient balance
Custom InsufficientBalanceError
Continue running after errors
🔐 Custom Exception

The program creates a custom exception:

class InsufficientBalanceError(Exception):
    pass