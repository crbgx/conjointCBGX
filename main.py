#bin/usr/main

from moviepy.editor import *
import time
from humanfriendly import format_timespan
import load_images
import merge_images
import select_files


def detect_empty_list(listOfLists):
    for index, list in enumerate(listOfLists):
        if list == []:
            print(f'ERROR: Variable {index} hasn\'t been found.')
            print('Please check the names of the variables')
            return False
    return True


def finish_timer(start):
    stop = time.time()
    seconds = round(stop - start, 0)
    print('Finishing program...')
    print('Elapsed time: ', format_timespan(seconds))


def check_file_not_empty(folderPath, variables, primaryValue):
    if folderPath == '':
        print('No folder selected')
        return False
    if variables == []:
        print('No variables selected')
        return False
    if primaryValue == None:
        print('No primary value selected')
        return False
    return True

##############################     MAIN PROGRAM     ##############################
def main(folderPath, variables, primaryValue, outputName, simpleMode):
    print('Starting program...')
    start = time.time()
    
    if check_file_not_empty(folderPath, variables, primaryValue) == False:
        finish_timer(start)
        return

    load_images.load_images(folderPath, variables)
    
    #Aqui meter select_files()
    variableIndex = select_files.select_files(variables, load_images.variableLists, simpleMode)

    if detect_empty_list(load_images.variableImages) == False:
        print('No files where found with those names')
        finish_timer(start)
        return

    merge_images.join_image(load_images.variableImages, variableIndex)
    finalNamesList = []
    for i in merge_images.resultNames:
        temp = [outputName, i]
        finalNamesList.append('_'.join(temp))
    
    load_images.save_images(merge_images.resultImages, finalNamesList)
    finish_timer(start)


folderPath = 'conjointCBGX/Data'
variables = ['Marca', 'Motor', 'Cambio_Transmisión_Combinación', 'Acabado', 'Precio']
primaryValue = 0
projectName = 'A'
languageName = 'SPTest'
outputName = f'{projectName}{languageName}'
simpleMode = True
main(folderPath, variables, primaryValue, outputName, simpleMode)