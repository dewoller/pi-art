import time
from Queue import Queue
from threading import Timer
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

        
class Pins:
    def __init__(self, eventQueue):

        self.controlPins={ 3: 1, 5: 2, 7: 3, 11: 4}
        GPIO.setmode(GPIO.BOARD)
        self.eventQueue = eventQueue
        for pin in self.controlPins.keys():
            print pin
            GPIO.setup( pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect( pin, GPIO.BOTH, callback=self.keyEventHandler, bouncetime=1000)

    def status (self):
        for pin in self.controlPins.keys():
            print "pin: %s\tstatus:%s\n" %(pin, GPIO.input(pin))

    def keyEventHandler (self, pin):
        state= GPIO.input(pin)
        print "handling button event from pin %s, number %s, currently %s\n" % (pin,  self.controlPins[ pin ], state)

        #timer.sleep(0.5)
        #if (state== GPIO.input(pin) | state == 1):
        self.eventQueue.put( "%s|%s" % (self.controlPins[ pin ], GPIO.input(pin)))



if __name__ == "__main__":
    q = Queue()
    p = Pins(q)
    while (1):
        print(q)
        print("waiting")
        time.sleep(10)

    
        
