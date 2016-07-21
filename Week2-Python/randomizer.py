import random
five_lines=["The water rushes", "The eagles soar high",
            "The waves crash on rocks","Breezes whisk through trees",
            "Fires crackle at night","Sunshine hits the dirt",
            "I lie in the sun", "The birds sing with me",
            "Glass shatters softly", "Trees break the skyline",
            "Green grass floods the fields", "Summer winds blow through",
            "Light circles darkness", "Flowers bloom in sun",
            "The sounds of night time", "Clouds gather around"]

seven_lines=["The sun sets down on the bluffs","I sit back on the elm tree",
             "Water flows through the river", "I touch the soft maple leaves",
             "Music plays soflty, sweetly", "I hear the birds singing near",
             "Lightness enfolds and follows", "I feel the sun on my face",
             "Birds chirp sweetly from the trees", "The earth is falling asleep"]
length_five= len(five_lines)
length_seven= len(seven_lines)
randcheck1=-2
randcheck2=-2
randcheck3=-2

for i in range(2):
    random_line1= random.randint(0,length_five-1)
    random_line2= random.randint(0,length_seven-1)
    random_line3= random.randint(0,length_five-1)


    
    while random_line1==random_line3:
        random_line3= random.randint(0,length_five-1)

    while (random_line1==randcheck1 or random_line1==randcheck3) :
        random_line1= random.randint(0,length_five-1)
        
    while (random_line2==randcheck2):
        random_line2= random.randint(0,length_seven-1)

    while (random_line3==randcheck1 or random_line3==randcheck3):
        random_line3= random.randint(0,length_five-1)

        
    print(five_lines[random_line1])
    if randcheck1 == -2:
        randcheck1= random_line1
    print(seven_lines[random_line2])
    if randcheck2 == -2:
        randcheck2= random_line2
    print(five_lines[random_line3])
    if randcheck3 == -2:
        randcheck3= random_line3

    
    print()
   
   

    




