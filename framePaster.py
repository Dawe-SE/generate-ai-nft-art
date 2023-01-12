import PIL, os
from PIL import Image

i = 1
for image in os.listdir("img/"):
    src = Image.open("img/"+image)
    frame = Image.open("frame.png").convert("RGBA")

    framed = src.copy()
    framed.paste(frame, (0, 0), frame)
    framed.save("framedimg/"+str(i)+".jpg")
    i = i + 1