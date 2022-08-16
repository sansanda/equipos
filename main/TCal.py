import sys
from threading import Thread
from time import sleep

from data_loggers_and_statistics.temperature_data_loggers import TemperatureDataLogger
from data_structures.Observable_List import Observable_List
from data_structures.Observable_Queue import Observable_Queue
from logger_and_messages.printing_messages import printMessage
from observer.Observer import Observer
from ovens.Ovens import Oven_I, FakeOven

from temperature.Thermometers import Thermometer_I

import statistics

class TCal(Thread, Observer):

    def __init__(self, threadname="TCal", temperature_profile=[], temperature_stabilization_criteria=(), oven=Oven_I,
                 thermometer=Thermometer_I, results_file=None):
        """

        :param threadname: An str with the name of the thread. :param temperature_profile: A list of integers with
        the temperatures to be applied during the thermal calibration process. :param
        temperature_stabilization_criteria: A tuple with the parameters that define the criteria of the temperature
        stabilization (sampling_period_secs, number_of_samples_of_window, stdev, number_of_consequtive_windows).
        """
        self.n_samples_of_window = temperature_stabilization_criteria[1]
        self.temperature_profile = temperature_profile
        self.temperature_stabilization_criteria = temperature_stabilization_criteria
        self.oven = oven
        self.thermometer = thermometer
        self.results_file = results_file
        self.temp_list = Observable_List(["lenIsMultipleOf" + str(self.n_samples_of_window)])
        self.temp_list.register("lenIsMultipleOf" + str(self.n_samples_of_window), self, self.lenIsMultipleOf_event_handler)

        self.temperature_data_logger = TemperatureDataLogger("temperature_data_logger",
                                                             self.oven,
                                                             self.temp_list,
                                                             self.temperature_stabilization_criteria[0]
                                                             )

        Thread.__init__(self, name=threadname)

    def run(self):
        printMessage("Starting Temperature Calibration Process", "*", "*")

        self.oven.start()
        self.oven.update_temperatureSP(self.temperature_profile[0])
        self.temperature_data_logger.start()

    def lenIsMultipleOf_event_handler(self, message):
        print(message)
        number = int(message[len("lenIsMultipleOf"):])
        # print(self.temp_list[-number:])
        # get the n_samples_of_window samples and calculate the stdev
        stdev = statistics.stdev(self.temp_list[-number:])
        print("stdev = " + str(stdev))


def main():
    fakeOven = FakeOven("fakeOven")
    tCal = TCal("TCal",[100,125,150,175,200],(1, 20, 0.01, 3),fakeOven,fakeOven,None)
    tCal.start()

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
