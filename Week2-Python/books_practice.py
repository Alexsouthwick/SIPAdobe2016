import random
colors= ["red", "yellow", "blue", "green", "purple"]
colors_length= len(colors)
random_index= random.randint(0, colors_length-1)
print(random_index)
print(colors[random_index])
