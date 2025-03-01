# Encapsulation

class Bank:
    def __init__(self, account_num, balance):
        self.balance = balance
        self.__account_num = account_num

    def deposit(self, amount):
        self.balance = self.balance + amount

    def check_balance(self):
        print(self.balance)

    def show_account_num(self, is_auth):
        if is_auth == True:
            print(self.__account_num)
        else:
            print("Not Allowed!")

obj = Bank(11234678987, 100)
obj.deposit(1000)
obj.check_balance()
obj.show_account_num(True)
