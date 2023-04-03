combinations = []
primaryKey = 0
variableNumbers = [['1', '2', '3', '4'], [['1', '2'], ['1', '2'], ['1', '2'], ['1', '2']], ['1', '2', '3', '4']]

for iIndex, i in enumerate(variableNumbers):
    temp = []
    for jIndex, j in enumerate(i):
        if type(j) == list:
            print('lista!')
            temp.append[[678]]
        else:
            temp.append(j)
    combinations.append(temp)