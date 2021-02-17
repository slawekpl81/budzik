import os
import time
from pygame import mixer

FILE = 'mplayer/astronomia.mp3'
PATH = os.path.abspath(FILE)

class PlaySound:

    @staticmethod
    def play(s_file=PATH, duration_secs=5):
        """Play a sound file for a configurable duration"""

        mixer.init()
        mixer.music.load(s_file)
        mixer.music.play()
        time.sleep(duration_secs)
        mixer.music.stop()
        mixer.quit()


if __name__ == '__main__':
    PlaySound.play(s_file='astronomia.mp3')
