import random

CHOICES = ["Rock", "Paper", "Scissors"]

def get_computer_choice():
    return random.choice(CHOICES)

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "TIE"
    
    if ( player_choice == "Rock" and computer_choice == "Scissors"
       or player_choice == "Scissors" and computer_choice == "Paper"
       or player_choice == "Paper" and computer_choice == "Rock"
    ):
        return "player"
    
    return "computer"