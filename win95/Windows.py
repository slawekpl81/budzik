import PySimpleGUI as sg


class BudzikWindow:

    def __init__(self):
        layout = [
            [sg.Text(size=(10,2), font=('Helvetica', 30), key='-WATCH-', justification='center')],
            [sg.Text('wake up in...minutes')],
            [sg.Text('minutes:'), sg.In(key='-MINUTES-', size=(5, 1))],
            [sg.Text('alarm text:'), sg.In(key='-AlarmText-', size=(10, 1))],
            [sg.Button('OK', key='-OK-')],
            [sg.Text('alarms:'), sg.Listbox(values=[], size=(15, 5), key='-AlarmsList-')],
        ]
        sg.theme('HotDogStand')
        self.window = sg.Window('PyBudzik', layout, margins=(100, 50))
        self.minutes = 0
        self.alarm_text = ''

    def loop(self):
        event, values = self.window.read(timeout=10)
        if event == '-OK-':
            if values['-MINUTES-'].isdigit():
                self.minutes = values['-MINUTES-']
                self.alarm_text = values['-AlarmText-']
                self.reset()
                return 'ok'
        # if event == '-AlarmsList-':
        #     if values['-AlarmsList-']:
        #         self.remove_obj = values['-AlarmsList-'][0]
        #         print(f'remove item:{self.remove_obj}')
        #         print(f'type of remover: {type(self.remove_obj)}')
        if event == sg.WIN_CLOSED:
            return 'close'


    def alarm(self, text):
        sg.popup(f'!!! {text} !!!')

    def reset(self):
        self.window['-MINUTES-'].update('')
        self.window['-AlarmText-'].update('')

    def update_win(self, alarms_list, time):
        # print(f'alarms_list:{alarms_list}')
        self.window['-AlarmsList-'].update(alarms_list)
        self.window['-WATCH-'].update(time)


if __name__ == '__main__':
    pass
