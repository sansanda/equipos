import sys
from time import sleep
from queue import Queue

from ovens.Ovens import FakeOven
import matplotlib.pyplot as plt


def main():
    fakeOven = FakeOven("fakeOven")
    temperatures_q = Queue()

    time = 0
    l = list()
    fakeOven.start()

    while True:

        temperatures_q.put(fakeOven.get_actual_temperature())
        #print(list(temperatures_q.queue))
        print(time, " - ", temperatures_q.get())

        sleep(1)
        time = time + 1
        if (time % 60) == 0:
            fakeOven.update_temperatureSP(fakeOven.get_temperatureSP() + 25)

    return 0


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
