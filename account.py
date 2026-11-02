
from abc import ABC, abstractmethod
from typing import Iterator

from transactions import Transaction
from decorators import log_action, validate_amount


class BankAccount(ABC):

    def __init__(
        self,
        account_holder: str,
        account_number: int,
        balance: float = 0.0
    ) -> None:

        if not isinstance(balance, (int, float)) or isinstance(balance, bool):
            raise ValueError("Invalid initial balance")

        if balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self.account_holder: str = account_holder
        self.account_number: int = account_number

        # Encapsulation
        self.__balance: float = float(balance)

        self.transactions: list[Transaction] = []

    # Property decorator
    @property
    def balance(self) -> float:
        return self.__balance

    # Deposit method
    @log_action
    @validate_amount
    def deposit(self, amount: float) -> None:

        self.__balance += amount

        transaction = Transaction(
            "Deposit",
            amount,
            __import__("datetime").datetime.now()
        )

        self.transactions.append(transaction)

        print(f"Rs.{amount} deposited successfully!")

    # Abstract method
    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass

    # Helper method
    def _deduct(self, amount: float) -> None:
        self.__balance -= amount

        transaction = Transaction(
            "Withdrawal",
            amount,
            __import__("datetime").datetime.now()
        )

        self.transactions.append(transaction)

    # Special method: __str__
    def __str__(self) -> str:
        return (
            f"Account Holder: {self.account_holder}\n"
            f"Account Number: {self.account_number}\n"
            f"Balance: Rs.{self.balance:.2f}"
        )

    # Special method: __repr__
    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(account_holder={self.account_holder!r}, "
            f"account_number={self.account_number!r}, "
            f"balance={self.balance!r})"
        )

    # Special method: __len__
    def __len__(self) -> int:
        return len(self.transactions)

    # Special method: __iter__
    def __iter__(self) -> Iterator[Transaction]:
        return iter(self.transactions)

    # Special method: __eq__
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BankAccount):
            return NotImplemented

        return self.account_number == other.account_number

    # Special method: __add__
    def __add__(self, other: "BankAccount") -> float:
        return self.balance + other.balance


# Inheritance
class SavingsAccount(BankAccount):

    def __init__(
        self,
        account_holder: str,
        account_number: int,
        balance: float = 0.0,
        interest_rate: float = 4.0
    ) -> None:

        super().__init__(
            account_holder,
            account_number,
            balance
        )

        self.interest_rate = interest_rate

    # Polymorphism
    @log_action
    @validate_amount
    def withdraw(self, amount: float) -> None:

        if amount > self.balance:
            raise ValueError("Insufficient balance!")

        self._deduct(amount)

        print(f"Rs.{amount} withdrawn successfully!")


# Another child class
class CurrentAccount(BankAccount):

    def __init__(
        self,
        account_holder: str,
        account_number: int,
        balance: float = 0.0,
        overdraft_limit: float = 5000.0
    ) -> None:

        super().__init__(
            account_holder,
            account_number,
            balance
        )

        if overdraft_limit < 0:
            raise ValueError("Overdraft limit cannot be negative")

        self.overdraft_limit = overdraft_limit

    # Different withdrawal implementation
    @log_action
    @validate_amount
    def withdraw(self, amount: float) -> None:

        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded!")

        self._deduct(amount)

        print(f"Rs.{amount} withdrawn successfully!")
