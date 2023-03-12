#bin/usr/merge_images

from PIL import Image


def join_image():
    topImage = Image.open('Data/image1.png')
    lowerImage =Image.open('Data/image2.png')
    result = Image.new('RGB', (topImage.width, topImage.height + lowerImage.height))
    result.paste(topImage, (0, 0))
    result.paste(lowerImage, (0, topImage.height))
    result.save('Data/joined.png')