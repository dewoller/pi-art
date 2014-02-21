import os
import sys
import pygame
import curses
pygame.init()
loop = 0
esc = 0

n=5
s=[None] * 9
for i in range(1,9):
    s[i]=pygame.mixer.Sound('music/0%s.ogg' % i)



#init the curses screen
stdscr = curses.initscr()

#use cbreak to not require a return key press
curses.cbreak()
curses.noecho()

track = 0
breaker = 0

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

while breaker == 0:
    # python curses to 'get' keyboard input
    k = stdscr.getch()
    kn = curses.keyname(k)
    if (kn >='1') & (kn <='8'):
        i=int(kn)
        cn=pygame.mixer.Channel(i-1)
        if (cn.get_busy()) :
            stdscr.addstr( "%s stopped" % kn )
            cn.stop()
        else:
            stdscr.addstr( "%s started" % kn )
            cn.play( s[i] )
    # press q to quit
    elif kn=="q":
        pygame.mixer.quit()
        breaker = 1
        curses.endwin()

