#!/usr/bin/python
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import daemon
import Dispatcher

import logging
logger = logging.getLogger( __name__ )

logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("/var/log/dispatcher.txt")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

daemonLogFile = open('/var/log/dispatcherLog.txt', 'w')
context = daemon.DaemonContext(
   files_preserve = [
      fh.stream,
   ],
    stdout = daemonLogFile,
    stderr = daemonLogFile
    )


logger.debug( "Before daemonizing." )
context.open()
logger.debug( "After daemonizing." )
with context:
   Dispatcher.go() 
