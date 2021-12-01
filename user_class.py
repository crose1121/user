class User():
    def __init__(self, name, wallet_balance, bank_balance):
        self.name = name
        self.wallet_balance = wallet_balance
        self.bank_balance = bank_balance

    def make_deposit(self,amount):
        if amount <= self.wallet_balance:
            self.wallet_balance -= amount
            self.bank_balance += amount
            return self
        else:
            print("Insufficient Funds")
    
    def make_withdrawal(self,amount):
        if self.bank_balance >= amount:
            self.bank_balance -= amount
            self.wallet_balance += amount
            return self
        else:
            print("Insufficient Funds")

    def transfer_money(self,other_user,amount):
        self.other_user = other_user
        self.amount = amount
        if self.bank_balance >= amount:
            self.bank_balance -= amount
            other_user.bank_balance += amount
            print("Your money has been transferred")
            return self
        else:
            print("Insufficient Funds!")


    def __str__(self):
        return (f"Your name: {self.name} \nWallet balance: {self.wallet_balance} \nBank balance: {self.bank_balance}")


user1 = User('Corey Rose', 4000,2500)
user2 = User('The Mountain', 2500,1000)
user3 = User('Eddard Stark', 3500,5000)

user1.make_deposit(1000).make_deposit(900).make_deposit(500).make_withdrawal(200)
print(user1)

user2.make_deposit(1000).make_deposit(900).make_withdrawal(500).make_withdrawal(200)
print(user2)

user3.make_deposit(2000).make_withdrawal(3000).make_withdrawal(2000).make_withdrawal(2000)
print(user3)

user1.transfer_money(user2,500)
print(user1)
print(user2)