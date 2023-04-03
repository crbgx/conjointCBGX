import itertools
from PIL import Image


combinations = []
primaryKey = 0
secondaryKey = 1
variables = ['Marca', 'Precio', 'Acabado']
variableNumbers = [['1', '2', '3', '4'], ['1','2'], ['1', '2', '3', '4']]


sizes = []
for array in variableImages:
    img = array[0]
    if type(img) == list:
        img = img[0]
    sizes.append(img.size)
widths, heights = zip(*sizes)
totalHeight = sum(heights)
max_width = max(widths)


combinations = list(itertools.product(*variableNumbers))

print(combinations)

resultNames = []
variableImages = []
resultImages = []

for combination in combinations:
    result = Image.new('RGB', (max_width, totalHeight))
    resultNames.append('_'.join(combination))
    yOffset = 0
    for indexImage, variableNumber in enumerate(combination):
        if indexImage == primaryKey:
            keyValue = variableNumber
        if indexImage == secondaryKey:
            result.paste(variableImages[indexImage][keyValue][int(variableNumber)-1], (0, yOffset))
            yOffset += variableImages[indexImage][keyValue][int(variableNumber)-1].size[1]
        else:
            result.paste(variableImages[indexImage][int(variableNumber)-1], (0, yOffset))
            yOffset += variableImages[indexImage][int(variableNumber)-1].size[1]
    resultImages.append(result)