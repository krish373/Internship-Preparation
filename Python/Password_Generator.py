# Strong Password Generator with atleast one lowercase letter, one uppercase letter, one digit, and one special character in Python
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
if(any(char.islower() for char in password) and any(char.isupper() for char in password) and any(char.isdigit() for char in password) and any(char in special_characters for char in password)):
    print("Generated Password:", password)
else:
    print("Password does not meet the criteria. Please try again.")