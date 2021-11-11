from PIL import Image, ImageFilter, ImageFont, ImageDraw
import time

size = 1080, 1080

'''n dient als counter für bilder'''
n = 3

#try:

    #while 1:

image = Image.open("//home//thassi//projects//ibot//source//pcimaker//pictures_original//" + str(n) + ".jpg")

image.thumbnail(size,Image.ANTIALIAS)

image = image.convert(mode='L')
image = image.filter(ImageFilter.GaussianBlur(20))

image = image.convert('RGB')

font_type = ImageFont.truetype('StayWriter-Handmade.ttf',50)
draw = ImageDraw.Draw(image)
draw.text(xy=tuple(el/3 for el in size), text = "motivierender Spruch", fill=(255,215,0), font=font_type)

image.save("//home//thassi//projects//ibot//source//pcimaker//pictures_new//" + str(n) + ".jpg")
#n += 1
#time.sleep(0.5)

#except:
#    print("alle Bilder wurden umgewandelt")
