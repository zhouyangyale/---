print('hello, world')


print("亲爱的周洋，你好呀")
print('                    wo 还是挺好的')
#range(1,11)

import cv2
import random

# 读取图片
img = cv2.imread('1.png')

# h、w为想要截取的图片大小
h = 80
w = 80

count = 1
while 1:
    # 随机产生x,y  此为像素内范围产生
    y = random.randint(1, 890)
x = random.randint(1, 1480)
# 随机截图
cropImg = img[(y):(y + h), (x):(x + w)]
cv2.imwrite('pic/' + str(count) + '.png', cropImg)
count += 1

while count == 2500:
    break