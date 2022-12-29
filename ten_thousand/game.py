import sys

from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker


class Game:
    def __init__(self):
        self.round = 1
        self.bank = Banker()
        self.remaining_dice = 6
        self.current_dice_options = []

    def welcome_greeting(self):
        print('Welcome to ten Ten Thousand')
        print("(y)es to play or (n)o to decline")

    def new_roll(self, roller):
        print(f"Rolling {self.remaining_dice} dice...")
        self.current_dice_options = roller(self.remaining_dice)
        new_dice_string = self.dice_to_string(self.current_dice_options)
        print(new_dice_string)

    def shelf_score(self, score):
        self.bank.shelf(score)
        print(f"You have {self.bank.shelved} unbanked points and {self.remaining_dice} dice remaining")

    def bank_score(self):
        banked = self.bank.bank()
        print(f"You banked {banked} points in round {self.round}")
        print(f"Total score is {self.bank.balance} points")

    def prepare_new_round(self):
        self.bank_score()
        self.round += 1
        self.remaining_dice = 6
        self.current_dice_options = []

    def quit_game(self):
        print(f"Thanks for playing. You earned {self.bank.balance} points")
        sys.exit("Exiting")

    def dice_to_string(self, tuple):
        string = "*** "
        for dice in tuple:
            string += f"{dice} "
        string += "***"
        return string

    def string_to_list(self, string):
        num_string_list = [char for char in string]
        return [int(val) for val in num_string_list]

    def play(self, roller=GameLogic.roll_dice):

        self.welcome_greeting()

        play_game = input("> ")
        if play_game == "n" or play_game == "no":
            print("OK. Maybe another time")
            return

        playing = True
        while playing:

            print(f"Starting round {self.round}")

            same_round = True
            while same_round:

                self.new_roll(roller)

                user_answer = input("Enter dice to keep, or (q)uit:\n> ")
                user_answer = user_answer.replace(" ", "")
                if user_answer == "q":
                    self.quit_game()
                users_dice_picks = self.string_to_list(user_answer)

                if GameLogic.validate_keepers(self.current_dice_options, users_dice_picks):
                    self.remaining_dice -= len(users_dice_picks)
                current_score = GameLogic.calculate_score(tuple(users_dice_picks))

                if self.remaining_dice == 0:
                    self.shelf_score(current_score)
                    self.remaining_dice = 6
                    self.current_dice_options = []
                else:
                    self.shelf_score(current_score)

                ask_again = input("(r)oll again, (b)ank your points or (q)uit:\n> ")

                if ask_again == "r":
                    continue

                elif ask_again == "b":
                    self.prepare_new_round()
                    same_round = False

                elif ask_again == "q":
                    self.quit_game()


if __name__ == "__main__":
    game = Game()
    game.play()
