#bin/usr/load_images

import glob
import os
from PIL import Image

def load_images(originalImagesPath, variableNames):
    originalImages = glob.glob(originalImagesPath + '/*.jpg')
    originalImages.sort()
    originalImagesOrganized = []
    for images in originalImages:
        for name in variableNames:
            temporalArray = []
            if name in images:
                temporalArray.append(images)
                break
        originalImagesOrganized.append(temporalArray)
            
    image = Image.open('Data/joined.png')
    image.show()

def save_images(conjointImages):
    i = 1
    folderDestination = f'Output_V{i}'
    while os.path.exists(folderDestination):
        i+=1
        folderDestination = f'{folderDestination}_V{i}'
    for image in conjointImages:
        image.save(f'{folderDestination}/{image.filename}')