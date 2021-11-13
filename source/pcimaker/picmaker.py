from PIL import Image, ImageFilter, ImageFont, ImageDraw
import time

'''n dient als counter für bilder'''
n = 3

#try:

    #while 1:

image = Image.open("//home//thassi//projects//ibot//source//pcimaker//pictures_original//" + str(n) + ".jpg")

W, H = image.size
msg = "motivierender Spruch"
#image.thumbnail(size,Image.ANTIALIAS)

image = image.convert(mode='L')
image = image.filter(ImageFilter.GaussianBlur(20))

image = image.convert('RGB')

font_type = ImageFont.truetype('Garet-Heavy.ttf',50)

draw = ImageDraw.Draw(image)
w, h = draw.textsize(msg, font=font_type)
draw.text(((W-w)/2,(H-h)/2), msg, fill="black", font=font_type)

font_type = ImageFont.truetype('Garet-Heavy.ttf',50)
w, h = draw.textsize(msg, font=font_type)
draw.text((((W-w)/2)+5,((H-h)/2)+5), msg, fill=(249,215,18), font=font_type)


image.save("//home//thassi//projects//ibot//source//pcimaker//pictures_new//" + str(n) + ".jpg")
#n += 1
#time.sleep(0.5)

#except:
#    print("alle Bilder wurden umgewandelt")
