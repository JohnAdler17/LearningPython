




from simplegraphics import *

canvas_size = 600
import random
def main():
    board = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]
    open_canvas(canvas_size, canvas_size)
    display_board(board)
    win = False


    
    for i in range (1, 19):
        for j in range (2):
            r = random.randint(0, 5)
            c = random.randint(0, 5)
            while board[r][c] != 0:
                r = random.randint(0, 5)
                c = random.randint(0, 5)
            board[r][c] = i
    print(board)

    num_matches = 0
    while win == False: 
        wait_for_click()
        click_x = get_last_click_x()
        click_y = get_last_click_y()
        c = int(click_x // 100)
        r = int(click_y // 100)
        number1 = str(board[r][c])        
        draw_string(number1, c * 100 + 50, r * 100 + 50, 18)
        first_coor_x = c * 100 + 50
        first_coor_y = r * 100 + 50

        

        wait_for_click()
        click_x = get_last_click_x()
        click_y = get_last_click_y()    
        c = int(click_x // 100)
        r = int(click_y // 100)
        number2 = str(board[r][c])
        draw_string(number2, c * 100 + 50, r * 100 + 50, 18)
        second_coor_x = c * 100 + 50
        second_coor_y = r * 100 + 50
        
        
        if first_coor_x == second_coor_x and first_coor_y == second_coor_y:
            set_color('black')
            
            draw_filled_circle(first_coor_x, first_coor_y, 18)
            draw_filled_circle(second_coor_x, second_coor_y, 18)
            set_color("pink")
            continue
        
        number1 = int(number1)
        number2 = int(number2)
        
        if number1 != number2:
            set_color('black')
            wait_for_click()
            draw_filled_circle(first_coor_x, first_coor_y, 18)
            draw_filled_circle(second_coor_x, second_coor_y, 18)
            set_color("pink")
                    
        elif number1 == number2:
            set_color('black')
            draw_filled_circle(first_coor_x, first_coor_y, 18)
            draw_filled_circle(second_coor_x, second_coor_y, 18)
            set_color("pink")
            draw_string(str(number1), first_coor_x, first_coor_y, 30)
            draw_string(str(number2), second_coor_x, second_coor_y, 30)
            perm_1_x = first_coor_x
            perm_2_x = second_coor_x
            perm_1_y = first_coor_y
            perm_2_y = second_coor_y
            num_matches += 1
            if (num_matches == 18):
                win = True
    set_color("white")
    draw_string("You Win!", 300, 300, 50)
    close_canvas_after_click()
        
            
    
def display_board(board):
    for i in range(100, canvas_size, 100):
        set_background_color('black')
        set_color('pink')
        draw_line(0, i, canvas_size, i)
        draw_line(i, 0, i, canvas_size)
        


main()
