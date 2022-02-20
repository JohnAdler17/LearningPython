'''
 * Program or Lab #: Connect the Dots
 *
 * Programmer: John Adler
 *
 * Due Date: 11/02/17
 *
 * COMP141, Fall 2017
 *
 * Pledge: I have neither given nor received unauthorized aid
 *         on this program. 
 *
 * Description: This program takes an input from the user to read a specific
 *              file type, open a canvas, and generate a picture based on the
 *              x and y coordinates denoted in the file. The program is ended
 *              by clicking on the canvas.
 *
 * Input: The user inputs the name of the file to be read and turned into a
 *        picture.
 *
 * Output: The program prints a 400 by 400 canvas with a different picture on
 *         it depending on the file name entered.
 *
'''

from simplegraphics import *

# This function reads the file name entered by the user, opens the file, and
# converts the x and y coordinates in the file to a picture by using the
# draw_line function.
def main():
    file_input = input("Enter file to be read: ")
    print('Click the canvas to close the window and end the program.')
    sf = float(input("Enter a strech factor: "))
    file = open(file_input, 'r')
    open_canvas(400, 400)
    line1 = file.readline()
    line1 = line1.rstrip()
    prevx, prevy = line1.split(' ')
    prevx = int(prevx)
    prevy = int(prevy)
    for line in file:
        line = line.rstrip()
        x, y = line.split(' ')
        x = int(x)
        y = int(y)
        currx = x
        curry = y
        if (currx == -1) or (curry == -1) or (prevx == -1) or (prevy == -1):
            prevx = currx
            prevy = curry
            continue
        draw_line((prevx*sf), (prevy*sf), (currx*sf), (curry*sf))
        prevx = currx
        prevy = curry
    close_canvas_after_click()
    file.close()
    
main()
