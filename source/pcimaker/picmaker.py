from PIL import Image, ImageFilter, ImageFont, ImageDraw
import time
from quote_generator import *
import os
size = 1080, 1080

'''n dient als counter für bilder'''
n = 3

#try:

    #while 1:

image = Image.open(os.getcwd()+"/" + str(n) + ".jpg")

image.thumbnail(size,Image.ANTIALIAS)

image = image.convert(mode='L')
image = image.filter(ImageFilter.GaussianBlur(20))

image = image.convert('RGB')

font_type = ImageFont.truetype('StayWriter-Handmade.ttf',50)
draw = ImageDraw.Draw(image)

quote = RandomQuoteGenerator.load_quote("quotes.csv")
t = ""+quote.author+": "+quote.text
draw.text(xy=tuple(el/3 for el in size), text=t, fill=(255,215,0), font=font_type)

image.save(os.getcwd()+"/" + str(n) + ".jpg")
#n += 1
#time.sleep(0.5)

#except:
#    print("alle Bilder wurden umgewandelt")
