#import os
#import sys
import pygame
import time
#import curses


class Sounds:
    def __init__(self, nSamples = 1):
        print ("initialising\n")
        pygame.init()
        self.nSamples = nSamples
        self.s=[None] * (self.nSamples )  # because arrays start at 0
        for i in range(0,self.nSamples ):
            print ("%s starting" % i)
            self.s[i]=pygame.mixer.Sound('music/0%s.ogg' % (i+1))
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
    n=8
    s = Sounds(n)
    for i in range(0,n):
        print(i)
        s.start(i)
        print("waiting")
        time.sleep(5)
        s.stop(i)
        time.sleep(2)
    s.quit()