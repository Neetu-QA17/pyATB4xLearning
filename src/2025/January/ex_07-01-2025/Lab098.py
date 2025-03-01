# Custom Exception - own exception or user defined exception

class MyCustomException(Exception):
    def __init__(self, message):
        self.msg = message
        super().__init__(message)

balance = 100
withdraw = int(input("Enter the amount that user wants to withdraw!!"))
if withdraw > balance:
    raise MyCustomException("Insufficient Balance!!")
else:
    print("Remain Bal ", (balance-withdraw))


