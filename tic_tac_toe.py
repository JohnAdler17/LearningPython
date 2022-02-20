from simplegraphics import *

canvas_size = 300
def main():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    open_canvas(canvas_size, canvas_size)
    playernum = 1
    while not x_wins(board) and not o_wins(board) and not tie(board):
        print_board(board)
        display_board(board)
        if(playernum == 1):
            print("Player X's turn")
        else:
            print("Player O's turn")
            
        #r = int(input("row for move: "))
        #c = int(input("col for move: "))
        wait_for_click()
        x = get_last_click_x()
        y = get_last_click_y()
        r = int(y//100)
        c = int(x//100)
        do_move(board, r, c, playernum)

        # switch player to other player
        if playernum == 1:
            playernum = -1
        else:
            playernum = 1

    print_board(board)
    display_board(board)
    print("Game over!")
    draw_string("Game over!", 150, 20, 25)

def sumRow(board, row):
    return sum(board[row])

def sumColumn(board, col):
    total = 0
    for row in range(len(board[col])):
        total += board[row][col]
    return total

def sum3(num1, num2, num3):
    return sum([num1,num2, num3])

def do_move(board, row, col, xo):
    board[row][col] = xo

def x_wins(board):
    wins = False
    for x in range(len(board)):
        if sumRow(board, x) == 3:
            wins = True
        elif sumColumn(board, x) == 3:
            wins = True
    if sum3(board[0][0], board[1][1], board[2][2]) == 3:
        wins = True
    elif sum3(board[2][0], board[1][1], board[0][2]) == 3:
        wins = True
    if(wins):
        print("X wins!")
    return wins

def o_wins(board):
    wins = False
    for x in range(len(board)):
        if sumRow(board, x) == -3:
            wins = True
        elif sumColumn(board, x) == -3:
            wins = True
    if sum3(board[0][0], board[1][1], board[2][2]) == -3:
        wins = True
    elif sum3(board[2][0], board[1][1], board[0][2]) == -3:
        wins = True
    if(wins):
        print("X wins!")
    return wins

def tie(board):
    tie = False
    if not x_wins(board) and not o_wins(board):
        anyZeros = False
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == 0:
                    anyZeros = True
                    break
            if anyZeros:
                break
        if not anyZeros:
            tie = True
    if tie:
        print("Tied Game!")
    return tie

def print_board(board):
    for row in range(0, len(board[row])):
        for col in range(0, len(board[row])):
            if board[row][col] == 1:
                print("X", end=' ')
            elif board[row][col] == 0:
                print("-", end=' ')
            else:
                print("O", end=' ')
        print()

def display_board(board):
    for i in range(100, canvas_size, 100):
        draw_line(0, i, canvas_size, i)
        draw_line(i, 0, canvas_size)
    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            if board[row][col] == 1:
                draw_image('x.gif', col*100 + 50, row*100 + 50)
            elif board[row][col] == -1:
                draw_image('o.gif', col*100 + 50, row*100 + 50)
main()

#draw_image(filename, x, y) <-- centers image at (x, y)
# the files can be .png or .jpg (not gifs)
