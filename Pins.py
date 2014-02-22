import time
from Queue import Queue
from threading import Timer
import logging
logger = logging.getLogger( __name__ )

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    logger.debug("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

        
class Pins:
    def __init__(self, eventQueue):

        self.controlPins={ 3: 0, 5: 1, 7: 2, 11: 3}
        self.state = [None] * 4
        GPIO.setmode(GPIO.BOARD)
        self.eventQueue = eventQueue
        for pin in self.controlPins.keys():
            logger.debug( "initialising pin %s" % pin )
            GPIO.setup( pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            self.state[ self.controlPins[ pin ]]=-100
            #GPIO.add_event_detect( pin, GPIO.BOTH, callback=self.keyEventHandler, bouncetime=1000)

    def poll (self):
        for pin in self.controlPins.keys():
            cstate = GPIO.input(pin)
            pindex = self.controlPins[ pin ]
            if ( cstate != self.state[ pindex ]):
                self.state[pindex] = cstate
                logger.debug( "polled pin %s, pindex %s, currently %s" % (pin,  pindex, cstate))
                self.eventQueue.put( "%s|%s" % (pindex, cstate ))

    def status (self):
        for pin in self.controlPins.keys():
            cstate = GPIO.input(pin)
            pindex = self.controlPins[ pin ]
            logger.debug( "polled pin %s, pindex %s, currently %s" % (pin,  pindex, cstate))

    def keyEventHandler (self, pin):
        state= GPIO.input(pin)
        logger.debug( "handling event from pin %s, pindex %s, currently %s" % (pin,  self.controlPins[ pin ], state))
        self.eventQueue.put( "%s|%s" % (self.controlPins[ pin ], state))



if __name__ == "__main__":
    q = Queue()
    p = Pins(q)
    while (1):
        logger.debug(q)
        logger.debug("waiting")
        time.sleep(10)

    
        
