import abc
import time
from threading import Thread


class Delay_I(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'pause') and
                callable(subclass.pause) and
                hasattr(subclass, 'resume') and
                callable(subclass.resume) and
                hasattr(subclass, 'abort') and
                callable(subclass.abort) or
                NotImplemented)

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

class Time_Delay(Delay_I, Thread):

    def __init__(self, threadname, mseconds):
        self.delay_mseconds = mseconds
        self.paused = False
        self.aborted = False

        Thread.__init__(self, name=threadname)

    def run(self):
        #Aqui debemos hacer un bucle while true con chequeo de pause, resume y abort
        #Este será un metodo sincrono
        reference = int(round(time.time() * 1000))
        actual = reference
        while actual < (reference + self.delay_mseconds):
            if self.aborted:
                self.aborted = False
                continue
            if not self.paused:
                actual = int(round(time.time() * 1000))
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

class Temperature_StDev_Delay(Delay_I, Thread):

    def __init__(self, stdev):
        self.stdev = stdev

    def run(self):
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