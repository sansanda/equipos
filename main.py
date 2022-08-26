from tCal.TCal import TCal
from ovens.Ovens import FakeOven
import sys

def main():
    fakeOven = FakeOven("fakeOven")
    ovenThermometer = fakeOven
    tCal = TCal("TCal",[100,125,150,175,200],(1, 5, 0.01, 3),fakeOven,ovenThermometer,None)
    tCal.start()

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit