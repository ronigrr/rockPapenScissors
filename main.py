import game
import cvs_reader
import csv


def printHeadline():
    print("----------------------------------------------------------------------------")
    print("            Rock Paper Scissors and other things           ")
    print("----------------------------------------------------------------------------")


def get_players_name():
    print("Please enter your name\n")
    return input()


def run_game(player1, computer, rolls):
    count = 1
    p1_score = 0
    computer_score = 0
    while count <= 3:
        p1_roll = game.Rolls()
        p1_roll.chose_roll()
        print(f'{player1.name} chose {p1_roll.roll}')
        p2_roll = game.Rolls()
        p2_roll.auto_chose_roll()
        print(f'{computer.name} chose {p2_roll.roll}')

        outcome = p1_roll.can_defeat_from_cvs(p2_roll.roll)
        if outcome is None:
            print(" its a tie! Try again\n")
        elif outcome:
            print(f'{player1.name} wins wins this round')
            p1_score += 1
            count += 1
        else:
            print(f'{computer.name} wins this round')
            computer_score += 1
            count += 1
        print(f'score is {player1.name} {p1_score}-{computer_score} {computer.name}')

    if p1_score > computer_score:
        print(f'{player1.name} wins the game!')
    else:
        print(f'{computer.name} won this time :(')


def main():
    printHeadline()
    rolls = game.Rolls
    name = get_players_name()

    player1 = game.Player(name)
    player2 = game.Computer()
    run_game(player1, player2, rolls)


if __name__ == '__main__':
    main()


