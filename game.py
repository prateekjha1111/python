import random

print("Let's play rock, paper & scissors!")
def get_choices():
    player_choice = input("Enter a choice (rock / paper / scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player" : player_choice, "computer" : computer_choice}
    return choices

choice = get_choices()

def check_win(player, computer):
    if player == "rock":
        if computer == "rock":
            result = f"You chose {player}, computer chose {computer}. It's a tie."
            return result
        elif computer == "paper":
            result = f"You chose {player}, computer chose {computer}. You lose."
            return result
        else:
            result = f"You chose {player}, computer chose {computer}. You win!."
            return result
        
    if player == "paper":
        if computer == "rock":
            result = f"You chose {player}, computer chose {computer}. You win!."
            return result
        elif computer == "paper":
            result = f"You chose {player}, computer chose {computer}. It's a tie."
            return result
        else:
            result = f"You chose {player}, computer chose {computer}. You lose."
            return result
        
    if player == "scissors":
        if computer == "rock":
            result = f"You chose {player}, computer chose {computer}. You lose."
            return result
        elif computer == "paper":
            result = f"You chose {player}, computer chose {computer}. You win!."
            return result
        else:
            result = f"You chose {player}, computer chose {computer}. It's a tie."
            return result
        
print(check_win(choice["player"], choice["computer"]))