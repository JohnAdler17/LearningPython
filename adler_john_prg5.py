'''
 * Program or Lab #: Program 5: Bottles of a Beverage
 *
 * Programmer: John Adler
 *
 * Due Date: 10/19/2017
 *
 * COMP141, Fall 2017
 *
 * Pledge: I have neither given nor received unauthorized aid
 *         on this program. 
 *
 * Description: This program will ask for a number of bottles and how many to
 *              take down from the wall each time from the user as an
 *              integer input and then will print the song about bottles of
 *              a beverage on a wall for the specified amount of bottles and
 *              the interval that they are taken down.
 *
 * Input: The user inputs a value for the starting number of bottles that are
 *        on the wall and a value for the interval that the bottles are taken
 *        down from the wall. These are the local variables for the song.
 *
 * Output: The program prints a song counting down as the bottles are taken
 *         from a wall. The number of bottles and interval specified determine
 *         how long the song will be.
 *
'''

# This function determines which version of the song to print after the user
# has input values for the number of bottles and the interval.
# Parameters: num_bottles, the number of bottles, and num_int, the interval.
# Returns: none.
def bottles_song(num_bottles, num_int):  
    if num_bottles == 1:
         print(num_bottles, "bottle of pop on the wall,", num_bottles, end=' ')
         print("bottle of pop.")
         print("Take it down, pass it around,", end=' ')
         print((num_bottles - num_int), "bottles of pop on the wall.")
    elif ((num_bottles - num_int) == 1) and (num_int == 1):
         print(num_bottles, "bottles of pop on the wall,", num_bottles, end=' ')
         print("bottles of pop.")
         print("Take one down, pass it around,", end=' ')
         print((num_bottles - num_int), "bottle of pop on the wall.")
    elif (num_bottles - num_int) == 1:
         print(num_bottles, "bottles of pop on the wall,", num_bottles, end=' ')
         print("bottles of pop.")
         print("Take", num_int, "down, pass them around,", end=' ')
         print((num_bottles - num_int), "bottle of pop on the wall.")
    elif num_int == 1:
         print(num_bottles, "bottles of pop on the wall,", num_bottles, end=' ')
         print("bottles of pop.")
         print("Take one down, pass it around,", end=' ')
         print((num_bottles - num_int), "bottles of pop on the wall.")
    else:
         print(num_bottles, "bottles of pop on the wall,", num_bottles, end=' ')
         print("bottles of pop.")
         print("Take", num_int, "down, pass them around,", end=' ')
         print((num_bottles - num_int), "bottles of pop on the wall.")
    
# The break at the end of the function determines whether another interval
# of bottles can be taken down from the wall and if not, the while loop ends.
def main():
    num_bottles = int(input("How many bottles should we start with? "))
    while num_bottles <= 0:
        print("You must start with a positive number of bottles.", end=' ')
        print("Please re-enter the number.")
        num_bottles = int(input("How many bottles should we start with? "))
    num_int = int(input("How many do we take off the wall each time? "))
    while num_int <= 0:
        print("You must remove a positive number of bottles.", end=' ')
        print("Please re-enter the number.")
        num_int = int(input("How many do we take off the wall each time? "))
    while num_bottles > 0:
        bottles_song(num_bottles, num_int)
        num_bottles -= num_int
        if (num_bottles - num_int) < 0:
            break

main()

