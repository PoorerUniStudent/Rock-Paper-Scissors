import random

def gameLoop():
    loop = True
    while(loop):
        computerChoice = random.randint(1,3)
        print("Enter your choice:\n 1 - Rock\n 2 - Paper\n 3 - Scissors\n\n")
        while(True):
            try:
                choice = int(input("Enter your choice: "))
                if choice not in [1,2,3]:
                    raise ValueError("Invalid choice. Please try again!\n")
                break
            except ValueError as e:
                print(f"Error: {e}")
        print("Now it's computer's turn...\n")
        if computerChoice == 1:
            print("Computer chose rock!\n")
        elif computerChoice == 2:
            print("Computer chose paper!\n")
        elif computerChoice == 3:
            print("Computer chose scissors!\n")
        
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