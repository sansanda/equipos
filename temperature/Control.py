from threading import Thread

from logger_and_messages.printing_messages import printMessage

import abc

import time

class Control_I(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'match') and
                callable(subclass.match) or
                NotImplemented)

    @abc.abstractmethod
    def match(self):
        """Gets if the control input match with the criteria"""
        raise NotImplementedError


class Delay_Control(Control_I):
    """A concrete Control based on elapsed time"""

    def __init__(self, delay):
        """
        :param delay: delay as seconds (in ms)
        """
        self.actual_time_stamp = round(time.time() * 1000)
        self.delay = delay

    def match(self):
        """
        :return: True if Control matchs the delay. False otherwise
        """
        match = False
        elapsed_time = round(time.time() * 1000) - self.actual_time_stamp
        if elapsed_time >= self.delay:
            match = True
        return match

class Delay_Control(Control_I):
    """A concrete Control based on elapsed time"""

    def __init__(self, delay):
        """
        :param delay: delay as seconds (in ms)
        """
        self.actual_time_stamp = round(time.time() * 1000)
        self.delay = delay

    def match(self):
        """
        :return: True if Control matchs the delay. False otherwise
        """
        match = False
        elapsed_time = round(time.time() * 1000) - self.actual_time_stamp
        if elapsed_time >= self.delay:
            match = True
        return match