#!/home/slawekj/Documents/budzik/venv/bin/python3
import sys
import subprocess
from datetime import datetime, timedelta
import time
from win95.Windows import BudzikWindow
from budzik.Budzik import Budzik
from budzik.Alarm import Alarm
from mplayer.player import PlaySound 


if __name__ == '__main__':
    budzikWin = BudzikWindow()
    alarms = set()
    alarms_text = set()

    while True:
        response = budzikWin.loop()

        if response == 'ok':
            alarms.add(Alarm(delta=budzikWin.minutes, text=budzikWin.alarm_text))

        if response == 'close':
            break
            
        for alarm in alarms:
            if alarm.budzik.alarm:
                PlaySound.play()
                budzikWin.alarm(alarm.__str__())
                alarms.remove(alarm)
                break
        alarms_text = set()
        for alarm in alarms:
            alarms_text.add(alarm.__str__())
        now = f'{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}'
        budzikWin.update_win(alarms_text, now)