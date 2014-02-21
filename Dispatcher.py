#import pdb ;pdb.set_trace()
from Sounds import Sounds
from Pins import Pins
from Queue import Queue


def process( payload, s):
    print("processing payload %s" % payload)
    (pin,status)=payload.split('|')
    pin = int(pin)
    #pdb.set_trace()
    if status == "0":
        s.start(pin)
    else:
        s.stop(pin)


def go():

    q = Queue()
    p=Pins( q )
    s= Sounds( 4 )

    while True:
        try:
            p.poll()
            payload = q.get(True, 1)
            process( payload, s)
            p.status()
            q.task_done()
        except Exception as e:
                print e
        

if __name__ == "__main__":
       go()

