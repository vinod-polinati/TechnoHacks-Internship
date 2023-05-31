class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount} successfully. New balance: {self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrawn {amount} successfully. New balance: {self.balance}"
        else:
            return "Insufficient balance."

# Create an instance of ATM
atm = ATM()

# Menu
while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        balance = atm.check_balance()
        print(f"Your balance is: {balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        result = atm.deposit(amount)
        print(result)
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        result = atm.withdraw(amount)
        print(result)
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

