import video2
import os

# def downall():
#     f=open("./python爬虫_视频/m3u8.txt")
#     m3u8line=f.readlines()
#     for url in m3u8line:
#         url=url.replace("\n", "")
#         print(url)  
#         video2.video(url)
 
def rename():
    filelist=os.listdir("F://ts")
    startname=28
    for file in filelist:
        if file[-4::]==".mp4":

            print(file)
            os.rename("f://ts/"+file,"f://ts/"+str(startname)+".mp4")
            print(file+"===>"+str(startname)+".mp4")
            startname+=1

# downall()
rename()



# https://www.sppmc.com/




# http://www.mycctv.cn/edu51891-2-1.html *************