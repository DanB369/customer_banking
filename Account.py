""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest, months=12):
        self.balance = balance
        self.interest = interest
        self.months = months

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest

# def calculate_interest(self, balance, interest, months):
#     return self.balance * self.interest * self.months

class SavingsAccount(Account):
    pass

    def __init__(self, balance, interest, months=12):
        super().__init__(balance, interest, months)

class CDAccount(Account):
    def __init__(self, balance, interest, months=12):
        super().__init__(balance, interest, months)
