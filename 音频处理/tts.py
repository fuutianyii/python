'''
Author: fuutianyii
Date: 2023-01-08 20:58:09
LastEditors: fuutianyii
LastEditTime: 2023-01-08 21:00:29
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''
###这是一个基于paddlepaddle的tts，可以本地使用，效果极佳，但是需要强大算力，安装繁琐
from paddlespeech.cli.tts.infer import TTSExecutor
import requests
import os

# tts = TTSExecutor()
# tts(text="老的。",
#     output="old_c.wav",
#     am="speedyspeech_csmsc",#Acoustic models
#     voc="wavernn_csmsc",
#     lang="zh")
##中文，需要不少算力（至少得有gpu），小主机放弃

# tts = TTSExecutor()
# tts(text="astronaut  astronaut.  a s t r o n a u t.   宇航员     brand  brand.  b r a n d.   广告     consider  consider.  c o n s i d e r.   考虑",
#     output="mix2.wav",
#     am="fastspeech2_mix",#Acoustic models
#     voc="style_melgan_csmsc",
#     lang="mix")
# finisheded=time.time()
##混合，但是中文效果不佳

class produce_audio():
    def __init__(self):
        self.tts = TTSExecutor() 
    def complie(self,word,chinese):
        text=""
        text+=word+"   "+word+".   "
        for w in list(word):
            w=w.replace("a","air")
            w=w.replace("o","oh")
            text+=w+"  "
        text+="."
        self.tts(text=text,
            output=f"{word}.wav",
            am="fastspeech2_ljspeech",#Acoustic models
            voc="hifigan_vctk",
            lang="en")
        chinese=chinese.replace(" ","")
        data=requests.get(f"https://fanyi.sogou.com/reventondc/synthesis?text={chinese}&speed=1&lang=zh-CHS&from=translateweb&speaker=5")
        f=open(f"{word}_c.wav","wb")
        f.write(data.content)
        f.close()
        os.system(f"ffmpeg  -y  -i {word}.wav -i {word}_c.wav -filter_complex \"[0:0][1:0]concat=n=2:v=0:a=1[out]\" -map \"[out]\" memorize_audio/{word}.wav")
        print("")
        os.system(f"rm -rf {word}.wav {word}_c.wav")
        return word+"_output.wav"
    
p=produce_audio()


if __name__ == "__main__":
    p.complie("old","老的")
    p.complie("young","年轻的")
    p.complie("film","电影;（给.....）蒙上一层薄膜；把......拍成电影，摄制电影；变得朦胧")
    exit()

# print("第一个完成"+str(finish_one-start))
# print("第二个完成"+str(finished-finish_one))
# print("第三个完成"+str(finisheded-finished))


# am={speedyspeech_csmsc,fastspeech2_csmsc,fastspeech2_ljspeech,fastspeech2_aishell3,fastspeech2_vctk,fastspeech2_mix,tacotron2_csmsc,tacotron2_ljspeech,fastspeech2_male}
# voc={pwgan_csmsc,pwgan_ljspeech,pwgan_aishell3,pwgan_vctk,mb_melgan_csmsc,style_melgan_csmsc,hifigan_csmsc,hifigan_ljspeech,hifigan_aishell3,hifigan_vctk,wavernn_csmsc,pwgan_male}




# am=['speedyspeech_csmsc-zh',
# 'fastspeech2_csmsc-zh',
# 'fastspeech2_aishell3-zh',
# 'fastspeech2_cnndecoder_csmsc-zh',
# 'fastspeech2_male-zh',
# 'fastspeech2_mix-mix']
  
  
  
  
# voc=['tacotron2_csmsc-zh',
# 'pwgan_csmsc-zh',
# 'pwgan_aishell3-zh',
# 'pwgan_male-zh',
# 'mb_melgan_csmsc-zh',
# 'style_melgan_csmsc-zh',
# 'hifigan_csmsc-zh',
# 'hifigan_aishell3-zh',
# 'wavernn_csmsc-zh']



# am=['hifigan_ljspeech-en',
# 'pwgan_ljspeech-en',
# 'tacotron2_ljspeech-en',
# 'fastspeech2_vctk-en',
#  'fastspeech2_ljspeech-en']

# voc=['pwgan_vctk-en',
# 'hifigan_vctk-en']