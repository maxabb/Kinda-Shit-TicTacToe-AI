# Basic Tic-Tac-Toe Game

# function to print a given board
def print_board(b):
    for row in b:
        print("|", end="")
        for column in row:
            print(column + '|', end="")
        print()
    print()


# function to check if somebody has won the game
def check_win(b):
    # check horizontal
    for row in b:
        if row[0] == row[1] == row[2] and row[2] != ' ':
            return row[0]

    # check vertical
    for i in range(3):
        if b[0][i] == b[1][i] == b[2][i] and b[0][i] != ' ':
            return b[0][i]

    # check diagonal
    if (b[0][0] == b[1][1] == b[2][2] or b[0][2] == b[1][1] == b[2][0]) and b[1][1] != ' ':
        return b[1][1]
    return False


# function to check if the game board is full
def check_full(b):
    if count_empty(b) == 0:
        return True
    return False


# function to assign a value to a game state
def get_value(b):
    empty = 0
    result = 0
    for row in b:
        for item in row:
            if item == ' ':
                empty += 1

    if check_win(b) == 'X':
        result = 1
    elif check_win(b) == 'O':
        result = -1

    return empty * result


# function to count the empty squares
def count_empty(b):
    count = 0
    for row in b:
        for item in row:
            if item == ' ':
                count += 1
    return count


# ai
def minimax(bo):
    original_board = []
    original_row = []
    b = []
    highest_value = -100
    final = ""

    ir = -1

    for row in bo:
        for item in row:
            original_row.append(item)
        b.append(original_row)
        original_row = []

    for row in b:
        for item in row:
            original_row.append(item)
        original_board.append(original_row)
        original_row = []

    # try every move finding the one with the highest value
    for row in b:
        ir += 1
        ii = -1
        for item in row:
            ii += 1
            if item == ' ':
                b[ir][ii] = 'O'
                if get_value(b) > highest_value:
                    highest_value = get_value(b)
                    final = f"{ir+1},{ii+1}"
                b[ir][ii] = 'X'
                if get_value(b) > 0:
                    b[ir][ii] = 'O'
                    final = f"{ir + 1},{ii + 1}"
                    return final
                b[ir][ii] = 'O'
                b = []
                for r in original_board:
                    for i in r:
                        original_row.append(i)
                    b.append(original_row)
                    original_row = []
    return final


#  make sure file is the main one being run
if __name__ == '__main__':
    running = True
    turn = 'X'
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    # game loop
    while running:
        # get move / generate move
        if turn == 'X':
            print("Insert Move: ", end="")
            move = input()
        else:
            if board[1][1] == ' ':
                board[1][1] = 'O'
            else:
                move = minimax(board)

        # make turn
        if board[int(move[0]) - 1][int(move[2]) - 1] != 'X':
            board[int(move[0]) - 1][int(move[2]) - 1] = turn

        print_board(board)

        if check_win(board):
            print(turn + " Wins!")
            print(get_value(board))
            running = False
            break

        if check_full(board):
            print("Draw!")
            running = False

        # change move
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
