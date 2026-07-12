# Password Generator
import random
length = int(input("Enter the length of the password: "))
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
password_characters = lowercase + uppercase + digits + special_characters
password = ""
for i in range(length):
    password += random.choice(password_characters)
print("Generated Password:", password)