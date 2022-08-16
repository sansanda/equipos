from queue import Queue
from threading import Thread
from time import sleep

from logger_and_messages.printing_messages import printMessage
from temperature.Thermometers import Thermometer_I

import abc

class Temperature_Data_Logger_I(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'update_sampling_period') and
                callable(subclass.update_sampling_period) and
                hasattr(subclass, 'get_sampling_period') and
                callable(subclass.get_sampling_period) or
                NotImplemented)

    @abc.abstractmethod
    def update_sampling_period(self, period_in_secs=1):
        """Set the temperature reading period"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_sampling_period(self):
        """Returns the temperature sampling peiod"""
        raise NotImplementedError

class TemperatureDataLogger(Temperature_Data_Logger_I, Thread):
    """A concrete thermometer"""

    def __init__(self, threadname="temperature_data_logger", thermometer=Thermometer_I,
                 sampling_list=list, sampling_period_secs=1):
        self.sampling_period = sampling_period_secs  # seconds
        self.thermometer = thermometer
        self.sampling_list = sampling_list
        self.time = 0
        Thread.__init__(self, name=threadname)

    def run(self):
        printMessage("Starting Temperature Data Logger...", "*", "*")
        while True:
            sleep(self.sampling_period)
            self.time = self.time + self.sampling_period
            self.sampling_list.append(self.thermometer.read_temperature())

    def update_sampling_period(self, sampling_period_in_secs=1):
        """Set the temperature reading period"""
        self.sampling_period = sampling_period_in_secs

    def get_sampling_period(self):
        """Returns the temperature sampling peiod"""
        return self.sampling_period