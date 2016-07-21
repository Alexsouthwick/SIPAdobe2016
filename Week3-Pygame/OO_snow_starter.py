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


pygame.init()

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height= 500
screen = pygame.display.set_mode((screen_width, screen_height))

snow_list = []

number_of_snowflakes = 100
for i in range(number_of_snowflakes):
    x_speed= random.randint(0,0)
    y_speed= random.randint(0,10)
    size= random.randint(3,25)
    x_pos= random.randint(0,700)
    y_pos= random.randint(0,0)
    snow_list.append((size, x_pos, y_pos))

pygame.display.set_caption("Snow")


class SnowFlake():

    '''
    This class will be used to create the SnowFlake Objects.
    It takes: 
        size - an integer that tells us how big we want the snowflake
        position - a 2 item list that tells us the coordinates of the snowflake (x,y) 
        wind - a boolean that lets us know if there is any wind or not.  
    '''

    def __init__(self, size, x_position, y_position):
        self.size= size
        self.x_position=x_position
        self.y_position= y_position
        #self.wind=wind
    
    
    def fall(self, x_speed, y_speed):
        """
        Take in a integer that represnts the speed at which the snowflake is falling in the y-direction.  
        A positive integer will have the snowflake falling down the screen. 
        A negative integer will have the snowflake falling up the screen. 
        
        If wind = True
            - the x direction of the snowflake changes
        """
        # if wind == True:
        #     x_speed= random.randint(-10, 10)
        #     self.x_position+= x_speed
        self.x_position+= x_speed
        self.y_position+= y_speed


        
    def draw(self):
        """
        Uses pygame and the global screen variable to draw the snowflake on the screen
        """
        pygame.draw.circle(screen, WHITE, [self.x_position, self.y_position], self.size)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



# Speed


#INITIALIZE YOUR SNOWFLAKE HERE!
#for i in range(number_of_snowflakes): 
   # for index in range(3):
       # snowflake = SnowFlake(snow_list[i][index])
snowflake1= SnowFlake(size, x_pos, 0)
# snowflake2= SnowFlake(size, x_pos, y_pos)
# snowflake3= SnowFlake(size, x_pos, y_pos)
# snowflake4= SnowFlake(size, x_pos, y_pos)
# snowflake5= SnowFlake(size, x_pos, y_pos)
# snowflake6= SnowFlake(size, x_pos, y_pos)
# snowflake7= SnowFlake(size, x_pos, y_pos)
# snowflake8= SnowFlake(size, x_pos, y_pos)
# # Snow List
# snow_list = [snowflake1, snowflake2, snowflake3, snowflake4, snowflake5, snowflake6, snowflake7, snowflake8]

# for flakes in range (snow_list):

#     x_speed= random.randint(-10,10)
#     y_speed= random.randint(0,10)
#     size= random.randint(10,50)
#     x_pos= random.randint(0,700)
#     y_pos= random.randint(0,500)

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
    screen.fill(BLACK)

    # --- Drawing code should go here
    # Begin Snow
    for i in range(100):
        snowflake1.draw()
        snowflake1.fall(x_speed, y_speed)
        x_pos= random.randint(0,700)
        x_speed=0
        y_speed= random.randint(-10,10)
    



    


    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
