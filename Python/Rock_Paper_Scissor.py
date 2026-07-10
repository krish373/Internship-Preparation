import random

Comp = random.choice(["Rock", "Paper", "Scissors"])
User = input("Enter your choice (Rock, Paper, Scissors): ") 

print("User choice:", User)
print("Computer choice:", Comp)

if(Comp == User):
    print("It's a tie")
elif(Comp == "Rock" and User == "Scissors"):
    print("Computer wins")
elif(Comp == "Scissors" and User == "Paper"):
    print("Computer wins")
elif(Comp == "Paper" and User == "Rock"):
    print("Computer wins")
elif(User == "Rock" and Comp == "Scissors"):
    print("User wins")
elif(User == "Scissors" and Comp == "Paper"):
    print("User wins")
elif(User == "Paper" and Comp == "Rock"):
    print("User wins")  


