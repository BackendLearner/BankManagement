
from account import BankAccount, SavingsAccount, CurrentAccount


class Bank:

    def __init__(self, bank_name: str) -> None:
        self.bank_name = bank_name
        self.accounts: dict[int, BankAccount] = {}

    def create_savings_account(
        self,
        name: str,
        account_number: int,
        balance: float = 0.0
    ) -> None:

        if account_number in self.accounts:
            raise ValueError("Account already exists!")

        account = SavingsAccount(
            name,
            account_number,
            balance
        )

        self.accounts[account_number] = account

        print("Savings account created successfully!")

    def create_current_account(
        self,
        name: str,
        account_number: int,
        balance: float = 0.0
    ) -> None:

        if account_number in self.accounts:
            raise ValueError("Account already exists!")

        account = CurrentAccount(
            name,
            account_number,
            balance
        )

        self.accounts[account_number] = account

        print("Current account created successfully!")

    def get_account(self, account_number: int) -> BankAccount:

        account = self.accounts.get(account_number)

        if account is None:
            raise ValueError("Account not found!")

        return account

    def transfer(
        self,
        sender_number: int,
        receiver_number: int,
        amount: float
    ) -> None:

        if amount <= 0:
            raise ValueError("Transfer amount must be positive")

        if sender_number == receiver_number:
            raise ValueError("Cannot transfer to the same account")

        sender = self.get_account(sender_number)
        receiver = self.get_account(receiver_number)

        # Withdraw from sender
        sender.withdraw(amount)

        # Deposit into receiver
        receiver.deposit(amount)

        print("\nTransfer completed successfully!")

    def display_all_accounts(self) -> None:

        if not self.accounts:
            print("No accounts available!")
            return

        for account in self.accounts.values():
            print("-" * 35)
            print(account)

    def show_transaction_history(self, account_number: int) -> None:

        account = self.get_account(account_number)

        print("\nTransaction History:")

        if len(account) == 0:
            print("No transactions found!")
            return

        for transaction in account:
            print(transaction)
