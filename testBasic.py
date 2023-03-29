from natsort import natsorted
from PIL import Image
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

folderPath = 'conjointCBGX/Data/realSimplified'
variables = ['Marca', 'Motor', 'Cambio_Transmisión_Combinación', 'Acabado', 'Precio']
primaryValue = 0
secondaryValue = [False, False, False, False, True]

primaryValueLength = variables[primaryValue]
variableLists = [[] for _ in variables]
listado = natsorted(os.listdir(folderPath))
listadoSimple = [get_string_before_last(i, '_') for i in listado]
countPrimary = listadoSimple.count(variables[primaryValue])
#print(countPrimary)
temp0 = variables[0]

counter = 0
tempList = []
tempImageList = []
variableImages = [[] for _ in variables]
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
                variableImages[i].append(Image.open(imagePath).convert('RGB'))
            else:
                counter += 1
                tempList.append(imagePath)
                tempImageList.append(Image.open(imagePath).convert('RGB'))
                temp1 = get_string_before_last(step2, '_')
                if counter == countPrimary + 1:
                    variableLists[i].append(tempList)
                    variableImages[i].append(tempImageList)
                    tempList = []
                    tempImageList = []
                    counter = 0
            break

print(variableLists)
print(variableImages)
