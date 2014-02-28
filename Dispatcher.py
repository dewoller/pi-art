#import pdb ;pdb.set_trace()
from Sounds import Sounds
from Pins import Pins
from Queue import Queue
import logging
logger = logging.getLogger( __name__ )


def process( payload, s):
    logger.debug("processing payload %s" % payload)
    (pin,status)=payload.split('|')
    pin = int(pin)
    #pdb.set_trace()
    if status == "1":
        s.start(pin)
    else:
        s.stop(pin)


def go():

    q = Queue()
    p=Pins( q )
    logger.debug("Loading Sounds")
    s= Sounds( 4 )
    logger.debug("Sounds Loaded")

    while True:
        try:
            p.poll()
            payload = q.get(True, 1)
            process( payload, s)
            p.status()
            q.task_done()
        except Exception as e:
                pass
        

if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.debug("starting")

    go()

