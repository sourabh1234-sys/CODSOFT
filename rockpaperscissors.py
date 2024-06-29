import random

print("Welcome to Rock-Paper-Scissors!")
print("-------------------------------")
print("Enter 'rock', 'paper', or 'scissors' to play.")
print("Enter 'quit' to exit the game.")
print("-------------------------------")

while True:
    userchoic = input("Enter your choice: ").lower()

    if userchoic == "quit":
        print("Thanks for playing")
        break

    if userchoic not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
        continue

    computerchoice = random.choice(["rock", "paper", "scissors"])

    print(f"\nYou chose: {userchoic}")
    print(f"Computer chose: {computerchoice}")

    if userchoic == computerchoice:
        print("It's a tie!")
    elif (userchoic == "rock" and computerchoice == "scissors") or \
         (userchoic == "scissors" and computerchoice == "paper") or \
         (userchoic == "paper" and computerchoice == "rock"):
        print("You win!")
    else:
        print("Computer wins!")

    print("-------------------------------")
    playagain = input("Play again? (yes/no): ")
    if playagain.lower() != "yes":
        print("Thanks for playing")
        break