def hangman(word):
    wrong = 0
    stages = ["",
              "__________          ",
              "|                   ",
              "|         |         ",
              "|         0         ",
              "|        /|\        ",
              "|        / \        ",
              "|                   "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to HANGMAN!")
    while wrong < len(stages) -1:
        print("\n")
        msg = "guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("you win!")
            print(" ".join(board))
            print(n)
            win = True
            break
    if not win:
        print("\n".join(stages))
        print("you died!!!!;)  answer is {}." .format(word))

import random
unko = [
        "banana",
        "roll",
        "train",
        "sword",
        "alibi",
        "altar",
        "brave"
        ]

hangman(random.choice(unko))















    

