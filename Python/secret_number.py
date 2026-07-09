import random
secret_number =  random.randint(1, 10)


User_Guess = int(input("enter a number:"))

while User_Guess != secret_number:
    User_Guess = int(input("Enter a number:"))
else:
    print("Secret Number is:", secret_number)