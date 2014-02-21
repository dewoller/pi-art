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



q = Queue()
p=Pins( q )
s= Sounds( 4 )

while True:
    try:
        payload = q.get(True, 20)
        process( payload, s)
        p.status()
        q.task_done()
    except Exception as e:
            print e
    




