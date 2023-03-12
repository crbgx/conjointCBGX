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
def main(folderPath, variableNames, outputName):
    print('Starting program...')
    start = time.time()
    load_images.load_images(folderPath, variableNames)
    finish_timer(start)


folderPath = '/Data'
variableNames = ['Marca', 'Motor', 'Cambio_Transmisión_Combinación', 'Transmision', 'Acabado', 'Precio']
projectName = 'A'
languageName = 'SPTest'
outputName = f'{projectName, languageName}'
#main(folderPath, variableNames, outputName)