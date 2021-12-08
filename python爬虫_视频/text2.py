import ffmpy3
ffmpy3.FFmpeg(inputs={'http://youku.com-youku.net/20180614/11920_4c9e1cc1/index.m3u8': None}, outputs={'1.mp4':None}).run()
# yourm3u8='https://www.iqiyi.com/v_19rz544sj4.html?vfrm=pcw_home&vfrmblk=D&vfrmrst=712211_focus_A_image1'
# a = FFmpeg(
#                  inputs={'https://www.iqiyi.com/v_19rz544sj4.html?vfrm=pcw_home&vfrmblk=D&vfrmrst=712211_focus_A_image1': None},
#                  outputs={'1.mp4': '-c copy',
#                           }
# )
# a.run()

# import os
# os.system("ffmpeg -i 'https://youku.cdn7-okzy.com/20200407/18551_93112350/index.m3u8' -acodec copy -vcodec copy 1.mp4")

