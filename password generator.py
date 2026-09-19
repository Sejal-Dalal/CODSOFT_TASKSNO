import random
import string

letters = int(input("Enter number of letters: "))
digits = int(input("Enter number of digits: "))
punctuation = int(input("Enter number of punctuation: "))

password = ""

for i in range(letters):
    password += random.choice(string.ascii_letters)

for i in range(digits):
    password += random.choice(string.digits)

for i in range(punctuation):
    password += random.choice(string.punctuation)

password = list(password)
random.shuffle(password)

password = "".join(password)

print("Generated Password:", password)