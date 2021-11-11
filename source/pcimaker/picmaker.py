from PIL import Image, ImageFilter, ImageFont, ImageDraw
import time

'''size = 1080, 1080'''

'''n dient als counter für bilder'''
n = 1

#try:

    #while 1:

image = Image.open("//home//thassi//projects//ibot//source//pcimaker//pictures_original//" + str(n) + ".jpg")

image = image.filter(ImageFilter.GaussianBlur(20))

font_type = ImageFont.truetype('StayWriter-Handmade.ttf',200)
draw = ImageDraw.Draw(image)
draw.text(xy=(300,300), text = "motivierender Spruch", fill=(255,215,0), font=font_type)

image.save("//home//thassi//projects//ibot//source//pcimaker//pictures_new//" + str(n) + ".jpg")
#n += 1
#time.sleep(0.5)

#except:
#    print("alle Bilder wurden umgewandelt")
