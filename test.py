#bin/usr/test

from moviepy.editor import *
import time
from humanfriendly import format_timespan
from natsort import natsorted
import merge_images
import select_files
from PIL import Image
import main


relativeVaribles = []

def load_images(folderPath, variables):
    # Groups in sublists paths to files with common variable name
    variableLists = [[] for _ in variables]
    listado = natsorted(os.listdir(folderPath))
    for fileName in listado:
        for i, name in enumerate(variables):
            if name in fileName:
                variableLists[i].append(f'{folderPath}/{fileName}')
                break

    # Groups in sublists images objects with common variable name
    variableImages = [[] for _ in variables]
    for i, typeVariable in enumerate(variableLists):
        for image in typeVariable:
            variableImages[i].append(Image.open(image).convert('RGB'))

    #prueba = {'Test':'Test1'}, {'Test':'Test2'}
    #prueba.append({'Test3': 'Test4'})
    print(listado)
    print(variableLists)
    print(variableImages)
    # print(prueba)
    # print(prueba['Test'])




##############################     MAIN PROGRAM     ##############################
def main(folderPath, variables, primaryValue, outputName, simpleMode):
    print('Starting program...')
    start = time.time()
    
    if main.check_file_not_empty(folderPath, variables, primaryValue) == False:
        main.finish_timer(start)
        return

    load_images(folderPath, variables)
    
    variableIndex = select_files.select_files(variables, load_images.variableLists, simpleMode)

    main.detect_empty_list(load_images.variableImages, start)

    merge_images.join_image(load_images.variableImages, variableIndex)
    finalNamesList = []
    for i in merge_images.resultNames:
        temp = [outputName, i]
        finalNamesList.append('_'.join(temp))
    
    load_images.save_images(merge_images.resultImages, finalNamesList)



folderPath = 'conjointCBGX/Data/real'
variables = ['Marca', 'Motor', 'Cambio_Transmisión_Combinación', 'Acabado', 'Precio']
load_images(folderPath, variables)

















##############################     TEST PROGRAM     ##############################
folderPath = 'conjointCBGX/Data/simplified'
variables = ['Marca', 'Motor', 'Cambio_Transmisión_Combinación', 'Acabado', 'Precio']
primaryValue = 0
projectName = 'A'
languageName = 'SPTest'
outputName = f'{projectName}{languageName}'
simpleMode = True