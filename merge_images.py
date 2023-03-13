#bin/usr/merge_images

from PIL import Image
import itertools


resultImages = []
resultNames = []


def join_image(imagesArray, variableIndex):
    global resultImages
    global resultNames
    resultImages = []
    resultNames = []
    
    sizes = []
    for img in imagesArray:
        sizes.append(img[0].size)
    widths, heights = zip(*sizes)
    totalHeight = sum(heights)
    max_width = max(widths)

    combinations = list(itertools.product(*variableIndex))
    
    for combination in combinations:
        result = Image.new('RGB', (max_width, totalHeight))
        resultNames.append('_'.join(combination))
        yOffset = 0
        for indexImage, variableNumber in enumerate(combination):
            result.paste(imagesArray[indexImage][int(variableNumber)-1], (0, yOffset))
            yOffset += imagesArray[indexImage][int(variableNumber)-1].size[1]
        resultImages.append(result)