#bin/usr/load_images

import os
from PIL import Image
from natsort import natsorted
import cv2
import numpy as np


variableLists = []
variableImages = []


def load_images(originalImagesPath, variableNames):
    global variableLists
    global variableImages
    # Groups in sublists paths to files with common variable name
    variableLists = [[] for _ in variableNames]
    listado = natsorted(os.listdir(originalImagesPath))
    for fileName in listado:
        for i, name in enumerate(variableNames):
            if name in fileName:
                variableLists[i].append(f'{originalImagesPath}/{fileName}')
                break
    print(variableLists)
    # Groups in sublists images objects with common variable name
    variableImages = [[] for _ in variableNames]
    for i, typeVariable in enumerate(variableLists):
        for image in typeVariable:
            variableImages[i].append(Image.open(image).convert('RGB'))


def save_images(conjointImages, fileNames):
    i = 1
    folderDestinationOriginal= 'Output'
    folderDestination = folderDestinationOriginal
    while os.path.exists(folderDestination):
        i+=1
        folderDestination = f'{folderDestinationOriginal}_V{i}'
    os.mkdir(folderDestination)
    count = 0
    for image, name in zip(conjointImages, fileNames):
        cv2.imwrite(f'{folderDestination}/{name}.png', cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR))
        if count%100==0 or count == len(fileNames)-1:
            print('Images conjoint saved: ', count)
        count += 1

folderPath = 'conjointCBGX/Data/realSimplified'
variables = ['Marca', 'Motor', 'Cambio_Transmisión_Combinación', 'Acabado', 'Precio']
load_images(folderPath, variables)