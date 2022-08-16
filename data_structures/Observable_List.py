import sys
from collections import deque
from queue import Queue
from time import sleep

from observer.Observer import Observer
from observer.Observer import Observable

class Observable_List(Observable, list, Observer):

    def __init__(self, events):
        """events is a list"""
        if events is None:
            events = []
        if "lenIsMultipleOf200" not in events:
            #len is the number of elements in the list
            events.append("lenIsMultipleOf200")

        Observable.__init__(self,events)
        list.__init__(self)

    def append(self, object):
        list.append(self, object)

        # get the keys of the dictionary of events
        ks = self.event_observers.keys()
        #for every event of type lenIsMultipleOf check if match
        for k in ks:
            if str(k).startswith("lenIsMultipleOf"):
                number = int(str(k)[len("lenIsMultipleOf"):])
                if (len(self) % number) == 0:
                    e = "lenIsMultipleOf" + str(number)
                    self.notify(e, e)

def main():

    ol = Observable_List(['lenIsMultipleOf100', 'lenIsMultipleOf200'])
    for n in range(0,201):
        ol.append(n)
        sleep(0.01)


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit