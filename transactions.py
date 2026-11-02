
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:
    transaction_type: str
    amount: float
    timestamp: datetime

    def __str__(self) -> str:
        return (
            f"{self.transaction_type}: "
            f"Rs.{self.amount:.2f} "
            f"at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
        )
