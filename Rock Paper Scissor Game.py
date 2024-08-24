import random

def rock_paper_scissors():
    # Options for the game
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        # Player's move
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
        if player_choice == 'quit':
            break
        if player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        
        # Computer's move
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
        else:
            print("You lose!")
        
        print()  # Blank line for readability

# Run the game
rock_paper_scissors()
