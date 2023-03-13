#bin/usr/main

from moviepy.editor import *
import time
from humanfriendly import format_timespan
import load_images
import merge_images


def check_file_type_video(filePath):
    if filePath == '':
        print('No file selected')
        return False
    elif filePath[-4:] != '.mp4' or filePath[-5:] == '.mpeg':
        print('Video file format is not valid')
        return False
    return True


def check_file_type_data(filePath):
    if filePath == []:
        print('No file selected')
        return False
    for i in filePath:
        if i[-4:] != '.dat':
            print('Data file format is not valid')
            return False
    return True


def remove_empty_items(dataSelected, captionsSelected, coloursSelected):
    try:
        index  = [index for (index, item) in enumerate(dataSelected) if item == '']
        for i in reversed(index):
            del dataSelected[i]
            del captionsSelected[i]
            del coloursSelected[i]
    except ValueError:
        pass
    return dataSelected, captionsSelected, coloursSelected


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


def get_string_between(string, char1, char2):
    result = ''
    try:
        start = string.rindex(char1)
        end = string.rindex(char2)
        if start >= 0 and end >= 0:
            result = string[start+1: end]
    except ValueError:
        pass
    return result

def get_string_before_last(string, char):
    result = ''
    try:
        end = string.rindex(char)
        if end >= 0:
            result = string[:end]
    except ValueError:
        pass
    return result



##############################     MAIN PROGRAM     ##############################
def main(folderPath, variables, primaryValue, outputName):
    print('Starting program...')
    start = time.time()

    # Check if files and names have been selected
    if folderPath == '':
        print('No folder selected')
        finish_timer(start)
        return
    if variables == []:
        print('No variables selected')
        finish_timer(start)
        return
    if primaryValue == None:
        print('No primary value selected')
        finish_timer(start)
        return
    
    load_images.load_images(folderPath, variables)
    variableIndex = [[] for _ in variables]
    for i, typeVariable in enumerate(load_images.variableLists):
        for name in typeVariable:
            variableIndex[i].append(get_string_between(name, '_', '.'))
    if detect_empty_list(load_images.variableImages) == False:
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
projectName = 'A'
languageName = 'SPTest'
outputName = f'{projectName}{languageName}'
primaryValue = 0
# main(folderPath, variables, primaryValue, outputName)