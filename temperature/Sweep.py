from threading import Thread

from logger_and_messages.printing_messages import printMessage

import abc

from ovens.Ovens import Oven_I


class Sweep_I(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'start') and
                callable(subclass.start) and
                hasattr(subclass, 'reset') and
                callable(subclass.reset) and
                hasattr(subclass, 'next') and
                callable(subclass.next) and
                hasattr(subclass, 'previous') and
                callable(subclass.previous) or
                NotImplemented)

    @abc.abstractmethod
    def start(self):
        """Set the oven SP to the first point of the temperature profile"""
        raise NotImplementedError

    @abc.abstractmethod
    def reset(self):
        """Set the oven SP to the first point of the temperature profile"""
        raise NotImplementedError

    @abc.abstractmethod
    def next(self):
        """Set the oven SP to the next point of the temperature profile"""
        raise NotImplementedError

    @abc.abstractmethod
    def previous(self):
        """Set the oven SP to the previous point of the temperature profile"""
        raise NotImplementedError

class Control_I(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'start') and
                callable(subclass.start) and
                hasattr(subclass, 'reset') and
                callable(subclass.reset) and
                hasattr(subclass, 'next') and
                callable(subclass.next) and
                hasattr(subclass, 'previous') and
                callable(subclass.previous) or
                NotImplemented)

    @abc.abstractmethod
    def start(self):
        """Set the oven SP to the first point of the temperature profile"""
        raise NotImplementedError

    @abc.abstractmethod
    def reset(self):
        """Set the oven SP to the first point of the temperature profile"""
        raise NotImplementedError

    @abc.abstractmethod
    def next(self):
        """Set the oven SP to the next point of the temperature profile"""
        raise NotImplementedError

    @abc.abstractmethod
    def previous(self):
        """Set the oven SP to the previous point of the temperature profile"""
        raise NotImplementedError

class Tempearture_Sweep_I(Sweep_I, Thread):
    """A concrete temperature sweep"""

    def __init__(self, temperature_profile=[0], oven=Oven_I):
        self.temperature_profile = temperature_profile
        self.oven = oven
        self.temperature_profile_index = 0

    def start(self):
        printMessage("Starting Temperature Profile Runner", "*", "*")
        self.reset()

    def reset(self):
        self.temperature_profile_index = 0
        self.oven.update_temperatureSP(self.temperature_profile[self.temperature_profile_index])

    def next(self):
        if (self.temperature_profile_index + 1) >= len(self.temperature_profile): return
        self.temperature_profile_index = self.temperature_profile_index + 1
        self.oven.update_temperatureSP(self.temperature_profile[self.temperature_profile_index])

    def previous(self):
        if self.temperature_profile_index <= 0: return
        self.temperature_profile_index = self.temperature_profile_index - 1
        self.oven.update_temperatureSP(self.temperature_profile[self.temperature_profile_index])

    def get_actual_temp_step(self):
        return self.temperature_profile[self.temperature_profile_index]

    def run(self):
        printMessage("Starting Temperature Profile Runner", "*", "*")
        pass

# TODO: evitar las siguientes situaciones, actual step quede index out of bounds, inicializar una lista vacia (minimo 1), evitar oven None
class Tempearture_Profile_Runner(Tempearture_Profile_Runner_I, Thread):
    """A concrete temperature profile runner"""

    def __init__(self, temperature_profile=[0], oven=Oven_I):
        self.temperature_profile = temperature_profile
        self.oven = oven
        self.temperature_profile_index = 0

    def start(self):
        printMessage("Starting Temperature Profile Runner", "*", "*")
        self.reset()

    def reset(self):
        self.temperature_profile_index = 0
        self.oven.update_temperatureSP(self.temperature_profile[self.temperature_profile_index])

    def next(self):
        if (self.temperature_profile_index + 1) >= len(self.temperature_profile): return
        self.temperature_profile_index = self.temperature_profile_index + 1
        self.oven.update_temperatureSP(self.temperature_profile[self.temperature_profile_index])

    def previous(self):
        if self.temperature_profile_index <= 0: return
        self.temperature_profile_index = self.temperature_profile_index - 1
        self.oven.update_temperatureSP(self.temperature_profile[self.temperature_profile_index])

    def get_actual_temp_step(self):
        return self.temperature_profile[self.temperature_profile_index]

    def run(self):
        printMessage("Starting Temperature Profile Runner", "*", "*")
        pass