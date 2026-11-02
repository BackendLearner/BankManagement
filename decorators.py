
from functools import wraps
from typing import Any, Callable


def log_action(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:

        print(f"\n[LOG] Executing {func.__name__}")

        result = func(*args, **kwargs)

        print(f"[LOG] {func.__name__} completed successfully")

        return result

    return wrapper


def validate_amount(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:

        amount = kwargs.get("amount")

        if amount is None and len(args) > 1:
            amount = args[1]

        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise ValueError("Amount must be a valid number")

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        return func(*args, **kwargs)

    return wrapper
