import random
# tolid adade random
import cv2
# baaraye pardazesh tasvir

T = 0.5
White = (255, 255, 255)
Black = (0, 0, 0)
image = cv2.imread('E:\\MY FILES\\PROJECTS\\Graphic\\png')
height, width, channels = image.shape
TenPerNoise = height * width * 0.1
TenPerNoise = int(TenPerNoise)
for x in range(TenPerNoise):
    col = random.randint(0, height - 1)
    hor = random.randint(0, width - 1)
    blackORwhite = random.random()
    if blackORwhite <= T:
        image[col, hor] = White

    if blackORwhite > T:
        image[col, hor] = Black


cv2.imshow('Noisy Pic', image)
DenoisedImage = cv2.fastNlMeansDenoisingColored(image, None, 40, None, 3, 9)
cv2.imshow('Denoised image', DenoisedImage)

cv2.waitKey(0)
