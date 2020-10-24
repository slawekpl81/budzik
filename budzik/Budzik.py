from datetime import datetime, timedelta


class Budzik:
    def __init__(self, alarm):
        self.hour = alarm.hour
        self.minute = alarm.minute

    @property
    def alarm(self):
        now = datetime.now()
        if now.hour == self.hour and now.minute >= self.minute:
            return True
        return False

    def __str__(self):
        return f'{self.hour}:{self.minute}'
