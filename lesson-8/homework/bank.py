import json
import random

class Account:
    
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        elif amount <= 0:
            return "Invalid withdrawal amount."
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

    def to_dict(self):
        return {"account_number": self.account_number, "name": self.name, "balance": self.balance}


class Bank:
    
    FILE_NAME = "accounts.json"

    def __init__(self):
        self.accounts = self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = random.randint(10000, 99999)
        while account_number in self.accounts:
            account_number = random.randint(10000, 99999)

        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        return f"Account created! Account Number: {account_number}"

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return f"Account {account_number}: {account.name}, Balance: ${account.balance}"
        return "Account not found."

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            result = account.deposit(amount)
            self.save_to_file()
            return result
        return "Account not found."

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            result = account.withdraw(amount)
            self.save_to_file()
            return result
        return "Account not found."

    def save_to_file(self):
        with open(self.FILE_NAME, "w") as file:
            json.dump({acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}, file)

    def load_from_file(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)
                return {int(acc_num): Account(int(acc_num), info["name"], info["balance"]) for acc_num, info in data.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

bank = Bank()
print(bank.create_account("Alice", 1000))

print(bank.view_account(10000)) 

print(bank.deposit(10000, 500)) 

print(bank.withdraw(10000, 200))