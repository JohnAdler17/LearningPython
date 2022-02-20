'''
 * Program or Lab #: Program 2: Darts
 *
 * Programmer: John Adler
 *
 * Due Date: September 14, 2017
 *
 * COMP141, Fall 2017
 *
 * Pledge: I have neither given nor received unauthorized aid
 *         on this program. 
 *
 * Description: This program takes an x-coordinate and y-coordinate input to
 *              then determine where a dart would land on a dart board. Each
 *              combination of x and y coordinates will determine where the
 *              dart lands and how many points are earned. If the dart lands
 *              off of the board, no points are awarded.
 *
 * Input: The user will input one x-coordinate and one y-coordinate to 
 *        determine where the dart will land.
 *
 * Output: Depending on the x and y coordinates, a string will be printed
 *         that displays the number of points awarded. If the board is missed,
 *         no points are awarded.
 *
'''

#These two statements define the variables x and y to be the integer
#corresponding to the coordinates where the dart lands.
x = int(input("What is the x-coordinate where your dart landed? "))

y = int(input("What is the y-coordinate where your dart landed? "))


#This function prints the statement "You win 5 points!" when called. It is
#called when the dart would land in the yellow sections of the dart board.
def main():
    print ("You win 5 points!")


#This function prints the statement "You win 10 points!" when called. It is
#called when the dart would land in the red sections of the dart board.
def yellow():
    print ("You win 10 points!")


#The following if/elif/else statements determine where the dart lands and what
#to print.
if (0 <= x <= 10) and (y <= 30):
    yellow()

elif (10 < x <= 40) and (y < 10):
    main()

elif (10 < x <= 30) and (10 <= y <= 30):
    print ("You win 15 points!")

elif (30 < x <= 40) and (10 < y <= 40):
    yellow()

elif (0 <= x <= 10) and (30 < y <= 40):
    main()

else:
    print ("You missed the board and earn no points.")
