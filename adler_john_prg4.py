'''
 * Program or Lab #: Program 4: Geometry Volumes
 *
 * Programmer: John Adler
 *
 * Due Date: October 1, 2017
 *
 * COMP141, Fall 2017
 *
 * Pledge: I have neither given nor received unauthorized aid
 *         on this program. 
 *
 * Description: This program starts by printing a menu assigning numbers 1-5 to
 *              calculate the volumes of different shapes and the number 6 to
 *              quit the program. Once a number 1-5 is entered, the user is
 *              prompted to enter different values for radius, length, width,
 *              and/or height depending on which shape is selected. Once the
 *              volume of the shape is calculated, the user is prompted to enter
 *              another menu number and this continues until the number 6 is
 *              entered to quit the program.
 *
 * Input: The user inputs a number 1-5 to calculate the volume of a certain
 *        shape or 6 to quit the program. Once a number 1-5 is selected, the
 *        user inputs certain values for the dimensions of the shape.
 *
 * Output: The program outputs a menu in the beginning of the main function and
 *         a print statement containing the calculated volume of the shape once
 *         the shape dimensions are entered. After a volume is calculated, a
 *         print statement is output asking for another menu value. If the value
 *         is 6, a statement will be printed that says "Program ending..." or if
 *         the value is not 1-6, an error statement will be printed instead.
 *
'''

# This function computes the volume of a sphere.
# Parameters: radius, the radius of the sphere.
# Returns: vsphere, the volume of a sphere.
def volume_sphere(radius):
    vsphere = (4/3) * (3.14) * (radius**3)
    return vsphere


# This function computes the volume of a rectangular prism.
# Parameters: length, width, and height of the prism.
# Returns: vprism, the volume of the prism.
def volume_rect_prism(length, width, height):
    vprism = length * width * height
    return vprism


# This function computes the volume of a cube.
# Parameters: s_length, the length of one side of the cube.
# Returns: vcube, the volume of the cube.
def volume_cube(s_length):
    vcube = volume_rect_prism(s_length, s_length, s_length)
    return vcube


# This function computes the volume of a cone.
# Parameters: radius and height of the cone.
# Returns: vcone, the volume of the cone.
def volume_cone(radius, height):
    vcone = (3.14) * (radius**2) * (height/3)
    return vcone


# This function computes the volume of an ice cream cone.
# Parameters: radius and height of the cone.
# Returns: vicone, the volume of the ice cream cone.
def volume_ice_cream_cone(radius, height):
    vicone = (volume_sphere(radius)/2) + volume_cone(radius, height)
    return vicone


# The main function starts by printing a menu for the user, asks the user for a
# menu input, then either calculates a volume, quits the program, or produces
# an error message depending on the menu value entered. The menu number prompt
# will continue to print until a 6 is entered as the menu value, ending the
# program.
def main():
    print("Menu:")
    print("(1) Volume of a Sphere")
    print("(2) Volume of a Prism")
    print("(3) Volume of a Cube")
    print("(4) Volume of a Cone")
    print("(5) Volume of an Ice Cream Cone")
    print("(6) Quit")
    num = 0
    while num != 6:
        num = int(input("Menu #: "))
        if (num == 1):
            radius = float(input("What is the radius of the sphere? "))
            final_volume = volume_sphere(radius)
            print ("Volume of the sphere is", final_volume)
        elif (num == 2):
            length = float(input("What is the length of the prism? "))
            width = float(input("What is the width of the prism? "))
            height = float(input("What is the height of the prism? "))
            final_volume = volume_rect_prism(length, width, height)
            print ("Volume of the prism is", final_volume)
        elif (num == 3):
            s_length = float(input("What is the side length of the cube? "))
            final_volume = volume_cube(s_length)
            print ("Volume of the cube is", final_volume)
        elif (num == 4):
            radius = float(input("What is the radius of the cone? "))
            height = float(input("What is the height of the cone? "))
            final_volume = volume_cone(radius, height)
            print ("Volume of the cone is", final_volume)
        elif (num == 5):
            radius = float(input("What is the radius of the ice cream? "))
            height = float(input("What is the height of the ice cream? "))
            final_volume = volume_ice_cream_cone(radius, height)
            print ("Volume of the ice cream come is", final_volume)
        elif (num == 6):
            print("Program ending...")
        else:
            print("Error: Not a valid menu number. Valid intigers are 1-6")

main()
