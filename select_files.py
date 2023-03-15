#usr/bin/select_files

def select_files(variables, variableLists, simpleMode):
    variableIndex = [[] for _ in variables]
    if simpleMode:
        for i, typeVariable in enumerate(variableLists):
            for name in typeVariable:
                variableIndex[i].append(get_string_between_last(name, '_', '.'))
    else:
        for i, typeVariable in enumerate(variableLists):
            for name in typeVariable:
                variableIndex[i].append(get_string_between_last(name, '/', '.'))
    return variableIndex


##############################     AUXILIAR FUNCTIONS     ##############################
def get_string_between_last(string, char1, char2):
    last_slash_index = string.rfind(char1)
    if last_slash_index == -1: return ''
    last_dot_index = string.rfind(char2)
    if last_dot_index == -1: return ''
    result = string[last_slash_index+1:last_dot_index]
    return result


def get_string_between_sames(string, char1):
    last_slash_index = string.find(char1)
    if last_slash_index == -1: return ''
    last_dot_index = string.rfind(char1)
    if last_dot_index == -1: return ''
    result = string[last_slash_index+1:last_dot_index]
    return result


def get_string_after_last(string, char1):
    last_slash_index = string.rfind(char1)
    if last_slash_index == -1: return ''
    result = string[last_slash_index+1:]
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