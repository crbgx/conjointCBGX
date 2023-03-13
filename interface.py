#bin/usr/interface

import PySimpleGUI as sg
import os
import main


countLines = 0
LIMIT = 8
VERTICALSIZE = LIMIT * 31


##############################    FUNCTIONS     ##############################



##############################     INTERFACE     ##############################
sg.theme('DarkTanBlue')

layout = [  
            [sg.Text('Choose the folder where the images are located:')],
            [sg.InputText(key='-FOLDER_PATH-', size = (70, 1)), sg.FolderBrowse()],
            [sg.Text('Project:'), sg.InputText(key = '-PROJECT_NAME-', size = (42, 1))],
            [sg.Text('Language:'), sg.InputText(key = '-LANGUAGE_NAME-', size = (40, 1))],

            [sg.Frame('List of variables to be added',
                [[sg.Text('Add a new variable name:'), sg.B('+', key = '-ADD COLUMN-')],
                [sg.Text('If a variable name is left blank, it will be ignored')],
                [sg.Text('Names must be given exactly like the ones of the images files')],
                [sg.HorizontalSeparator()],
                [sg.Col([[]], scrollable = True, key = '-COLUMN-', s = (500, VERTICALSIZE))]], key = '-FRAME-')
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

    elif event == '-ADD COLUMN-':
        if countLines < LIMIT:
            window.extend_layout(window['-COLUMN-'], [[sg.Text(f'Variable name {countLines}:'),
                                                       sg.InputText(key=f'-VARIABLE_NAME_{countLines}-', enable_events=True, size = (15, 1)),
                                                       sg.Radio('Primary value', '-PRIMARY-', key = f'-PRIMARY_KEY_{countLines}-', default = True if countLines == 0 else False)]])
            window.visibility_changed()
            window['-COLUMN-'].contents_changed()
            countLines += 1
        elif countLines == LIMIT:
            window.extend_layout(window['-COLUMN-'], [[sg.Text(f'No more than {LIMIT} variables can be added')], [sg.HorizontalSeparator()]])
            window.visibility_changed()
            window['-COLUMN-'].contents_changed()
            countLines += 1

    elif event == 'EXECUTE_MAIN':
        for i in range(0,countLines):
            if values[f'-PRIMARY_KEY_{i}-']:
                primaryValue = i
                break
        folderPath = values['-FOLDER_PATH-']
        variableNames = [values[f'-VARIABLE_NAME_{i}-'] for i in range(0,countLines)]
        projectName = values['-PROJECT_NAME-']
        languageName = values['-LANGUAGE_NAME-']
        outputName = f'{projectName}{languageName}'
        main.main(folderPath, variableNames, primaryValue, outputName)
    
window.close()