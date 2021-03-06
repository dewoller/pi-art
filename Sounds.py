#import os
#import sys
import pygame
import time
import logging
import os
logger = logging.getLogger( __name__)
DIR=os.path.dirname(os.path.realpath(__file__))
#import curses


class Sounds:
    def __init__(self, maxSamples = 1):
        logger.debug ("initialising")
        pygame.init()
        self.nSamples = 0
        self.s=[None] * (maxSamples )  # because arrays start at 0
        beep=pygame.mixer.Sound('%s/Beep-sound.ogg' % DIR )
        for i in range(0,maxSamples ):
            soundFile = '%s/music/0%s.ogg' % (DIR, (i+1))
            logger.debug ("looking for %s file" % soundFile )
            if( os.path.isfile( soundFile )):
                self.nSamples = self.nSamples + 1
                self.beep(beep)
                time.sleep(.1)
                self.beep(beep)
                self.s[i]=pygame.mixer.Sound(soundFile)
                self.initialise( i )
                self.beep(beep)
                time.sleep(.5)
                logger.debug ("sound %s loaded" % i)
            logger.debug ("sound file loaded")
        backgroundFilename ='%s/music/background.ogg' % DIR
        if( os.path.isfile( backgroundFilename )):
            background=pygame.mixer.Sound(backgroundFilename)
            self.background(background)

        # set up the mixer
        freq = 44100     # audio CD quality
        bitsize = -16    # unsigned 16 bit
        channels = 2     # 1 is mono, 2 is stereo
        buffer = 1024    # number of samples (experiment to get right sound)
        pygame.mixer.init(freq, bitsize, channels, buffer)

        # optional volume 0 to 1.0
        pygame.mixer.music.set_volume(1.0)

        # starts pygame clock
        clock = pygame.time.Clock()

    def getNSamples(self):
        return self.nSamples

    def beep(self, s):
        pygame.mixer.find_channel().play(s)

    def background(self, s):
        pygame.mixer.find_channel().play(s, loops=-1)

    def initialise(self, n):
        cn=pygame.mixer.Channel(n)
        cn.play( self.s[n], loops=-1)
        cn.pause()

    def start(self, n):
        if n < self.nSamples:
            logger.debug("playing sound %s", n)
            pygame.mixer.Channel(n).unpause()

    def stop(self, n):
        if n < self.nSamples:
            logger.debug("pausing sound %s", n)
            pygame.mixer.Channel(n).pause()

    def quit(self):
        pygame.mixer.quit()

if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    n=3
    time.sleep(10)
    s = Sounds(n)
    for i in range(0,n-1):
        s.start(i)
        s.start(i+1)
        time.sleep(10)
        s.stop(i)
        time.sleep(10)
        s.start(i)
        time.sleep(10)
        s.stop(i)
        s.stop(i+1)
        time.sleep(10)
    s.quit()
