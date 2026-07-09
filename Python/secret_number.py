import random
secret_number =  random.randint(1, 10)


User_Guess = int(input("enter a number:"))

while User_Guess != secret_number:
    if User_Guess > secret_number:
        print("Too high")
    elif User_Guess < secret_number:
        print("Too low")
    User_Guess = int(input("Enter a number:"))
else:
    print("Secret Number is:", User_Guess)