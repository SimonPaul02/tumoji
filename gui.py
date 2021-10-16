import PySimpleGUI as sg

col = [[sg.Text('This is the first line')],
       [sg.In()],
       [sg.Button('Save'), sg.Button('😎')]]

layout = [[sg.Column(col, key='-COLUMN-'), ]]  # put entire layout into a column so it can be saved

window = sg.Window("Tumoji", layout, size=(750, 500), element_justification='c')

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, '😎'):
        break  # exit
    elif event == 'Save':
        print("alfdkasdölf")


window.close()


