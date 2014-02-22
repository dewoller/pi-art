#import os
#import sys
import pygame
import time
import logging
logger = logging.getLogger( __name__)
#import curses


class Sounds:
    def __init__(self, nSamples = 1):
        logger.debug ("initialising")
        pygame.init()
        self.nSamples = nSamples
        self.s=[None] * (self.nSamples )  # because arrays start at 0
        beep=pygame.mixer.Sound('Beep-sound.ogg' )
        for i in range(0,self.nSamples ):
            logger.debug ("sound %s loading" % i)
            print ("%s starting" % i)
            self.beep(beep)
            self.s[i]=pygame.mixer.Sound('music/0%s.ogg' % (i+1))
            self.beep(beep)
            self.beep(beep)
            logger.debug ("sound %s loaded" % i)
            print ("... completed")

        # set up the mixer
        freq = 44100     # audio CD quality
        bitsize = -16    # unsigned 16 bit
        channels = 2     # 1 is mono, 2 is stereo
        buffer = 2048    # number of samples (experiment to get right sound)
        pygame.mixer.init(freq, bitsize, channels, buffer)

        # optional volume 0 to 1.0
        pygame.mixer.music.set_volume(1.0)

        # starts pygame clock
        clock = pygame.time.Clock()

    def beep(self, s):
        pygame.mixer.Channel(0).play(s)
        time.sleep(.5)

    def start(self, n):
        cn=pygame.mixer.Channel(n)
        if (not cn.get_busy()):
            cn.play( self.s[n], loops=-1)

    def stop(self, n):
        cn=pygame.mixer.Channel(n)
        if (cn.get_busy()) :
            cn.stop( )

    def quit(self):
        pygame.mixer.quit()

if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    n=8
    s = Sounds(n)
    for i in range(0,n):
        logger.debug(i)
        s.start(i)
        logger.debug("playing sound ", i)
        time.sleep(5)
        s.stop(i)
        time.sleep(2)
    s.quit()
