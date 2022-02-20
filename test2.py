def volume_sphere(radius):
    vsphere = (4/3) * (3.14) * (radius**3)
    return vsphere

def volume_rect_prism(length, width, height):
    vprism = length * width * height
    return vprism

def volume_cube(s_length):
    vcube = volume_rect_prism(s_length, s_length, s_length)
    return vcube

def volume_cone(radius, height):
    vcone = (3.14) * (radius**2) * (height/3)
    return vcone

def volume_ice_cream_cone(radius, height):
    vicone = (volume_sphere(radius)/2) + volume_cone(radius, height)
    return vicone

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
            print("Error: Not a valid menu number.")

main()
