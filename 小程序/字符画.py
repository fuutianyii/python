# -*- coding: utf-8 -*-
import random
import cv2 as cv
import numpy as np
#opencv-python

#pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-pyth

def img2asciiart(frame, k=5):
    """
    利用聚类将像素信息聚为3或5类，颜色最深的类用数字密集地表示，阴影的类用横杠表示，明亮部分空白表示。
    若字符画结果不好，可以尝试更改K为3。若依然无法很好地表现原图，请换图尝试。
    :param frame: 输入图片数组
    :param k: 聚类数量，大于等于3
    :return: 输出图片数组
    """
    assert isinstance(k, int) and k >= 3, "聚类数量k的值应为大于等于3的整数"
    frame = np.asarray(frame, dtype=np.uint8)

    height, width, *_ = frame.shape  # 有时返回两个值，有时三个值
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_array = np.float32(frame_gray.reshape(-1))

    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv.KMEANS_RANDOM_CENTERS
    compactness, labels, centroids = cv.kmeans(frame_array, k, None, criteria, 10, flags)
    centroids = np.uint8(centroids)

    centroids = centroids.flatten()
    centroids_sorted = sorted(centroids)
    centroids_index = np.array([centroids_sorted.index(value) for value in centroids])

    bright = [abs((3 * i - 2 * k) / (3 * k)) for i in range(1, 1 + k)]
    bright_bound = bright.index(np.min(bright))
    shadow = [abs((3 * i - k) / (3 * k)) for i in range(1, 1 + k)]
    shadow_bound = shadow.index(np.min(shadow))

    labels = labels.flatten()
    labels = centroids_index[labels]
    labels_picked = [labels[rows * width:(rows + 1) * width:2] for rows in range(0, height, 2)]

    canvas = np.zeros((3 * height, 3 * width, 3), np.uint8)
    canvas.fill(255)

    y = 8
    for rows in labels_picked:
        x = 0
        for cols in rows:
            if cols <= shadow_bound:
                cv.putText(canvas, str(random.randint(2, 9)),
                           (x, y), cv.FONT_HERSHEY_PLAIN, 0.45, 1)
            elif cols <= bright_bound:
                cv.putText(canvas, "-", (x, y),
                           cv.FONT_HERSHEY_PLAIN, 0.4, 0, 1)
            x += 6
        y += 6
    return canvas


if __name__ == '__main__':
    file_path = input("path:")
    img = cv.imread(file_path)
    asciiart = img2asciiart(img)
    output=input("output:")
    cv.imwrite(output, asciiart)





