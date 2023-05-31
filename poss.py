import string
import random
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
length = int(input("Enter password length: "))
password = generate_password(length)
print("Your random password is:", password)