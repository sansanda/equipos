import sys
from delays.delay import Time_Delay
import keyboard

def main():

    tDelay = Time_Delay(2000)
    tDelay.start()

    print("Hola")


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
