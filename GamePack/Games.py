# Functions


def hangman():
    print()
    answerstr = input("Enter text to guess: ")
    answer = []
    for i in answerstr:
        answer.append(i)
    answer = " ".join(answer)

    for i in range(0, 20):
        print("---" * 25)

    print("Guess the following: ")

    to_guess = ""
    for i in range(0, len(answerstr)):
        to_guess = to_guess + "_ "
    print(to_guess)

    lives = 5

    while lives > 0:
        print(f"You have {lives} lives")

        # answer = "h e a l   t h e   w o r l d"

        guess = input("Your answer: ")
        guess = guess.lower()
        found = 0
        flag = True
        index = []
        while (flag):
            if index == []:
                index.append(answer.find(guess))
            if index[found] != -1:
                found = found + 1
                index.append(answer.find(guess, index[found - 1] + 1))

            elif index.index(-1) != -1:
                flag = 0

        if index[0] != -1:
            num = 0
            index.pop()
            for i in index:
                to_guess1 = to_guess[0:index[num]]
                to_guess2 = to_guess[index[num] + 1:]
                to_guess1 = to_guess1 + guess
                to_guess = to_guess1 + to_guess2
                print(to_guess)
                num = num + 1
        else:
            lives = lives - 1

        # print("YOU WIN!")

        if lives == 0:
            print("Game over")
            print("Solution is:")
            print(answer)


def tic_tac_toe():
    # Tic-Tac-Toe Program using
    # random number in Python

    # importing all necessary libraries
    import numpy as np
    import random
    from time import sleep

    # Creates an empty board
    def create_board():
        return (np.array([[0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]]))

        # Check for empty places on board

    def possibilities(board):
        l = []

        for i in range(len(board)):
            for j in range(len(board)):

                if board[i][j] == 0:
                    l.append((i, j))
        return (l)

        # Select a random place for the player

    def random_place(board, player):
        selection = possibilities(board)
        current_loc = random.choice(selection)
        board[current_loc] = player
        return (board)

        # Checks whether the player has three

    # of their marks in a horizontal row
    def row_win(board, player):
        for x in range(len(board)):
            win = True

            for y in range(len(board)):
                if board[x, y] != player:
                    win = False
                    continue

            if win == True:
                return (win)
        return (win)

        # Checks whether the player has three

    # of their marks in a vertical row
    def col_win(board, player):
        for x in range(len(board)):
            win = True

            for y in range(len(board)):
                if board[y][x] != player:
                    win = False
                    continue

            if win == True:
                return (win)
        return (win)

        # Checks whether the player has three

    # of their marks in a diagonal row
    def diag_win(board, player):
        win = True

        for x in range(len(board)):
            if board[x, x] != player:
                win = False
        return (win)

        # Evaluates whether there is

    # a winner or a tie
    def evaluate(board):
        winner = 0

        for player in [1, 2]:
            if (row_win(board, player) or
                    col_win(board, player) or
                    diag_win(board, player)):
                winner = player

        if np.all(board != 0) and winner == 0:
            winner = -1
        return winner

        # Main function to start the game

    def play_game():
        board, winner, counter = create_board(), 0, 1
        print(board)
        sleep(2)

        while winner == 0:
            for player in [1, 2]:
                board = random_place(board, player)
                print("Board after " + str(counter) + " move")
                print(board)
                sleep(2)
                counter += 1
                winner = evaluate(board)
                if winner != 0:
                    break
        return (winner)

        # Driver Code

    print("Winner is: " + str(play_game()))

def rock_paper_scissors():
    # import random module
    import random

    # Print multiline instruction
    # performstring concatenation of string
    print("Winning Rules of the Rock paper scissor game as follows: \n"
          + "Rock vs paper->paper wins \n"
          + "Rock vs scissor->Rock wins \n"
          + "paper vs scissor->scissor wins \n")

    while True:
        print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")

        # take the input from user
        choice = int(input("User turn: "))

        # OR is the short-circuit operator
        # if any one of the condition is true
        # then it return True value

        # looping until user enter invalid input
        while choice > 3 or choice < 1:
            choice = int(input("enter valid input: "))

        # initialize value of choice_name variable
        # corresponding to the choice value
        if choice == 1:
            choice_name = 'Rock'
        elif choice == 2:
            choice_name = 'paper'
        else:
            choice_name = 'scissor'

        # print user choice
        print("user choice is: " + choice_name)
        print("\nNow its computer turn.......")

        # Computer chooses randomly any number
        # among 1 , 2 and 3. Using randint method
        # of random module
        comp_choice = random.randint(1, 3)

        # looping until comp_choice value
        # is equal to the choice value
        while comp_choice == choice:
            comp_choice = random.randint(1, 3)

        # initialize value of comp_choice_name
        # variable corresponding to the choice value
        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'paper'
        else:
            comp_choice_name = 'scissor'

        print("Computer choice is: " + comp_choice_name)

        print(choice_name + " V/s " + comp_choice_name)

        # condition for winning
        if ((choice == 1 and comp_choice == 2) or
                (choice == 2 and comp_choice == 1)):
            print("paper wins => ", end="")
            result = "paper"

        elif ((choice == 1 and comp_choice == 3) or
              (choice == 3 and comp_choice == 1)):
            print("Rock wins =>", end="")
            result = "Rock"
        else:
            print("scissor wins =>", end="")
            result = "scissor"

        # Printing either user or computer wins
        if result == choice_name:
            print("<== User wins ==>")
        else:
            print("<== Computer wins ==>")

        print("Do you want to play again? (Y/N)")
        ans = input()

        # if user input n or N then condition is True
        if ans == 'n' or ans == 'N':
            break

    # after coming out of the while loop
    # we print thanks for playing
    print("\nThanks for playing")
