import random
from getpass import getpass
from time import time
import os
import gameInterface

def get_player_choice(self):
        """ Obtient et retourne le choix du joueur. """

        try:
            # Masquer la saisie (notez que cela peut ne pas fonctionner dans tous les environnements)
            return getpass.getpass(prompt="Type your choice (rock, paper, scissors): ").lower()
        except Exception:
            # Repli sur l'entrée standard en cas d'erreur avec getpass
            return input("Type your choice (rock, paper, scissors): ").lower()

def display_message(self, message):
        """ Affiche un message à l'utilisateur. """
        print(message)

our_choice = ["rock", "paper", "scissors"]

def good_response(response):
    return response in our_choice

def winner_responses(first_response, second_response):
    if first_response == "rock" and second_response == "scissors":
        return True
    elif first_response == "paper" and second_response == "rock":
        return True
    elif first_response == "scissors" and second_response == "paper":
        return True
    return False

def anime(first_response, second_response):
    return first_response == second_response

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    clear_screen()
    game_interface = game_interface()
    game_interface.display_message("\033[0;32m### Rock Paper Scissors Game ###\033[0m")

    running = True
    while running:
        player_proposition = game_interface.get_player_choice()

        while not good_response(player_proposition):
            game_interface.display_message("Not a valid option, expecting: rock, paper, or scissors")
            player_proposition = game_interface.get_player_choice()

        game_interface.display_message(f"You chose: {player_proposition}")
        time.sleep(0.5)
        game_interface.display_message("Computer is thinking...")
        time.sleep(1)
        pc_response = random.choice(our_choice)
        game_interface.display_message(f"Computer chose: {pc_response}\n")

        if anime(player_proposition, pc_response):
            game_interface.display_message("IT'S A TIE!!!")
        elif winner_responses(player_proposition, pc_response):
            game_interface.display_message(f"{player_proposition} beats {pc_response}\nYOU WIN!!!")
        else:
            game_interface.display_message(f"{pc_response} beats {player_proposition}\nYOU LOSE!")
            running = False

    game_interface.display_message("Have a good day")

if __name__ == "__main__":
    main()