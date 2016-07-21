

import PIL
from PIL import Image
im= Image.open("sticks.jpg")
#im.rotate(0).show()
pix= im.load()
new_pix=[]
for j in range(750):
    for i in range(750):
        #print(pix[i,j])
        r=(pix[i,j][0])
        b=(pix[i,j][1])
        g=(pix[i,j][2])
        if ((r+b+g)<182):
            r= 0
            b=51
            g=76
            new_pix.insert(i,[r,b,g])
        elif (364>(r+b+g)>=182):
            r= 217
            b=26
            g=33
            new_pix.insert(i,[r,b,g])
        elif (546>(r+b+g)>=364):
            r= 112
            b=150
            g=158
            new_pix.insert(i,[r,b,g])
        elif ((r+b+g)>=546):
            r= 252
            b=227
            g=166
            new_pix.insert(i,[r,b,g])

new_colors = tuple(new_pix)
#im.putdata(new_colors)
im = Image.new ("RGB", (750,750), new_colors)
im.rotate(0).show()
print("printed")
        
        #new_image.save("newpic.jpg", "jpeg")    
#new_image.save("output.jpg", "jpeg")




