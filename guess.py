from random import randint
from art import logo

print(logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def game():
    def check_ans(guess,ans,turns):
        """Check answer against guess. Return the no. of turns remaining."""
        if guess>ans:
            print("Too High")
            return turns-1
        elif guess<ans:
            print("Too Low")
            return turns-1
        else:
            print(f"You got it! The ans was {ans}.")


    def set_difficulty():
        
        level = input("Choose a difficulty. Type 'easy' or 'hard': " )
        if level == "easy":
            return EASY_LEVEL_TURNS
        else:
            return HARD_LEVEL_TURNS
            
            

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 to 100.")

    ans = randint(1,100)
    turns = set_difficulty()
    guess = 0

    while guess != ans:
        print(f"You have {turns} attempts remaining to guess the number.")
        
        guess = int(input("Make your guess: "))
        turns = check_ans(guess,ans,turns)  
        if turns == 0 :
            print("You lose!")
            return
        elif guess != ans:
            print("Guess Again")

game()