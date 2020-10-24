from datetime import datetime, timedelta
from .Budzik import Budzik


class Alarm:
    def __init__(self, delta, text):
        self.hour = 0
        self.minute = 0
        self.text = text
        self.set_time_by_delta(delta)
        self.budzik = Budzik(self)
        self.active = True

    def set_time_by_delta(self, delta):
        now = datetime.now()
        wait = timedelta(minutes=int(delta))
        alarm = now + wait
        self.hour = alarm.hour
        self.minute = alarm.minute

    def set_time(self, time):
        pass

    def __str__(self):
        return f'{self.hour}:{self.minute} - {self.text}'
