
from bank import Bank


def main() -> None:

    bank = Bank("Python Banking System")

    while True:

        print("\n========== BANK MANAGEMENT SYSTEM ==========")

        print("1. Create Savings Account")
        print("2. Create Current Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Balance")
        print("6. Transfer Money")
        print("7. View Transaction History")
        print("8. Display All Accounts")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        try:

            if choice == "1":

                name = input("Enter account holder name: ")
                number = int(input("Enter account number: "))
                balance = float(input("Enter initial balance: "))

                bank.create_savings_account(
                    name,
                    number,
                    balance
                )

            elif choice == "2":

                name = input("Enter account holder name: ")
                number = int(input("Enter account number: "))
                balance = float(input("Enter initial balance: "))

                bank.create_current_account(
                    name,
                    number,
                    balance
                )

            elif choice == "3":

                number = int(input("Enter account number: "))
                amount = float(input("Enter deposit amount: "))

                account = bank.get_account(number)
                account.deposit(amount)

            elif choice == "4":

                number = int(input("Enter account number: "))
                amount = float(input("Enter withdrawal amount: "))

                account = bank.get_account(number)
                account.withdraw(amount)

            elif choice == "5":

                number = int(input("Enter account number: "))

                account = bank.get_account(number)

                print(f"\nCurrent Balance: Rs.{account.balance:.2f}")

            elif choice == "6":

                sender = int(input("Enter sender account number: "))
                receiver = int(input("Enter receiver account number: "))
                amount = float(input("Enter transfer amount: "))

                bank.transfer(sender, receiver, amount)

            elif choice == "7":

                number = int(input("Enter account number: "))

                bank.show_transaction_history(number)

            elif choice == "8":

                bank.display_all_accounts()

            elif choice == "9":

                print("Thank you for using our banking system!")
                break

            else:

                print("Invalid choice! Please try again.")

        except (ValueError, TypeError) as error:

            print(f"Error: {error}")

        except Exception as error:

            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
