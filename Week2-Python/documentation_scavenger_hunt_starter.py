"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
MIDNIGHT_BLUE= (25, 25, 112)
PURPLE= (148, 0, 211)


pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# WRITE YOUR CODE HERE
colors= [BLACK, WHITE, RED, GREEN, BLUE, GREY, MIDNIGHT_BLUE, PURPLE]
colors_length= len(colors)
rand_background= random.randint(0, colors_length-1)




x=350
y=250
speed_x= random.randint(-10, 10)
speed_y= random.randint(-10,10)
circle_size= random.randint(20,80)
rand_color= random.randint(0,colors_length-1)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(colors[rand_background])

    # --- Drawing code should go here

    
    pygame.draw.circle(screen, colors[rand_color],[x,y],circle_size,0)
    x+= speed_x
    y+= speed_y
    

    
    if (x<= circle_size or x>=SCREEN_WIDTH-circle_size):
        speed_x=-speed_x
        rand_color= random.randint(0,colors_length-1)
    if (y<= circle_size or y>=SCREEN_HEIGHT-circle_size):
        speed_y= -speed_y
        rand_color= random.randint(0,colors_length-1)
        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
       

    # --- Limit to 60 frames per second
    clock.tick(60)
    

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
