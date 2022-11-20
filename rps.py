import random

choice = ['r', 'p', 's']
count = [0, 0]

def abbreviation(t):
    if t == 'r':
        print("Rock")
    elif t == 'p':
        print("Paper")
    elif t == "s":
        print("Scissors")


def main():
    while True:
        print(" ")
        turn = input("please enter your turn ('r', 'p', 's')").lower()
        if turn == 'exit':
            break
        else:
            abbreviation(turn)
        c_turn = random.choice(choice)
        abbreviation(c_turn)

        if turn == 'r' and c_turn == 's' or turn == 'p' and c_turn == 'r' or turn == 's' and c_turn == 'p':
            print("Human wins the point")
            count[0] += 1
        elif c_turn == 'r' and turn == 's' or c_turn == 'p' and turn == 'r' or c_turn == 's' and turn == 'p':
            print("Computer wins the point")
            count[1] += 1
        elif turn == c_turn:
            print("Deus!")

        print("the score is:", count)

        if count[0] == 3:
            print("Human wins the game")
            print(" ")
            replay = input("Wanna play again? (YES or NO)").lower()
            if replay == "YES":
                main()
            else:
                break

        elif count[1] == 3:
            print("Computer wins the game")
            print(" ")
            replay = input("Wanna play again? (YES or NO)").lower()
            if replay == "YES":
                return turn
            elif replay == "NO":
                break



main()
