# functions

# driver code
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

    print("YOU WIN!")

    if lives == 0:
        print("Game over")
        print("Solution is:")
        print(answer)


