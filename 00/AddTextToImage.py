from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

im = Image.open("resource/test.jpg")

font = ImageFont.truetype('Arial.ttf', 150)
draw = ImageDraw.Draw(im)
(x,y) = im.size
draw.text((x-150,50),"3",(255,0,0),font=font)

draw = ImageDraw.Draw(im)

im.save("resource/resoult.jpg")
