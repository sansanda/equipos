from threading import Thread
from time import sleep

from logger_and_messages.printing_messages import printMessage


class update_mu_and_sigma_task(Thread):
    def __init__(self, threadname, thermometer, period_secs=2):
        self.thermometer = thermometer
        self.period_secs = period_secs
        Thread.__init__(self, name=threadname)

    def run(self):
        while(True):
            printMessage("Updating thermometer parameters....", "*", "*")
            self.thermometer.updateParameters(self.thermometer.getParameters()[0], self.thermometer.getParameters()[1]*0.99)
            sleep(self.period_secs)