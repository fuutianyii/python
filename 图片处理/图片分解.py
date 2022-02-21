from PIL import Image
import os
try:
    os.mkdir("tmp")
except:
    pass
print("工作路径"+os.getcwd())
# 此程序将图片拆分图片为多个10x10的图片


outdir="tmp/"

img=Image.open("1.png")
width=img.size[0]
heigh=img.size[1]
tpoord=0
rpoord=10
bpoord=10
lpoord=0

imgname=1
while ((bpoord <=heigh) and (rpoord <=width)):
    cliping=img.crop((lpoord,tpoord,rpoord,bpoord))
    result_image = Image.new('RGB', (10,10), (0,0,0,0)) #mode, result size, color
    result_image.paste(cliping,(0,0,10,10), mask=0)
    result_image.save(outdir+f"{imgname}.png")
    print("produce "+outdir+f"{imgname}.png")
    imgname+=1
    lpoord+=10
    rpoord+=10
    if rpoord>heigh:
        rpoord=10
        lpoord=0
        bpoord+=10
        tpoord+=10