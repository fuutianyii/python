import cv2
#opencv-python

#pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python

str = 'mqpka89045321@#$%^&*()_=||||}' # 字符表
path=input()
im = cv2.imread(path)    # 读取图像
grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)    # 灰度转换
grey = cv2.resize(grey, (100, 50))    # 缩小图像
str_img = ''    # 用于装字符画
for i in grey:    # 遍历每个像素
    for j in i:
        index = int(j / 256 * len(str))    # 获取字符坐标
        str_img += str[index]    # 将字符添加到字符画中
    str_img += '\n'
print(str_img)