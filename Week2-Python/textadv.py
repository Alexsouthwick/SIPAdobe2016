
print(
"You wake up one morning and find that you aren\'t in your bed; you aren\'t even in your room.You\'re in the middle of a giant maze.A sign is hanging from the ivy: 'You have one hour. Don\'t touch the walls.' There is a hallway to your right and to your left."
)


print("Type 'left' to go left or 'right' to go right.")
user_input = input()
while (user_input != "left" and user_input!= "right"): 
    print("Please either type 'right' or 'left'. Check your spelling and capitalization.")
    user_input= input()

if user_input == "left":
    print("You decide to go left and find a small dwarf sitting next to a tree. He looks mean, but he is the only person you can see and you could use some help...") 
    print("Type 'talk' or 'walk away' ")
    user_input = input()

    while (user_input != "talk" and user_input!= "walk away"): 
        print("Please either type 'talk' or 'walk away'. Check your spelling and capitalization.")
        user_input= input()

    if user_input == "talk":
        print("You decide to talk to the dwarf. At first he is very gruff but soon he starts to warm up to you. You ask him for advise on how to get out of the maze. He says 'I can\'t tell you how to get out, but I can say that there is a secret trap door about 20 feet from here. Make sure to avoid it.' You thank him and go on your way, making sure to avoid the secret trap door. At the end of the road you find a beautiful horse. You think it could help you leave the maze faster, but you don't know where it came from. ")
        print("Type 'take horse' or 'walk away'")
        user_input= input()

        while (user_input != "take horse" and user_input != "walk away"):
            print("Please either type 'take horse' or 'walk away'. Check your spelling and capitalization.")
            user_input= input()

        if user_input == 'take horse':
            print("You decide to take the horse. As you try to get on the horse it suddenly bucks up, throws you off, and you hit your leg on a tree. The horse had been scared by a nest of bees near its head and when they see you, they begin to sting you all over. Because of your leg injury you can't get up, and you are stung to death. ")
            print("You have died. Game Over.")
        elif user_input == "walk away":
            print("You decide to walk away from the horse and continue on foot. Suddenly you see the exit right in front of you! You sprint as fast as you can for the door and escape the maze!")
            print("You successfully exited the maze! Congratulations!")

    elif user_input== "walk away":
        print("You decide to ignore the mean-looking dwarf. You continue walking forward another 20 feet and suddenly the floor gives way beneath you. You fall suddenly through a secret trap door and crack your skull open on the sharp rocks below. ")
        print("You have died. Game Over.")

    
elif user_input == "right":
    print("You choose to go right and find a sword lying in the middle of a circle of pebbles. It is dark and you could use the protection, but you don\'t know where the sword came from.")
    print("Type 'take sword' or 'walk away' ") 
    user_input= input()

    while (user_input != "take sword" and user_input != "walk away"):
        print("Please either type 'take sword' or 'walk away'. Check your spelling and capitalization.")
        user_input= input()
   
    if user_input== "take sword":
        print("You decide to take the sword. You reach down to pick it up but find that you can\'t, it is too heavy. You suddenly hear a voice coming out of the maze somewhere. It says 'Only the chosen one can take the sword from the circle. You must prove you are the chosen one by battling my army of goblins!' Suddenly a giant horde of goblins erupts from the other side of the hallway. You can either hold your ground and fight the goblins with the sword or drop the sword and run away.")
        print("Type 'fight goblins' or 'run away' ")
        user_input= input()

        while (user_input != "fight goblins" and user_input !="run away"):
            print("Please either type 'fight goblins' or 'run away'. Check your spelling and capitalization.")
            user_input= input()

        if user_input== "fight goblins":
            print("You decide to stand your ground and fight the goblins. You fight some of them off and you scare the rest so much that they flee. The voice says 'You are the chosen one. Take the sword and exit the maze.' You step out of the circle of pebbles and suddenly a door opens at the end of the wall. You walk through the door holding your sword.")
            print("You successfully exited the maze! Congratulations!")
        elif user_input ==  "run away":
            print("You decide the run away from the goblins. As you are sprinting through the maze, you hear the voice shout 'YOU COWARD. YOU ARE NOT THE CHOSEN ONE!' Suddenly a lightning bolt erupted from the sky and strikes you down.")
            print("You have died. Game Over.")

    elif user_input == "walk away":
        print("You decide to leave the sword and keep walking. It is very dark and late and you are starting to get really hungry. Thankfully you come across a cute little restaurant in the middle of the maze. You walk in but there is nobody there, no customers, no waiters, nobody. The only thing in it is a beautiful, sweet smelling apple pie. You hear your stomach grumble as you see it.")
        print("Type 'take pie' or 'leave restaurant'")
        user_input= input()

        while (user_input != "take pie" and  user_input != "leave restaurant"):
            print("Please either type 'take pie' or 'leave restaurant'. Check your spelling and capitalization.")
            user_input= input()
    
        if user_input== "take pie":
            print("You try the pie. Suddenly a giant ogre rushes in from the kitchen. He screams 'DID YOU TAKE MY PIE! THAT WAS FOR MY MOTHER!! The ogre punches you in the face with such force that your head turns all the way around your body.")
            print("You have died. Game Over.")
        elif user_input == "leave restaurant":
            print(" You decide to leave the restaurant. You leave the restaurant out of the back door and on the other side of the hallway you see a door! You run towards it and exit the maze!")
            print("You successfully exited the maze! Congratulations!")
 



