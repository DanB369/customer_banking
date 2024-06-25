"""Import the Account class from the Account.py file."""
import Account as Ac
   
    
def create_cd_account(balance, interest_rate, months):
   
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    my_cd_account = Ac.Account(balance, interest_rate, months)


    # Calculate interest earned
    calculate_interest = balance * interest_rate * months
    interest_rate = calculate_interest

    # Update the CD account balance by adding the interest earned
    cd_updated_balance = balance + calculate_interest
    balance = cd_updated_balance

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    my_cd_account.set_balance(balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    my_cd_account.set_interest(interest_rate)

    # Return the updated balance and interest earned.
    return cd_updated_balance, calculate_interest
