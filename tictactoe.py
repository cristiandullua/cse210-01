'''
Tic-Tac-Toe
Author: Cristian Ullua
'''
from colorama import Back, Style
PLAYER_X = 'X'
PLAYER_O = 'O'

def main():
    current_player = next_player('')
    board = create_board()

    for turns in range(9):
        display_board(board)
        make_move(current_player, board)
        current_player = next_player(current_player)
        if has_winner(board):
            print('Good game. Thanks for playing!')
            break

    display_board(board)

    if not has_winner(board):
        print('It is a draw. Try again.')

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    print()
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print('-+-+-')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print('-+-+-')
    print(f'{board[6]}|{board[7]}|{board[8]}')
    print()
 
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(current_player, board):
    while True:
        try:
            square = int(input(f'{current_player}\'s turn to choose a square (1-9): '))
            if board[square - 1] == PLAYER_X or board[square - 1] == PLAYER_O:
                print()
                print('Position already ocupied, try again.')
            else:
                break
        except Exception as e:
                print(e)
                continue

    board[square - 1] = current_player

def next_player(current):
    if current == "" or current == PLAYER_O:
        return PLAYER_X
    elif current == PLAYER_X:
        return PLAYER_O

if __name__ == "__main__":
    try:
        main()
    except BaseException:
        import sys
        print(sys.exc_info()[0])
        import traceback
        print(traceback.format_exc())
    finally:
        print("Press Enter to continue ...")
        input()