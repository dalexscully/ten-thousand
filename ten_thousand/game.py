import sys

from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker
from helper_functions.helpers import dice_to_string, string_to_list


class Game:
    def __init__(self):
        self.round = 1
        self.bank = Banker()
        self.remaining_dice = 6
        self.current_dice_options = []

    def print_welcome_message(self):
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")

    def display_new_roll(self, roller):
        print(f"Rolling {self.remaining_dice} dice...")
        self.current_dice_options = roller(self.remaining_dice)
        new_dice_string = dice_to_string(self.current_dice_options)
        print(new_dice_string)

    def shelf_the_score(self, score):
        self.bank.shelf(score)
        print(f"You have {self.bank.shelved} unbanked points and {self.remaining_dice} dice remaining")

    def bank_the_score(self):
        banked = self.bank.bank()
        print(f"You banked {banked} points in round {self.round}")
        print(f"Total score is {self.bank.balance} points")

    def prepare_new_round(self):
        self.bank_the_score()
        self.round += 1
        self.remaining_dice = 6
        self.current_dice_options = []

    def print_cheater(self):
        print("Cheater!!! Or possibly made a typo...")
        dice_string = dice_to_string(self.current_dice_options)
        print(dice_string)

    def zilch(self):
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")
        self.bank.clear_shelf()
        self.prepare_new_round()

    def quit_game(self):
        print(f"Thanks for playing. You earned {self.bank.balance} points")
        sys.exit("Exiting")

    def play(self, roller=GameLogic.roll_dice):

        self.print_welcome_message()

        ask_user_to_play = input("> ")
        if ask_user_to_play == "n" or ask_user_to_play == "no":
            print("OK. Maybe another time")
            return

        playing = True
        while playing:

            print(f"Starting round {self.round}")

            same_round = True
            while same_round:

                self.display_new_roll(roller)

                if len(GameLogic.get_scorers(self.current_dice_options)) == 0:
                    self.zilch()
                    same_round = False
                    continue

                valid_pick = False
                while valid_pick == False:

                    try:

                        user_answer = input("Enter dice to keep, or (q)uit:\n> ")
                        user_answer = user_answer.replace(" ", "")
                        if user_answer == "q":
                            self.quit_game()
                        users_dice_picks = string_to_list(user_answer)

                    except ValueError as error:
                        self.print_cheater()

                    if GameLogic.validate_keepers(self.current_dice_options, users_dice_picks):
                        self.remaining_dice -= len(users_dice_picks)
                        current_score = GameLogic.calculate_score(tuple(users_dice_picks))
                        valid_pick = True
                    else:
                        self.print_cheater()

                if self.remaining_dice == 0:
                    self.shelf_the_score(current_score)
                    self.remaining_dice = 6
                    self.current_dice_options = []
                else:
                    self.shelf_the_score(current_score)

                ask_again = input("(r)oll again, (b)ank your points or (q)uit:\n> ")

                if ask_again == "r":
                    continue

                elif ask_again == "b":
                    self.prepare_new_round()
                    same_round = False

                elif ask_again == "q":
                    self.quit_game()


if __name__ == "__main__":

    try:
        game = Game()
        game.play()
    except KeyboardInterrupt:
        game.quit_game()