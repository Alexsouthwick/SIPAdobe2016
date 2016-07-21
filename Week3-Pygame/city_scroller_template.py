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
GREY = (129, 129, 129)
YELLOW = (255, 255, 0)
colors = [BLACK, GREEN, BLUE, RED]

def random_color():
    return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



class Building():
    def __init__(self, x_point, y_point, width, height, color):
        self.x_point= x_point
        self.y_point= y_point
        self.width= width
        self.height= height
        self.color= color

    def draw(self,x_point):
        pygame.draw.rect(screen, self.color, (self.x_point, self.y_point, self.width, self.height))
        pygame.draw.rect(screen, BLACK, (self.x_point, self.y_point, self.width, self.height), 2)


    def move(self, speed):
        self.x_point+=speed
        

class Scroller(object):

    def __init__(self, width, height, base, color, speed):
        self.width= width
        self.height= height
        self.base= base
        self.color= color
        self.speed= speed
        self.building_list= []
        self.combined_width= 0
        self.add_buildings()

    def add_buildings(self):
        while  self.combined_width<= self.width:
            self.add_building(self.combined_width)

    def add_building(self, x_location):
        width= random.randint(50,100)
        building= Building(x_location, self.base, width, random.randint(-500,-50), self.color)
        self.combined_width+= width
        self.building_list.append(building)

    def draw_buildings(self):
        for item in self.building_list:
            item.draw(self.combined_width)

    def move_buildings(self):
        last_building=self.building_list[-1]
        first_building= self.building_list[0]
        for item in self.building_list:
            item.move(self.speed)
        if last_building.x_point>= SCREEN_WIDTH:
            self.building_list.remove(last_building)
        if first_building.x_point>= 0:
            width= random.randint(50,100)
            x_location= first_building.x_point- width
            building= Building(x_location, self.base, width, random.randint(-500,-10), self.color)
            self.building_list.insert(0,building)
class Cloud():
    def __init__(self, x_pos, color):
        self.x_pos= x_pos
        self.color= color

    def draw(self):
        radius= 20
        y_pos= 50
        pygame.draw.circle(screen, self.color, (self.x_pos, 50), radius)
        pygame.draw.circle(screen, self.color, (self.x_pos+ 20, y_pos), radius)
        pygame.draw.circle(screen, self.color, (self.x_pos+40, y_pos), radius)
        pygame.draw.circle(screen, self.color, (self.x_pos+ 10, 30), radius)
        pygame.draw.circle(screen, self.color, (self.x_pos+30, 30), radius)

    def move(self, speed):
        self.x_pos+= speed

    # def loop(self):
    #     if self.x_pos> 800:
    #         cloud2= Cloud(0, WHITE)
    #         cloud2.move_draw()


    def move_draw(self):
        self.draw()
        #print("this is drawing")
        self.move(-1)
        #print("this is moving")
        # self.loop()
        # print("this is looping")


FRONT_SCROLLER_COLOR = (224,  238, 238)
MIDDLE_SCROLLER_COLOR = (193, 205, 205)
BACK_SCROLLER_COLOR = (131,  139, 139)
BACKGROUND_COLOR = (151,  255, 255)

front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT + 200, FRONT_SCROLLER_COLOR, 5)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT + 100), MIDDLE_SCROLLER_COLOR, 3)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT), BACK_SCROLLER_COLOR, 2)

cloud= Cloud(800, WHITE)


# -------- Main Program Loop --------

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
    screen.fill(BACKGROUND_COLOR)

    # --- Drawing code should go here
    pygame.draw.circle(screen, YELLOW, (100, 100), 50 )
    back_scroller.draw_buildings()
    back_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    front_scroller.draw_buildings()
    front_scroller.move_buildings()
    cloud.move_draw()


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
