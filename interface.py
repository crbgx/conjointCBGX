#bin/usr/interface

import PySimpleGUI as sg
import main


countLines = 0
LIMIT = 8
VERTICALSIZE = LIMIT * 31


##############################    FUNCTIONS     ##############################
def create_row(disabled):
    global countLines
    row = [ sg.Text(f'Variable name {countLines}:'),
            sg.InputText(key=f'-VARIABLE_{countLines}-', enable_events = True, size = (20, 1)), sg.FileBrowse(file_types = [('JPG file', '*.jpg'), ('PNG file', '*.png')]),
            sg.Radio('Primary', '-PRIMARY-', key = f'-PRIMARY_KEY_{countLines}-', default = True if countLines == 0 else False, disabled = disabled),
            sg.Checkbox('Secondary', default = False, key = f'-SECONDARY_VALUES_{countLines}-', disabled = disabled)]
    countLines += 1
    return row


def update_variable_name(i):
    newName = main.get_string_between(values[f'-VARIABLE_{i}-'], '/', '.')
    newName = main.get_string_before_last(newName, '_')
    if main.has_numbers(newName):
        newName = main.get_string_before_last(newName, '_')
    if newName == '':
        return
    window[f'-VARIABLE_{i}-'].Update(newName)


##############################     INTERFACE     ##############################
sg.theme('DarkTanBlue')

layout = [  
            [sg.Text('Choose the folder where the images are located:')],
            [sg.InputText(key = '-FOLDER_PATH-', size = (70, 1)), sg.FolderBrowse()],
            [sg.Text('Project:'), sg.InputText(key = '-PROJECT-', size = (42, 1))],
            [sg.Text('Language:'), sg.InputText(key = '-LANGUAGE-', size = (40, 1))],
            [sg.Text('Execution mode:'), sg.Radio('Simple', '-MODE-', key = '-SIMPLE_MODE-', default = True, enable_events = True), sg.Radio('Relative', '-MODE-', key = '-RELATIVE_MODE-', default = False, enable_events = True)],

            [sg.Frame('List of variables to be added',
                [[sg.Text('Add a new variable name:'), sg.B('+', key = '-ADD COLUMN-')],
                [sg.Text('If a variable name is left blank, it will be ignored')],
                [sg.Text('Names must be given exactly like the ones of the images files')],
                [sg.HorizontalSeparator()],
                [sg.Col([create_row(True) for _ in range(0,2)], scrollable = True, key = '-COLUMN-', s = (500, VERTICALSIZE))
                        ]], key = '-FRAME-')
            ],
            
            [sg.Button('Create merged images', key = 'EXECUTE_MAIN'), sg.Exit()]
        ]

window = sg.Window('ConjointCBGX', layout, finalize = True, resizable = True)


##############################     EVENT LOOP     ##############################
while True:      
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        print('Exiting program...')
        break

    elif event == '-SIMPLE_MODE-':
        for i in range(0, countLines):
            window[f'-PRIMARY_KEY_{i}-'].update(disabled = True)
            window[f'-SECONDARY_VALUES_{i}-'].update(disabled = True)

    elif event == '-RELATIVE_MODE-':
        for i in range(0, countLines):
            window[f'-PRIMARY_KEY_{i}-'].update(disabled = False)
            window[f'-SECONDARY_VALUES_{i}-'].update(disabled = False)

    elif event == '-ADD COLUMN-':
        if countLines < LIMIT:
            if values['-SIMPLE_MODE-'] == True:
                disabled = True
            else:
                disabled = False
            window.extend_layout(window['-COLUMN-'], [create_row(disabled)])
            window.visibility_changed()
            window['-COLUMN-'].contents_changed()
        elif countLines == LIMIT:
            window.extend_layout(window['-COLUMN-'], [[sg.Text(f'No more than {LIMIT} variables can be added')], [sg.HorizontalSeparator()]])
            window.visibility_changed()
            window['-COLUMN-'].contents_changed()
            countLines += 1

    elif event == 'EXECUTE_MAIN':
        simpleMode = True if values['-SIMPLE_MODE-'] else False
        primaryValue = None
        if simpleMode == False:
            for i in range(0,countLines):
                if values[f'-PRIMARY_KEY_{i}-']:
                    primaryValue = i
                    break
        folderPath = values['-FOLDER_PATH-']
        variables = [values[f'-VARIABLE_{i}-'] for i in range(0,countLines)]
        project = values['-PROJECT-']
        laguage = values['-LANGUAGE-']
        outputName = f'{project}{laguage}'
        secondaryValue = None
        if simpleMode == False:
            secondaryValue = [values[f'-SECONDARY_VALUES_{i}-'] for i in range(0,countLines)]
        main.main(folderPath, variables, primaryValue, outputName, simpleMode)

    # Update variableName when data file is selected
    elif event == '-VARIABLE_0-':
        i = 0
        update_variable_name(i)
    
    elif event == '-VARIABLE_1-':
        i = 1
        update_variable_name(i)
    
    elif event == '-VARIABLE_2-':
        i = 2
        update_variable_name(i)
    
    elif event == '-VARIABLE_3-':
        i = 3
        update_variable_name(i)
    
    elif event == '-VARIABLE_4-':
        i = 4
        update_variable_name(i)
    
    elif event == '-VARIABLE_5-':
        i = 5
        update_variable_name(i)
    
    elif event == '-VARIABLE_6-':
        i = 6
        update_variable_name(i)
    
    elif event == '-VARIABLE_7-':
        i = 7
        update_variable_name(i)
    
    elif event == '-VARIABLE_8-':
        i = 8
        update_variable_name(i)
    
    
window.close()