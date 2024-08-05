import random

def rockPaperScissors(user_input, comp):
    # draws
    if user_input == comp:
        print(f"The computer chose {comp}. {user_input} versus {comp}, ends in a draw.")
    # Comp wins
    elif (user_input == "rock" and comp == "paper") or (user_input == "paper" and comp == "scissors") or (user_input == "scissors" and comp == "rock"):
        print(f"The computer chose {comp}. {user_input} versus {comp}, computer wins.")
    # User wins
    else:
        print(f"The computer chose {comp}. {user_input} versus {comp}, you win!")

def main():
    options = ["rock", "paper", "scissors"]
    comp = random.choice(options)
    user_input = input("Enter rock, paper, or scissors: ").lower()
    
    if user_input not in options:
        print("Invalid input! Please enter rock, paper, or scissors.")
    else:
        rockPaperScissors(user_input, comp)

if __name__ == "__main__":
    main()
