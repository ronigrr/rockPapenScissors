import random
import csv
import cvs_reader
from os import system


class Player:
    def __init__(self, name):
        self.name = name


class Computer(Player):
    def __init__(self):
        super().__init__(self)
        self.name = "computer"


class Rolls:
    def __init__(self):
        self.roll = None
        self.all_rolls = self.get_rolls()

    def print_chose_menu(self):

        text = "Chose: "
        for roll in self.all_rolls:
            if roll[0] == 'D':
                text += f"[{roll[:2]}]{roll[2:]} "
            else:
                text += f"[{roll[0]}]{roll[1:]} "
        print(text)

    def chose_roll(self):
        self.print_chose_menu()
        user_input = input().upper()
        if user_input == 'D':
            print("Sorry what you chose is not in the game, try again\n")
            self.chose_roll()
        elif user_input == 'DE':
            self.roll = "Devil"
            return "Devil"
        elif user_input == "DR":
            self.roll = "Dragon"
            return "Dragon"
        else:
            for roll in self.all_rolls:
                if roll[0].upper() == user_input:
                    self.roll = roll
                    return roll
                else:
                    print("Sorry what you chose is not in the game, try again\n")
                    self.chose_roll()

    def auto_chose_roll(self):
        roll = random.choice(self.all_rolls)
        self.roll = roll
        return random.choice(self.all_rolls)

    def can_defeat_from_cvs(self, second_roll):
        current_dict = self.read_rolls(self.roll)
        return self.check_if_can_defeat(current_dict, second_roll)

    @staticmethod
    def read_rolls(roll_to_read):
        with open('battle-table.csv') as fin:
            reader = csv.DictReader(fin)
            for row in reader:
                if row['Attacker'].__str__() == roll_to_read:
                    return row

    @staticmethod
    def check_if_can_defeat(current_dict, second_roll):
        win_lose_tie = current_dict[second_roll]
        if win_lose_tie == 'win':
            return True
        elif win_lose_tie == 'lose':
            return False
        else:
            return None

    @staticmethod
    def get_rolls():
        rolls = []
        with open('battle-table.csv') as fin:
            reader = csv.DictReader(fin)
            for row in reader:
                rolls.append(row['Attacker'])
        return rolls
