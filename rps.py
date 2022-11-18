import random
choice = ['r', 'p', 's']

def abbreviation(t):
    if t == 'r':
        print("Rock")
    elif t == 'p':
        print("Paper")
    elif t == "s":
        print("Scissors")

def main():
    while True:
        turn = input("please enter your turn ('r', 'p', 's')").lower()
        if turn == 'exit':
            break
        else:
            abbreviation(turn)
        c_turn = random.choice(choice)
        abbreviation(c_turn)

        if turn == 'r' and c_turn == 's' or turn == 'p' and c_turn == 'r' or turn == 's' and c_turn == 'p':
            print("Human wins!")
        elif c_turn == 'r' and turn == 's' or c_turn == 'p' and turn == 'r' or c_turn == 's' and turn == 'p':
            print("Computer wins!")
        elif turn == c_turn:
            print("Deus!")


main()
