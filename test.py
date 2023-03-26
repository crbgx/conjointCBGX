#bin/usr/test

from moviepy.editor import *
import time
from humanfriendly import format_timespan
import merge_images
import select_files




def load_images(folderPath, variables):
    # Groups in sublists paths to files with common variable name
    variableLists = [[] for _ in variableNames]
    listado = natsorted(os.listdir(originalImagesPath))
    for fileName in listado:
        for i, name in enumerate(variableNames):
            if name in fileName:
                variableLists[i].append(f'{originalImagesPath}/{fileName}')
                break

    # Groups in sublists images objects with common variable name
    variableImages = [[] for _ in variableNames]
    for i, typeVariable in enumerate(variableLists):
        for image in typeVariable:
            variableImages[i].append(Image.open(image).convert('RGB'))




##############################     MAIN PROGRAM     ##############################
def main(folderPath, variables, primaryValue, outputName, simpleMode):
    print('Starting program...')
    start = time.time()
    
    if check_file_not_empty(folderPath, variables, primaryValue) == False:
        finish_timer(start)
        return

    load_images(folderPath, variables)
    
    variableIndex = select_files.select_files(variables, load_images.variableLists, simpleMode)

    detect_empty_list(load_images.variableImages, start)

    merge_images.join_image(load_images.variableImages, variableIndex)
    finalNamesList = []
    for i in merge_images.resultNames:
        temp = [outputName, i]
        finalNamesList.append('_'.join(temp))
    
    load_images.save_images(merge_images.resultImages, finalNamesList)






















##############################     TEST PROGRAM     ##############################
folderPath = 'conjointCBGX/Data/simplified'
variables = ['Marca', 'Motor', 'Cambio_Transmisión_Combinación', 'Acabado', 'Precio']
primaryValue = 0
projectName = 'A'
languageName = 'SPTest'
outputName = f'{projectName}{languageName}'
simpleMode = True