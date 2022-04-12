#提取gif的每一帧并且从右往左平铺
from PIL import Image
import os
if os.path.exists("tmp"):
    pass
else:
    os.mkdir("tmp")
gif=Image.open("glance.gif")
while True:
    try:
        num=gif.tell()
        gif.save(f"tmp/{num}.png")
        gif.seek(gif.tell()+1)
    except:
        break

png=Image.new("RGBA",(402,600))
for imagenum in range(0,201):
    png.paste(Image.open(f"tmp/{imagenum}.png"),(imagenum*2,0,imagenum*2+2,600))    

png.save("glance.png")
png.show()
