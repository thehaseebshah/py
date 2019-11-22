# Classes


class Player:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def change_name(self, n):
        self.name = n

    def change_age(self, a):
        self.age = a


# Driver Code

from Games import hangman
from Games import rock_paper_scissors
from Games import tic_tac_toe

print()
print()
print("Welcome to Game Pack!")
nm = input("Please enter your name: ")
ag = input("Please enter your age: ")
gn = input("Please also enter your gender: ")
player = Player(nm, ag, gn)
choice = int(input(
    f"Which game do you want to play, {player.name}?\n"
    f"1) -- Hangman\n2) -- Tic Tac Toe \n3) -- Rock Paper Scissors"
    f"\nPlease enter choice, 1, 2, or 3: "))

if choice == 1:
    hangman()
elif choice == 2:
    tic_tac_toe()
elif choice == 3:
    rock_paper_scissors()
else:
    print("Invalid choice. Game exiting. ")
