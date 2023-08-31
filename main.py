import random

def print_board(board):
    for i in range(0, int(len(board))):
        print(board[i][0] + "|" + board[i][1] + "|" + board[i][2])
        if i < 2:
            print("-----")

def is_win(board, turn):
    if turn == "X":
        win = "XXX"
    else:
        win = "OOO"
    
    for i in range(0, int(len(board))):
        line = str(board[i][0])+ str(board[i][1]) + str(board[i][2])
        if line == win:
            print_board(board)
            print(turn + " KAZANDI")
            return True
    
    for i in range(0, int(len(board))):
        line = str(board[0][i])+ str(board[1][i]) + str(board[2][i])
        if line == win:
            print_board(board)
            print(turn + " KAZANDI")
            return True
        
    line = str(board[0][0])+ str(board[1][1]) + str(board[2][2])
    line2 = str(board[2][0])+ str(board[1][1]) + str(board[0][2])
    if line == win:
        print_board(board)
        print(turn + " KAZANDI")
        return True
    elif line2 == win:
        print_board(board)
        print(turn + " KAZANDI")
        return True


def player_input(board, turn):
    while True:
        print_board(board)
        if turn == "X":
            col = int(input(turn + "'in Sırası Sütunu Giriniz: ")) - 1
            row = int(input(turn +  "'in Sırası satırı Giriniz: ")) - 1
        elif turn == "O":
            col = int(input(turn + "'nun Sırası Sütunu Giriniz: ")) - 1
            row = int(input(turn +  "'nun Sırası satırı Giriniz: ")) - 1
        
        if is_empty(board, row, col):
            board[row][col] = turn
            return board
        else:
            print("Seçtiğiniz kutu dolu lütfen başka bir kutu seçiniz.")

def computer_input(board):
    while True:
        row = random.randrange(0, int(len(board)))
        col = random.randrange(0, int(len(board[row])))
        
        if is_empty(board, row, col):
            board[row][col] = "O"
            break

    return board

def is_empty(board, row, col):
    if board[row][col] == " ":
        return True
    else:
        return False

def is_game_ended(board):
    for i in range(0, int(len(board))):
        for j in range(0, int(len(board[i]))):
            if board[i][j] == " ":
                return False
    return True

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


player_count = int(input("1-Tek Kişilik\n2-İki Kişilik\nTercih: "))

if player_count == 1:
    while True:
        board = player_input(board, "X")
        if is_win(board, "X"):
            break

        if is_game_ended(board) == True:
            print_board(board)
            print("Tahta Doldu BERABERE")
            break

        board = computer_input(board)
        if is_win(board, "O"):
            break

elif player_count == 2:
    while True:
        board = player_input(board, "X")
        if is_win(board, "X"):
            break

        if is_game_ended(board) == True:
            print_board(board)
            print("Tahta Doldu BERABERE")
            break

        board = player_input(board, "O")
        if is_win(board, "O"):
            break