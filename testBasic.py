from natsort import natsorted
from PIL import Image
import numpy as np
import cv2
import os

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

def get_string_after_last(string, char1):
    last_slash_index = string.rfind(char1)
    if last_slash_index == -1: return ''
    result = string[last_slash_index+1:]
    return result


# folderPath = 'conjointCBGX/Data/simplified'
folderPath = 'conjointCBGX/Data/realSimplified'
variables = ['Marca', 'Motor', 'Cambio_Transmisión_Combinación', 'Acabado', 'Precio']
primaryValue = 0
secondaryValue = [False, False, False, False, True]
projectName = 'A'
languageName = 'SPTest'
outputName = f'{projectName}{languageName}'

# primaryValueLength = variables[primaryValue]
variableLists = [[] for _ in variables]
listado = natsorted(os.listdir(folderPath))
listadoSimple = [get_string_before_last(i, '_') for i in listado]
countPrimary = listadoSimple.count(variables[primaryValue])

counter = 0
tempList = []
tempImageList = []
tempNumberList = []
variableNumbers = [[] for _ in variables]
for fileName in listado:
    for i, name in enumerate(variables):
        if name in fileName:
            relativeNumber = get_string_between(fileName, '_', '.')
            step2 = get_string_before_last(fileName, '_')
            variableNameNumber = get_string_after_last(step2, '_')
            relativeIsANumber = variableNameNumber.isdigit()
            imagePath = f'{folderPath}/{fileName}'
            if relativeIsANumber == False:
                variableLists[i].append(imagePath)
                variableNumbers[i].append(relativeNumber)
            else:
                counter += 1
                tempList.append(imagePath)
                tempNumberList.append(relativeNumber)
                tempImageList.append(Image.open(imagePath).convert('RGB'))
                if counter == countPrimary + 1:
                    variableLists[i].append(tempList)
                    variableNumbers[i].append(tempNumberList)
                    tempList = []
                    tempImageList = []
                    tempNumberList = []
                    counter = 0
            break

sizes = []
for array in variableImages:
    img = array[0]
    if type(img) == list:
        img = img[0]
    sizes.append(img.size)
widths, heights = zip(*sizes)
totalHeight = sum(heights)
max_width = max(widths)
        

combinations = [[]]
for k, lst in enumerate(variableNumbers):
    #print('lst', lst)
    temp = []
    for iIndex, i in enumerate(lst):
        if k == primaryValue:
            primaryKey = iIndex
        #print('i', i)
        for jIndex, j in enumerate(combinations):
            #print('j', j)
            if type(i) == list:
                #print(i)
                temp.append(j[primaryKey] + list(i))
            else:
                temp.append(j+[i])
    combinations = temp


resultImages = []
resultNames = []
for combination in combinations:
    result = Image.new('RGB', (max_width, totalHeight))
    resultNames.append('_'.join(combination))
    yOffset = 0
    for indexImage, variableNumber in enumerate(combination):
        result.paste(variableImages[indexImage][int(variableNumber)-1], (0, yOffset))
        yOffset += variableImages[indexImage][int(variableNumber)-1].size[1]
    resultImages.append(result)

finalNamesList = []
for i in resultNames:
    temp = [outputName, i]
    finalNamesList.append('_'.join(temp))

i = 1
folderDestinationOriginal = 'Output'
folderDestination = folderDestinationOriginal
while os.path.exists(folderDestination):
    i+=1
    folderDestination = f'{folderDestinationOriginal}_V{i}'
os.mkdir(folderDestination)

count = 0
for image, name in zip(resultImages, finalNamesList):
    cv2.imwrite(f'{folderDestination}/{name}.png', cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR))
    if count%100==0 or count == len(finalNamesList)-1:
        print('Images conjoint saved: ', count)
    count += 1