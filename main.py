import random

# This is just the gameloop, will continue if you type y but end if you type n
def gameLoop():
    loop = True
    while(loop):
        # I put the random selection inside the loop because if it was outside, then the
        # computers choice would've been fixed
        computerChoice = random.randint(1,3)
        print("Enter your choice:\n 1 - Rock\n 2 - Paper\n 3 - Scissors\n\n")
        while(True):
            try:
                choice = int(input("Enter your choice: "))
                if choice not in [1,2,3]:
                    raise ValueError("Invalid choice. Please try again!\n")
                break
            # I still have zero idea on why we do ValueError instead of anything else
            except ValueError as e:
                print(f"Error: {e}")
        print("Now it's computer's turn...\n")
        if computerChoice == 1:
            print("Computer chose rock!\n")
        elif computerChoice == 2:
            print("Computer chose paper!\n")
        elif computerChoice == 3:
            print("Computer chose scissors!\n")
        
        # I think I could've just put this stuff in another function to do
        # Or there was a better solution, but this is the best I've got for now.
        if choice == 1:
            if computerChoice == 1:
                print("<== It's a tie ==>")
            elif computerChoice == 2:
                print("<== Computer wins! ==>")
            elif computerChoice == 3:
                print("<== Player wins! ==>")
        elif choice == 2:
            if computerChoice == 1:
                print("<== Player wins! ==>")
            elif computerChoice == 2:
                print("<== It's a tie! ==>")
            elif computerChoice == 3:
                print("<== Computer wins! ==>")
        elif choice == 3:
            if computerChoice == 1:
                print("<== Computer wins! ==>")
            elif computerChoice == 2:
                print("<== Player wins! ==>")
            elif computerChoice == 3:
                print("<== It's a tie! ==>")
        while(True):
            try:
                loopChoice = input("Do you want to play again? (Y/N)\n").upper()
                if loopChoice not in ['Y', 'N']:
                    raise ValueError("Invalid input. Please enter 'Y' for Yes or 'N' for No.\n")
                break
            except ValueError as e:
                print(f"Error: {e}")

        if loopChoice == "N":
            print("\nThanks for playing!")
            break
        elif loopChoice == "Y":
            print("\n")
            continue
def main():
    print("Winning rules of the game ROCK PAPER SCISSORS are:\n")
    print("Rock vs Paper -> Paper \nRock vs Scissors -> Rock\nPaper vs Scissors -> Papper\n\n")
    gameLoop()
if __name__ == '__main__':
    main()