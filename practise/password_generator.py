import random
import string

length = int(input("Enter password length: "))

chars = string.ascii_letters + string.digits + string.punctuation
password = ""

for i in range(length):
    password += random.choice(chars)

print("Generated Password:", password)
