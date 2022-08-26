from queue import Queue
from threading import Thread, Event
from time import sleep

from data_structures.Observable_List import Observable_List
from logger_and_messages.printing_messages import printMessage
from temperature.Thermometers import Thermometer_I

import abc


class Temperature_Data_Logger_I(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'update_sampling_period') and
                callable(subclass.update_sampling_period) and
                hasattr(subclass, 'get_sampling_period') and
                callable(subclass.get_sampling_period) and
                hasattr(subclass, 'get_last_samples') and
                callable(subclass.get_last_samples) or
                NotImplemented)

    @abc.abstractmethod
    def update_sampling_period(self, period_in_secs=1):
        """Set the temperature reading period"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_sampling_period(self):
        """Returns the temperature sampling peiod"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_samples(self, n):
        """Returns a list with the last n samples"""
        raise NotImplementedError


class TemperatureDataLogger(Temperature_Data_Logger_I, Thread):
    """A concrete thermometer"""

    def __init__(self, threadname="temperature_data_logger", thermometer=Thermometer_I, sampling_period_secs=1):
        self.sampling_period = sampling_period_secs  # seconds
        self.thermometer = thermometer
        self.sampling_buffer = Observable_List(None)
        self.time = 0

        # For managing pause and resume the data_logger
        self.can_run = Event()
        self.can_run.set()

        Thread.__init__(self, name=threadname)

    def addEvent(self, event):
        self.sampling_buffer.addEvent(event)

    def update_sampling_period(self, sampling_period_in_secs=1):
        """Set the temperature reading period"""
        self.sampling_period = sampling_period_in_secs

    def get_sampling_period(self):
        """Returns the temperature sampling peiod"""
        return self.sampling_period

    @abc.abstractmethod
    def get_last_samples(self, n):
        """Returns a list with the last n samples"""
        if n > len(self.sampling_buffer):
            return None
        return self.sampling_buffer[-n:]

    def run(self):
        printMessage("Starting Temperature Data Logger...", "*", "*")
        while True:
            self.can_run.wait()
            self.sampling_buffer.append(self.thermometer.read_temperature())
            self.time = self.time + self.sampling_period
            sleep(self.sampling_period)

    def pause(self):
        self.can_run.clear()

    def resume(self):
        self.can_run.set()
