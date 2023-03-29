from natsort import natsorted
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

counter = -1
tempList = []
for fileName in listado:
    for i, name in enumerate(variables):
        if name in fileName:
            relativeNumber = get_string_between(fileName, '_', '.')
            #print(relativeNumber)
            step2 = get_string_before_last(fileName, '_')
            #print(step2)
            variableNameNumber = get_string_after_last(step2, '_')
            #print(variableNameNumber)
            relativeIsANumber = variableNameNumber.isdigit()
            #print(relativeIsANumber)
            if relativeIsANumber == False:
                variableLists[i].append(f'{folderPath}/{fileName}')
            else:
                counter += 1
                tempList.append(f'{folderPath}/{fileName}')
                temp1 = get_string_before_last(step2, '_')
                if counter == countPrimary:
                    # print(tempList)
                    # print('actualizamos')
                    variableLists[i].append(tempList)
                    tempList = []
                    counter = -1
                # if temp1 != temp0:
                #     print('actualizamos')
                    #variableLists[i] = [[] for _ in variables]

                # print(temp1)
                # print('es complejo')
                #variableLists[int(relativeNumb)][int(relativeNumber)].append(f'{folderPath}/{fileName}')
            break

print(variableLists)