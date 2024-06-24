""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest

class SavingsAccount(Account):
    """Creating a SavingsAccount class that inherits from the Account class"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method calculates the interest earned.
    def calculate_interest(self, interest):
        """Calculates the interest earned"""
        return interest

class CDAccount(Account):
    """Creating a CDAccount class that inherits from the Account class"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest    

    # This method calculates the interest earned.
    def calculate_interest(self, interest):
        """Calculates the interest earned"""
        return interest