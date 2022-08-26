import abc
import time

class Delay_I(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'start') and
                callable(subclass.start) and
                hasattr(subclass, 'pause') and
                callable(subclass.pause) and
                hasattr(subclass, 'resume') and
                callable(subclass.resume) and
                hasattr(subclass, 'abort') and
                callable(subclass.abort) or
                NotImplemented)

    @abc.abstractmethod
    def start(self):
        """Executes the delays"""
        raise NotImplementedError

    @abc.abstractmethod
    def pause(self):
        """Pauses the delays"""
        raise NotImplementedError

    @abc.abstractmethod
    def resume(self):
        """Resumes the delays"""
        raise NotImplementedError

    @abc.abstractmethod
    def abort(self):
        """Abort the delays"""
        raise NotImplementedError

class Time_Delay(Delay_I):

    def __init__(self, mseconds):
        self.delay_mseconds = mseconds
        self.paused = False
        self.aborted = False

    def start(self):
        #Aqui debemos hacer un bucle while true con chequeo de pause, resume y abort
        #Este será un metodo sincrono
        reference = int(round(time.time() * 1000))
        actual = reference
        while actual < (reference + self.delay_mseconds):
            if not self.paused and not self.aborted:
                actual = int(round(time.time() * 1000))
            if self.aborted:
                self.aborted = False
                return
        return

    def pause(self):
        """Pauses the delays"""
        self.paused = True

    def resume(self):
        """Resumes the delays"""
        self.paused = False

    def abort(self):
        """Abort the delays"""
        self.aborted = True

class Temperature_StDev_Delay(Delay_I):

    def __init__(self, stdev):
        self.stdev = stdev

    def start(self):
        pass

    def pause(self):
        """Pauses the delays"""
        pass

    def resume(self):
        """Resumes the delays"""
        pass

    def abort(self):
        """Abort the delays"""
        pass