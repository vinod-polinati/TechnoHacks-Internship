# _TechnoHacksOfficial_ _Internship_

## ATM Class
The `ATM` class represents a simple ATM machine. It allows users to check their balance, deposit money, and withdraw money.

```python
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
```
## Basic Calculator
The `Basic Calculator` code allows users to perform arithmetic operations such as addition, subtraction, multiplication, and division.

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

print("Basic Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter operation (1/2/3/4): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input!")
```
## Random Password Generator
The `RPG` code generates a random password of a specified length using a combination of letters (uppercase and lowercase), digits, and special characters.
```python
import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
```
## Rock, Paper, Scissors Game
The `Rock, Paper, Scissors` game allows users to play against the computer. It determines the winner based on the choices made by the user and the computer.
```python
import random

choices = ["rock", "paper", "scissors"]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win...!"
    else:
        return "Computer wins!"
```
## To-do List Manager
The `to-do list manager` allows users to manage a list of tasks. It provides options to display the to-do list, add items, remove items, and clear the entire list.
```python
todo_list = []

def display_todo_list():
    print("To-do List:")
    for i, item in enumerate(todo_list):
        print(f"{i+1}. {item}")
    print()

def add_todo_item():
    item = input("Enter a new item to add to the to-do list: ")
    todo_list.append(item)
    print(f"{item} has been added to the to-do list.\n")

def remove_todo_item():
    display_todo_list()
    item_num = input("Enter the number of the item to remove: ")
    try:
        item_num = int(item_num)
        item = todo_list[item_num - 1]
        todo_list.pop(item_num - 1)
        print(f"{item} has been removed from the to-do list.\n")
    except (ValueError, IndexError):
        print("Invalid item number. Please try again.\n")

def clear_todo_list():
    todo_list.clear()
    print("To-do list
```
