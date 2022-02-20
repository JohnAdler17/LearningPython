# Name: John Adler
# Project: Potato Heads
# Pledge: I have neither given nor received unauthorized aid on this program. 
# Description: This program draws 2 identical potatoes side-by-side with
#              identical hair, mouth, and eye features no matter the location of
#              the potato on the canvas.
# Input: There is no input for this program.
# Output: The program outputs a canvas with two identical potato drawings each
#         with eyes, a mouth, and hair.

from simplegraphics import *

# Draw the eyes on a potato of radius 150 pixels.
# Parameters: (centerx, centery), the (x, y) coordinates of the potato center.
# Returns: None
# This function draws the eyes on each of the potatoes.
def draw_eyes(centerx, centery):
    set_color("black")
    draw_filled_circle((centerx - 45), (centery - 20), 30)
    draw_filled_circle((centerx + 45), (centery - 20), 30)
    set_color("white")
    draw_filled_circle((centerx - 45), (centery - 20), 27)
    draw_filled_circle((centerx + 45), (centery - 20), 27)
    set_color_rgb(153, 76, 0)
    draw_filled_circle((centerx - 45), (centery - 17), 18)
    draw_filled_circle((centerx + 45), (centery - 17), 18)
    set_color("black")
    draw_filled_circle((centerx - 45), (centery - 16), 12)
    draw_filled_circle((centerx + 45), (centery - 16), 12)


# Draw the hair on a potato of radius 150 pixels.
# Parameters: (centerx, centery), the (x, y) coordinates of the potato center.
# Returns: None
# This function draws the hair on each of the potatoes.
def draw_hair(centerx, centery):
    draw_filled_polygon((centerx - 120), (centery - 100), (centerx + 120),
                        (centery - 100), (centerx + 65), (centery - 140),
                        (centerx + 35), (centery - 157), (centerx),
                        (centery - 165), (centerx - 35), (centery - 157),
                        (centerx - 65), (centery - 140))

# Draw the mouth on a potato of radius 150 pixels.
# Parameters: (centerx, centery), the (x, y) coordinates of the potato center.
# Returns: None
# This function draws the mouth on each of the potatoes.
def draw_mouth(centerx, centery):
    draw_filled_polygon((centerx - 100), (centery + 45), (centerx + 100),
                        (centery + 45), (centerx + 65), (centery + 75),
                        (centerx + 45), (centery + 85), (centerx),
                        (centery + 100), (centerx - 45), (centery + 85),
                        (centerx - 65), (centery + 75))
    set_color("white")
    draw_filled_polygon((centerx - 95), (centery + 48), (centerx + 95),
                        (centery + 48), (centerx + 62), (centery + 72),
                        (centerx + 42), (centery + 82), (centerx),
                        (centery + 97), (centerx - 42), (centery + 82),
                        (centerx - 62), (centery + 72))
    set_color("black")
    set_line_thickness(4)
    draw_line((centerx - 80), (centery + 45), (centerx - 80), (centery + 60))
    draw_line((centerx + 80), (centery + 45), (centerx + 80), (centery + 62))
    draw_line((centerx - 45), (centery + 45), (centerx - 45), (centery + 85))
    draw_line((centerx + 45), (centery + 45), (centerx + 45), (centery + 85))
    draw_line(centerx, (centery + 45), centerx, (centery + 100))


# The program starts here.  
# *** DO NOT CHANGE ANY OF THE CODE IN MAIN. ***
def main():
	open_canvas(800, 400)

	# Draw the left potato:
	# Draw a potato-colored circle, centered at (200, 200).
	set_color_rgb(224, 144, 76)
	draw_filled_circle(200, 200, 150)
	set_color("black")

	# Draw the features of the left potato.
	draw_eyes(200, 200)
	draw_hair(200, 200)
	draw_mouth(200, 200)

	# Draw the right potato:
	# Draw a potato-colored circle, centered at (600, 200).
	set_color_rgb(224, 144, 76)
	draw_filled_circle(600, 200, 150)
	set_color("black")

	# Draw the features of the right potato.
	draw_eyes(600, 200)
	draw_hair(600, 200)
	draw_mouth(600, 200)    
	
	close_canvas_after_click()

main()
